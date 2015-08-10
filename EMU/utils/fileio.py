'''
Created on Dec 16, 2014

@author: Erich O'Saben


Implements common IO operations for files. Most implementations were taken from https://docs.python.org/2/library/csv.html

On Github at https://github.com/ErichdotPy/PythonUtils
'''

import csv
import sys
import json

def read_delimited(filename, mode='rU', d=',', q=0):
    """
    Reads delimited files one line at a time and appends to a list.

    @return: contents of the file

    q=0 means 'csv.QUOTE_NONE'

    Additional quoting options can be found at: https://docs.python.org/2/library/csv.html
    """

    file_contents = []
    with open(filename, mode) as f:
        reader = csv.reader(f, delimiter=d, quoting=q)
        try:
            for row in reader:
                file_contents.append(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
    
    
    return file_contents
    

def write_delimited(contents, outputFilePath, mode='wb', d=',', q=0):    
    """
    Writes a delimited file, default setting is csv.

    q=0 means 'csv.QUOTE_NONE'

    Additional quoting options can be found at: https://docs.python.org/2/library/csv.html
    """

    with open(outputFilePath, mode) as f :
        writer = csv.writer(f, delimiter=d, quoting=q)
        try:
            for c in contents:
                writer.writerow ([c])
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (outputFilePath, writer.line_num, e))
            
    



def read_file(filename, mode='rU', stripChar='\n', replaceChar='', lines=False):
    """
    Basic implementation of reading a text file into a list. Default is to read one line at a time. 

    If lines=True, uses read.readlines() and return each line of the file as is (includes all whitespace and newline chars)

    If lines=False will strip will remove all characters specified in stripChar and replace with replaceChar. Defaults of those settings are "\n" and "" respectively.

    @return: contents of the file
    """
    with open(filename, mode) as f:
        if lines:
            file_contents = f.readlines()
        else:
            file_contents = []
            for line in f:
                file_contents.append(line.replace(stripChar,replaceChar).strip()),
    
    return file_contents




def write_file(contents, filename, mode='wb'):
    """
    Basic implementation of writing to a text file. Each line of a list is a line in the file.

    If you have nested lists, loop the call to this function passing each inside list as the contents and change to mode to mode='a'
    """
    with open(filename, mode) as f:
        for c in contents:
            f.write("%s\n" % c)
    f.close()


    
def write_file_dict(contents, filename, mode='wb'):
    """
    Basic implementation of writing a Python dictionary to file. Writes item in the dict as ''key: value''.

    If you have nested key/value pairs, loop the call to this function passing each key/value pair as the contents and change to mode to mode='a'.

    Can be used in pair with write_file or write_delimited if nested values are lists. Also make sure that their mode is changed to mode='a'
    """
    with open(filename, mode) as f:
        for k,v in contents.items():
            f.write("{0}: {1}\n".format(k,v))
    



def write_matrix_csv(matrix_contents, filename, mode='wb'):

    """
    Basic implementation of writing a matrix to a CSV file.

    matrix_contents must be a list of lists which each nested list is a row in the matrix. 
    For proper viewing in spreadsheet applications make matrix_contents[0][0] = ''
    For example the matrix:

        A   B   
    a   2   3    
    b   4   5 
    

    where A and B are column headers and a and b are row names. matrix_contents would look like:

    matrix_contents = [['', 'A', 'B'], ['a', 2, 3], ['b', 4, 5]]
    """

    with open(filename, mode) as f:
        writer = csv.writer(f)
        [writer.writerow(r) for r in matrix_contents]
    



def write_json(data,filename, sort_keys=False,mode='wb'):
    """
    Basic implementation to write a Python dict to a json file.
    """

    with open(filename , mode) as f:
        json.dump(data, f,sort_keys)
    


def read_json(filename,json_objs=False):
    """
    Provides two different types of read operations for a json file. If the file is a well formed json document, k  and 
    this will return a python dict of the json structure. If the file is multiple lines of json 
    objects, set the json_objs flag to true and a list of Python dictionaries will be returned.
    """
    
    if json_objs:
        file_contents = []
        with open(filename) as f:
            for line in fin:
                file_contents.append(json.loads(line))
        
        return file_contents
    else:
        file_contents = json.loads(open(filename).read())

    return file_contents