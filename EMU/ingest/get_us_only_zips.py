import os
import sys
import json

utils = os.path.abspath(os.path.join('..',"utils"))
sys.path.insert(0, utils)

import fileio as io

all_zips_file = io.read_file(os.path.join('..',"data", "zip_code_master.csv"))
all_zips = set([x.split(",")[0] for x in all_zips_file[1:]])
print len(all_zips)

final_data_file = []
census_all_zips = io.read_file(os.path.join('..',"data", "census_all_zips.csv"))
census_zips = set([x.split(",")[0] for x in census_all_zips[1:]])
print len(census_zips)

print len(census_zips - all_zips)

final_data_file.append(census_all_zips[0])
for line in census_all_zips[1:]:
    #print line.split(",")[0] 
    if line.split(",")[0] in all_zips:
        final_data_file.append(line)
        
        
io.write_file(final_data_file,os.path.join('..',"data", "census_all_us_zips.csv"))
    
    