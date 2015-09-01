import census
import os
import sys
import json

utils = os.path.abspath(os.path.join('..',"utils"))
sys.path.insert(0, utils)

import fileio as io
import pandas as pd

c = census.Census()

vars = []
var_names = []
for key,value in c.acs_variables.items():
    #print key
    for k,v in value.items():
        vars.append(v["variable"])
        var_names.append(k)


all_zips_file = io.read_file(os.path.join('..',"data", "zip_code_master.csv"))
all_zips = [x.split(",")[0] for x in all_zips_file[1:]]
print len(all_zips)

vars_1 = vars[0:49]
var_names_1 = var_names[0:49]
vars_2 = vars[50:99]
var_names_2 = var_names[50:99]
vars_3 = vars[100:]
var_names_3 = var_names[100:]

zip_query_1 = c.get(vars_1,year=2013, survey="acs5", zip_codes="*")

zip_query_2 = c.get(vars_2,year=2013, survey="acs5", zip_codes="*")

zip_query_3 = c.get(vars_3,year=2013, survey="acs5", zip_codes="*")
print "zip_query_1 length: ", len(zip_query_1)
print "zip_query_1 length: ", len(zip_query_2)
print "zip_query_1 length: ", len(zip_query_3)

'''
zips_after_api = [x[-1] for x in zip_query_1[1:]]

remaining_zips = set(all_zips) - set(zips_after_api)
print remaining_zips

zip_query_4 = c.get(vars_1,year=2013, survey="acs5", zip_codes=list(remaining_zips))
print zip_query_4
'''

zip_frame_1 = pd.DataFrame(zip_query_1, columns=var_names_1 + ["name", "zip"] )
zip_frame_1 = zip_frame_1.reindex(zip_frame_1.index.drop(0))
print len(zip_frame_1)
#print zip_frame_1

zip_frame_2 = pd.DataFrame(zip_query_2, columns=var_names_2 + ["name", "zip"] )
zip_frame_2 = zip_frame_2.reindex(zip_frame_2.index.drop(0))
print len(zip_frame_2)

zip_frame_3 = pd.DataFrame(zip_query_3, columns=var_names_3 + ["name", "zip"] )
zip_frame_3 = zip_frame_3.reindex(zip_frame_3.index.drop(0))
print len(zip_frame_3)



total_frame = zip_frame_1.merge(zip_frame_2,on="zip")
total_frame = total_frame.merge(zip_frame_3,on="zip")
#print len(total_frame)


del total_frame["name_x"]
del total_frame["name_y"]
 

#print total_frame

total_frame.to_csv("census_all_zips.csv", columns=["zip"]+var_names_1+var_names_2+var_names_3)
