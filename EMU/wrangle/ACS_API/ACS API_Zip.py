import urllib
import ast

#Get per capita income 

ListofStates = []
ListofState_Elements = ()

class Census:

    #def get(self, fields, geo, year=2013, dataset='sf1'):
    def get(self, fields, geo, year=2011, dataset='acs5'):
        fields = [','.join(fields)]
        base_url = 'http://api.census.gov/data/%s/%s?&get=' % (str(year), dataset)
            #http://api.census.gov/data/2010/sf1?key=be9a3def7712bc7334bfe885e1ca46943be121e7&get=DP03_0043M&for=state:25

        query = fields
        for item in geo:
            query.append(item)
        add_url = '&'.join(query)
        url = base_url + add_url
        print(url)
        response = urllib.urlopen(url)
        print response.read()

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

if __name__ == '__main__':
    c = Census()
    #______________________________________________________________________________________
    #grab the list of states with their IDs
    ListofStates_Output = c.get(['B00001_001E'],['for=zip+code+tabulation+area:*'])

    #______________________________________________________________________________________
    # Cast results to list type
    #Call state
    ListofStates_ListOutput = ast.literal_eval(ListofStates_Output.decode('utf8'))
    FindStates(ListofStates_Output)