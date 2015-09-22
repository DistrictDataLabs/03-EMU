
library(sqldf)
library(glmnet)
library(stringr)

setwd("~/R-files/saturation")

zipbiz13 <- read.csv("zbp13detail.txt", header=TRUE) #CBP Zipcode 2013
zipbiz09 <- read.csv("zbp09detail.txt", header=TRUE) #CBP Zipcode 2009


#Processing census data
zcta2 <- read.csv("nhgis0003_ds201_20135_2013_zcta_E.csv", header=TRUE) #NHGIS population 
zcta2 <- zcta2[,c("ZCTA5A","UEPE001")]
colnames(zcta2) <- c("zip","pop")
zcta2 <- zcta2[-1,]
zcta2$zip <- as.character(zcta2$zip)
zcta2$zip5 <- sprintf("%05s", zcta2$zip)
zcta2$pop <- as.numeric(as.character(zcta2$pop))
zcta2$zip =NULL

# Starbucks data from NN
sbux_nn = read.csv("sbux_log_reg_out.csv", header=TRUE)
sbux_nn$zip <- as.character(sbux_nn$zip)
sbux_nn$zip5 <- sprintf("%05s", sbux_nn$zip)
sbux_nn$actual=NULL
sbux_nn$zip = NULL

##CBP Data
zipbiz13 <- zipbiz13[,c("zip","naics","est")]
colnames(zipbiz13)<-c("zip","naics","est13")
zipbiz09 <- zipbiz09[,c("zip","naics","est")]
colnames(zipbiz09)<-c("zip","naics","est09")
zipbiz <- merge(zipbiz09,zipbiz13,by=c("zip","naics"))

naics_list <- c("11","21","22","23","31","42","44","48", "51","52","53","54","55","56","61","62","71","72","81")

for (i in 1:length(naics_list))
{
  tmp_string <- paste(naics_list[i],"----",sep="")
  zipbiz2 <- zipbiz[zipbiz$naics==tmp_string,]
  zipbiz2$zip5 <- sprintf("%05s",zipbiz2$zip)
  zipbiz2[is.na(zipbiz2)]<-0
  zipbiz2$cagr <- ((zipbiz2$est13/zipbiz2$est09)^(1/5))-1

  zipbiz2 <- merge(zipbiz2, zcta2, by = c("zip5"))
  zipbiz2$busprop <- zipbiz2$est13*1000/zipbiz2$pop
  zipbiz2 <- zipbiz2[zipbiz2$busprop <Inf,]
  zipbiz2$busprop <- zipbiz2$busprop/summary(zipbiz2$busprop)[5] # scale by 75 percentile , need to revisit
  zipbiz2$busprop[zipbiz2$busprop >=1] <-1 # cap ratio to 1
  
  zipbiz2 <- merge(zipbiz2, sbux_nn, by = c("zip5"))
  zipbiz2$sat_score = sqrt((zipbiz2$sbux_prob -0.25)^2+(zipbiz2$busprop-0.5)^2 + (zipbiz2$cagr-0.75)^2) # distance from ideal< CAGR = 0.75, BP = 0.5>
  zipbiz2$sat_score_per <- min(zipbiz2$sat_score)*100/zipbiz2$sat_score
  
  zipbiz_tmp <- zipbiz2[,c("zip5","cagr","busprop","sbux_prob","sat_score","sat_score_per")]  
  names(zipbiz_tmp)[-1] <- paste(names(zipbiz_tmp)[-1],naics_list[i])
  
  if (i ==1)
    zipbiz_final <- zipbiz_tmp
  else
    zipbiz_final <- merge(zipbiz_final,zipbiz_tmp, by= c("zip5"), all = TRUE) # <naics,zip> not the same for all naics code
}

  write.csv(zipbiz_final,"Sat_score_metric_ALL.csv",row.names=F,na="")
