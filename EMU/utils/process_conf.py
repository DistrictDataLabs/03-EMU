"""
Accesses and Reads the users API.conf file. Assumes the file is within the EMU directory structure
"""
import os
import project_dirs as pds
import fileio as io


DIRS = pds.get_project_dirs("EMU")

def get_api_key(api):
    api_file = io.read_file(os.path.join(DIRS["project"], "API.conf"))
    #print api_file
    
    for line in api_file:
        #skip empty lines
        if line:
            #skip comment lines
            if line[0] == "#":
                continue
            line_split = line.split(":")
            if line_split[0].lower() == api.lower():
                return line_split[1].strip()
                
    
    
    


