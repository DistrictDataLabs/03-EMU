import os
import sys

utils = os.path.abspath(os.path.join('..'))
sys.path.insert(0, utils)

import utils.fileio as io

contents = io.read_delimited(os.path.join('..',"data", "DSBS_NCCombined.csv"))

#read each file from line 1 on
for line in contents[1:]:
    #split last index of each line in the file
    line_split = line[-1].split()
    print line_split