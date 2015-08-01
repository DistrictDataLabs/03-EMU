import urllib
import ast

#Get per capita income 

ListofStates = []
ListofState_Elements = ()

class Census:
    def __init__(self, key):
            self.key = 'be9a3def7712bc7334bfe885e1ca46943be121e7'

    def get(self, fields, geo, year=2010, dataset='sf1'):
        fields = [','.join(fields)]
        base_url = 'http://api.census.gov/data/%s/%s?key=%s&get=' % (str(year), dataset, self.key)
            #http://api.census.gov/data/2010/sf1?key=be9a3def7712bc7334bfe885e1ca46943be121e7&get=DP03_0043M&for=state:25

        query = fields
        for item in geo:
            query.append(item)
        add_url = '&'.join(query)
        url = base_url + add_url
        print(url)
        response = urllib.urlopen(url)
        return response.read()

def FindStates(ListofStates_Output):
    for StateRow in range(1,len(ListofStates_ListOutput)):
        ListofStates_Elements = ListofStates_ListOutput[StateRow]
        
        #Split list into the 3 elements of each state:  
        for StateElement in range(0, len(ListofStates_Elements)):
            if StateElement == 0:
                CurrentStateElement = int(ListofStates_Elements[StateElement])
            else:
                CurrentStateElement = ListofStates_Elements[StateElement]
            print CurrentStateElement

def FindFIPS(ListofFIPS_Output):
    for FIPSRow in range(1,len(ListofFIPS_ListOutput)):
        ListofFIPS_Elements = ListofFIPS_ListOutput[FIPSRow]
        
        #Split list into the 3 elements of each FIPS code:  
        for FIPSElement in range(0, len(ListofFIPS_Elements)):
            if FIPSElement == 0:
                #CurrentFIPSElement = int(ListofFIPS_Elements[FIPSElement])
                CurrentFIPSElement = ListofFIPS_Elements[FIPSElement]
            else:
                CurrentFIPSElement = ListofFIPS_Elements[FIPSElement]
            print CurrentFIPSElement

def FindZips(ListofZips_Output):
    for ZipsRow in range(1,len(ListofZips_ListOutput)):
        ListofZips_Elements = ListofZips_ListOutput[ZipsRow]
        
        #Split list into the 3 elements of each Zip Code:  
        for ZipsElement in range(0, len(ListofZips_Elements)):
            if ZipsElement == 0:
                #CurrentZipsElement = int(ListofZips_Elements[ZipsElement])
                CurrentZipsElement = ListofZips_Elements[ZipsElement]
            else:
                CurrentZipsElement = ListofZips_Elements[ZipsElement]
            print CurrentZipsElement

'''def FindCounties(ListofCounties_Output):
    for CountiesRow in range(1,len(ListofCounties_ListOutput)):
        ListofCounties_Elements = ListofCounties_ListOutput[CountiesRow]
        
        #Split list into the 3 elements of each Zip Code:  
        for CountiesElement in range(0, len(ListofCounties_Elements)):
            if CountiesElement == 0:
                #CurrentCountiesElement = int(ListofCounties_Elements[CountiesElement])
                CurrentCountiesElement = ListofCounties_Elements[CountiesElement]
            else:
                CurrentCountiesElement = ListofCounties_Elements[CountiesElement]
            print CurrentCountiesElement'''

if __name__ == '__main__':
    c = Census('be9a3def7712bc7334bfe885e1ca46943be121e7')
    #______________________________________________________________________________________
    #grab the list of states with their IDs
    '''ListofStates_Output = c.get(['P0010001,NAME'],['for=state:*'])'''

    #grab the list of FIPS with their IDs
    '''ListofFIPS_Output = c.get(['P0010001,NAME'],['for=place:*'])'''

    #grab the list of zip codes with their IDs
    ListofZips_Output = c.get(['B00001_001E'],['zip+code+tabulation+area:20001'])

    #grab the list of Counties with their IDs
    '''ListofCounties_Output = c.get(['P0010001'],['county:*'])'''

    #______________________________________________________________________________________
    # Cast results to list type
    #Call state
    '''ListofStates_ListOutput = ast.literal_eval(ListofStates_Output.decode('utf8'))
                FindStates(ListofStates_Output)'''

    #Call FIPS codes
    '''ListofFIPS_ListOutput = ast.literal_eval(ListofFIPS_Output.decode('utf8'))
                FindFIPS(ListofFIPS_Output)'''

    #Call Zip Codes
    ListofZips_ListOutput = ast.literal_eval(ListofZips_Output.decode('utf8'))
    FindZips(ListofZips_Output)

    #Call Counties
    '''ListofCounties_ListOutput = ast.literal_eval(ListofCounties_Output.decode('utf8'))
                FindCounties(ListofCounties_Output)'''