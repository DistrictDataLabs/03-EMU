import sys
import os
import urllib
import ast
import json
utils = os.path.abspath(os.path.join('..'))
sys.path.insert(0, utils)

#print sys.path

import utils.process_conf as conf
import utils.fileio as io
import utils.project_dirs as pds

DIRS = pds.get_project_dirs("EMU")

"""
Provides access to the Census ACS API.

Much of this class was based on/inspired by the CITYSDK. Visit http://uscensusbureau.github.io/citysdk/ for more information. 

The following types of surveys are available for each year:
2010: acs5
2011: acs5
2012: acs5, acs3, acs1
2013: acs5, acs3, acs1


"""

class Census:
    def __init__(self):
        self.key = conf.get_api_key("census")
        self.nat_codes = self.__set_nat_codes() #uses the two letter state abbrevation to access the state in the API.
        self.acs_variables = self.__set_acs_vars()  #acs api variables in major topics of Age,Economic,Poverty,Commute,Education,Employment,Housing,Population
        self.state_county_codes = self.__set_state_county() #a python dict of all counties listed by state. Use the 2 letter state abbrev. to access the availble counties
        
        #used for ACS survey validation
        self.__survey_types = {
            "2010": ["acs5"],
            "2011": ["acs5"],
            "2012": ["acs5", "acs3", "acs1"],
            "2013": ["acs5", "acs3", "acs1"]
            }

    """
    Returns a list of lists of data from the Census API based on a given set of variables. Each index of the list is a row in the returned data set. 
    Index 0 is the header row.
    
    States can be passed as their two letter abbreviation code. Counties must be passed as their ACS API numerical code. Use state_county_codes for a reference.
    
    Each location parameter and the variables parameter must be lists. Year can be a string or int. survey indicates the whether it's a 1, 3, or 5, ACS profile.
    
    Currently the following location hierarchies are implemented:
    State, County
    State Only
    County Only -> USE W/ Caution! Will query every state for the given county code. Probably not very useful..
    Zip Codes -> Census API does not allow for zip codes to be combined with any other hierarchy.
    """
    def get(self,variables, year=2011, survey="acs5", states=None, counties=None, zip_codes=None):
        #validate parameters
        if survey[:3] == "acs":
            self.__validate_params(survey, year)
        
        
        if isinstance(variables, basestring):
            sys.stderr.write("Variables must be in a list. If only one variable is being queried, put brackets around the string. ie c.get(['B00002_001E'])")
        
             
        var_string = ",".join([x for x in variables])
        
        base_url = 'http://api.census.gov/data/{0}/{1}?key={2}&get={3},NAME&for='.format(str(year), survey, self.key, var_string)
        
        #zip codes
        if zip_codes:
            if states or counties:
                sys.stderr.write("NOTE: Census API does not permit a location heirarchy with zip codes. Only returning data by zip codes.")
            
            zip_string = ",".join([x for x in zip_codes])
            final_url = base_url + "zip+code+tabulation+area:{0}".format(zip_string)
            
        #states and counties
        elif states and counties:
            county_string = ",".join([x for x in counties])
            state_string = ",".join([self.nat_codes[x]["num"] for x in states])
            final_url = base_url + "county:{0}&in=state:{1}".format(county_string,state_string)
        #counties only -> ALL STATES WILL BE QUERIED.         
        elif counties:
            if counties == "*":
                county_string = counties
            else:
                county_string = ",".join([x for x in counties])
                
            final_url = base_url + "county:{0}&in=state:*".format(county_string)
        #states only
        elif states:
            if states == "*":
                state_string = states
            else:
                state_string = ",".join([self.nat_codes[x]["num"] for x in states])
            
            final_url = base_url + "state:{0}".format(state_string)
        else:
            sys.stderr.write("Your location preference was not recognized")
            os._exit(-1)
        
        
        print "\nquerying: ", final_url
        response = urllib.urlopen(final_url)
        response_value = response.read()
       
        try:
            response_json = json.loads(response_value)
            return response_json
        except ValueError as e:
            print "an error occured:"
            sys.stderr.write(response_value)
            os._exit(-1)
        
        
        
                
    """
    Provides the ability to write a custom API call. Only 'http://api.census.gov/data/' is given and the user must fill in the rest.
    
    The data returned is in the same structure as in the "get" function.
    """ 
    def manual_query(self, query_string):
        base_url = 'http://api.census.gov/data/'
        final_url = base_url + query_string
        
        print "\nquerying: ", final_url
        response = urllib.urlopen(final_url)
        response_value = response.read()
        try:
            response_json = json.loads(response_value)
            return response_json
        except ValueError as e:
            print "an error occured:"
            sys.stderr.write(response_value)
            os._exit(-1)
        
    
    """
    Reads in the national_fips_codes.txt file to a python dict. The two letter state abbreviation is the key to access the state's codes.
    """
    def __set_nat_codes(self):
        fips_file = io.read_file(os.path.join(DIRS["data"],"national_fips_codes.txt"))
        nat_codes = {}
        for line in fips_file[1:]:
            line_split = line.split("|")
            nat_codes[line_split[1]] = {"num":line_split[0], "state_name":line_split[2], "fips":line_split[3]}
        
        return nat_codes
    
    def __set_acs_vars(self):
        return io.read_json(os.path.join(DIRS["data"],"acs_variables.json"))
       
    """
    Validates API parameters before making the request. Checks obvious errors/omission to catch the error before the call. 
    """
    def __validate_params(self, survey, year):
        if survey not in self.__survey_types[str(year)]: 
            sys.stderr.write("The year and survey type your requested are invalid. See documentation to see valid combinations.")
            os._exit(-1)
    """
    Returns a python dict of every county and their ACS API code listed out by state. 
    
    
    """     
    def __set_state_county(self):
        state_county_file = io.read_delimited(os.path.join(DIRS["data"],"acs_state_county_codes.csv"))
        
        state_county = {}
        for line in state_county_file[1:]:
            if line[2] in state_county.keys():
                state_county[line[2]][line[4]] = line[5]
            else:
                state_county[line[2]] = {}
                
        return state_county  
        
        
        
