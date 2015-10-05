library(caret)
library(dplyr)
library(tidyr)
#Import data 
zctan <- read.csv("census_naicsCount_ALL_zip.csv")

dim(zctan) # 33120, 123
sbux <- read.csv("socrata.csv", header=TRUE) ##Starbucks file from Socrata
dim(sbux) #22625    21

#Starbucks Data
sbux<-sbux[sbux$Country=="US",]
sbux$zip5 <- as.numeric(substr(as.character(sbux$Postal.Code),1,5))
sbux_a <- data.frame(zip5=unique(sbux$zip5),binary_sbux=1)
colnames(sbux_a) <- c("zip","binary_sbux")
summary(sbux_a)

#Process NHGIS data
zcta <- merge(sbux_a,zctan,by="zip",all.y=T)
zcta$binary_sbux[is.na(zcta$binary_sbux)]<-0
zcta[is.na(zcta)]<-0

# Data cleaning by population
hist(zcta$population)
table(zcta$binary_sbux)
hist(zcta$binary_sbux)
zcta_pop2 <- zcta %>% select(-X) %>% 
  filter(population > 100) %>% 
  mutate_each(funs(as.numeric), 3:124)

# Examine the data
table(zcta_pop2$binary_sbux)
hist(zcta_pop2$binary_sbux)
dim(zcta_pop2)
dim(zcta)

#### Run model in parallel ####
library(doParallel)
cl <- makeCluster(detectCores())
registerDoParallel(cl)
### Make Sure to Stop at End ####

# Caret Models
set.seed(1234)

# GLM Net
zcta_glm <- zcta_pop2
dim(zcta_glm)
head(zcta_glm)
zcta_glm$binary_sbux <- as.factor(zcta_glm$binary_sbux)
zcta_glm <- zcta_glm %>% mutate_each(funs(as.numeric), 3:140)

# Split Data into Training and Test set
splitIndex <- createDataPartition(zcta_glm$binary_sbux, p = .75, list = FALSE, times = 1)
trainDF <- zcta_glm[ splitIndex,]
testDF  <- zcta_glm[-splitIndex,]


ctrl <- trainControl(method = "repeatedcv", repeats = 5, number = 10)
glmnGrid <- expand.grid(.alpha = c(0, .1, .2, .4, .6, .8, 1),
                        .lambda = seq(.01, .2, length = 40))

glmnTuned <- train(binary_sbux ~ ., 
                   data = trainDF, 
                   method = "glmnet",
                   tuneGrid = glmnGrid,
                   preProc = c("center", "scale"), 
                   trControl = ctrl)

plot(glmnTuned, plotType = "level")
plot(glmnTuned, plotType = "line")

glmtest <- predict(glmnTuned, newdata = testDF)
print(postResample(pred=glmtest, obs=as.factor(testDF[,"binary_sbux"])))

stopCluster(cl)
