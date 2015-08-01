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

if __name__ == '__main__':
    c = Census('be9a3def7712bc7334bfe885e1ca46943be121e7')
    #______________________________________________________________________________________

    #grab the list of FIPS with their IDs
    ListofFIPS_Output = c.get(['P0010001,NAME'],['for=place:*'])
   
    #______________________________________________________________________________________
    # Cast results to list type
    #Call FIPS codes
    ListofFIPS_ListOutput = ast.literal_eval(ListofFIPS_Output.decode('utf8'))
    FindFIPS(ListofFIPS_Output)