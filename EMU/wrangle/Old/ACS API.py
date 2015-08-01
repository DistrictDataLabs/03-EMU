import urllib
import ast

#Get per capita income 

ListofStates = []
ListofState_Elements = ()

class Census:
    def __init__(self, key):
            self.key = 'be9a3def7712bc7334bfe885e1ca46943be121e7'

    def get(self, fields, geo, year=2011, dataset='sf1'):
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

if __name__ == '__main__':
    c = Census('be9a3def7712bc7334bfe885e1ca46943be121e7')
    #______________________________________________________________________________________

    #grab the list of zip codes with their IDs
    ListofZips_Output = c.get(['B00001_001E'],['for=zip+code+tabulation+area:*'])

    #______________________________________________________________________________________
    # Cast results to list type
    #Call Zip Codes
    ListofZips_ListOutput = ast.literal_eval(ListofZips_Output.decode('utf8'))
    FindZips(ListofZips_Output)
