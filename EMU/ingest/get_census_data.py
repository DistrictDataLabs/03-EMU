import census
import os
import sys
import json

utils = os.path.abspath(os.path.join('..',"utils"),)
sys.path.insert(0, utils)

import fileio as io
import pandas as pd



vars = []
var_names = []
for key,value in c.acs_variables.items():
    print key
    for k,v in value.items():
        vars.append(v["variable"])
        var_names.append(k)


yelp_zips = io.read_file(os.path.join('..',"data", "yelp_zipcodes.csv"))


print len(vars)

vars_1 = vars[0:49]
var_names_1 = var_names[0:49]
vars_2 = vars[50:99]
var_names_2 = var_names[50:99]
vars_3 = vars[100:]
var_names_3 = var_names[100:]

zip_query_1 = c.get(vars_1,year=2013, survey="acs5", zip_codes=yelp_zips)
zip_query_2 = c.get(vars_2,year=2013, survey="acs5", zip_codes=yelp_zips)
zip_query_3 = c.get(vars_3,year=2013, survey="acs5", zip_codes=yelp_zips)


zip_frame_1 = pd.DataFrame(zip_query_1, columns=var_names_1 + ["name", "zip"] )
zip_frame_1 = zip_frame_1.reindex(zip_frame_1.index.drop(0))

zip_frame_2 = pd.DataFrame(zip_query_2, columns=var_names_2 + ["name", "zip"] )
zip_frame_2 = zip_frame_2.reindex(zip_frame_2.index.drop(0))

zip_frame_3 = pd.DataFrame(zip_query_3, columns=var_names_3 + ["name", "zip"] )
zip_frame_3 = zip_frame_3.reindex(zip_frame_3.index.drop(0))



total_frame = zip_frame_1.merge(zip_frame_2,on="zip")
total_frame = total_frame.merge(zip_frame_3,on="zip")

del total_frame["name_x"]
del total_frame["name_y"]
 

print total_frame

total_frame.to_csv("census_by_zip.csv", columns=["zip"]+var_names_1+var_names_2+var_names_3)