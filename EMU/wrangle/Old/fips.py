import urllib
import ast

#Get per capita income 

ListofStates = []
ListofState_Elements = ()


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