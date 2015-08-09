'''
Created on Jul 13, 2015

@author: Erich O'Saben

'''
import sys
import os



def get_project_dirs(project_root_name):
    '''
    Given a project root directory name, returns a python dict with all directory paths.

    Each directory is accessed as a key of the dict. Nested directories are seperated by a "."
    The root level directory can be accessed by the key 'project'
    '''
    path = sys.path[0].split(os.sep)
    project_index = path.index(project_root_name)

    project_root = os.path.join("/",*path[:project_index + 1])
    
    DIRS = {'project': project_root}
       
    root_dir_split = project_root.split(os.sep)
    if root_dir_split[-1] == '':
        root_dir = root_dir_split[-2]
    else:
        root_dir = root_dir_split[-1]
    
    for root, dirnames, filenames in os.walk(project_root): 

        root_split = root.split(os.sep)
        root_index = root_split.index(root_dir)

        for name in dirnames:
            if name[0] == '.':
                continue
                   
            path_stem = ""
            if len(root_split) - root_index > 1:
                for i in range(root_index +1,len(root_split)):
                    path_stem += root_split[i] + "."
            
            DIRS[path_stem + name] = os.path.join(root, name)
        
        
    return DIRS