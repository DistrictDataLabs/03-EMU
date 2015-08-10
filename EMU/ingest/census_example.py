"""
Some basic examples of how to use the Census API class...
"""

import census

"""
Before you use this, do the following:
1. There is a file called API.conf.SAMPLE, copy this file and rename it to API.CONF
2. Move this file so it is in the EMU directory (NOT 03-EMU directory)
3. Copy and paste your Census API key in the spot. We will be using this file from now on to hide our API keys (not committing them to github).
"""

c = census.Census()

"""
Set your variables...
"""
# python dict of commonly used variables
print "Top level categories: ", c.acs_variables.keys()

econ_income = c.acs_variables['Economic']['income']['variable']
print "econ_income variable: ", econ_income

age_vars = []
for key,value in c.acs_variables["Age"].items():
    print key
    age_vars.append(value["variable"])

query_variables = age_vars + [econ_income]
print "\nAll variables to be queried: ", query_variables

"""
Set your locations...
"""
print "\nHow to access counties within a state: " 
print c.state_county_codes.keys()
print c.state_county_codes["VA"]
print "Get a county code: ",
county_code = c.state_county_codes["VA"]["Fairfax"]
print county_code


"""
Query!
"""
response = c.get(query_variables, counties=[county_code], states=["VA"])

for r in response:
    print r


#user defined variables
response_2 = c.get(["B01002_002E"], zip_codes=["20001"])
for r in response_2:
    print r

#manual query, 'http://api.census.gov/data/' is provided..fill in the rest..
response_3 = c.manual_query("2011/acs5?&get=B01002_002E,NAME&for=zip+code+tabulation+area:20001")
for r in response_3:
    print r

#all states...
response_4 = c.get(["B01002_002E"], states="*")
for r in response_4:
    print r


