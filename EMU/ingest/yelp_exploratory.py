'''
Basic script to show how to access the businesses records and reviews within the Yelp data set that are specific to starbucks.
'''



import json

'''
returns a list of json objects and each json object is a review.
'''
def get_reviews(file_path):
    reviews = []
    with open(file_path) as fin:
        for line in fin:
            reviews.append(json.loads(line))
    
    print "available keys in reviews: ", reviews[0].keys()
    return reviews

'''
returns a list of json objects and each json object is a business record.

This file is very big. May take a while to complete this step.
'''
def get_businesses(file_path):                           
    businesses = []
    with open(file_path) as fin:
        for line in fin:
            businesses.append(json.loads(line))
    
    print "available keys in businesses: ", businesses[0].keys()
    return businesses            

'''
returns a list of json objects and each json object is a starbucks business record.
'''                
def get_starbucks(businesses):                
    starbucks = []
    for b in businesses:
        if b['name'] == 'Starbucks' or b['name'] == 'starbucks':
            starbucks.append(b['business_id'])
    
    return starbucks

'''
returns a list of dates that are associated with starbucks reviews..
'''
def get_sbux_review_dates(reviews, starbucks):        
    dates = []
    for r in reviews:
        if r['business_id'] in starbucks:
            dates.append(r['date'])
    
    return dates
            
def main():      
    #UPDATE FILE PATHS TO YOUR LOCAL FILES. IF ON WINDOWS, YOU WILL NEED TO CHANGE PATH SEPERATOR FROM "/" TO "\"
    bus_file_path = "PATH/TO/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json"
    rev_file_path = "PATH/TO/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json"
     
    businesses = get_businesses(bus_file_path)
    print "number of businesses available: ", len(businesses)
    
    reviews = get_reviews(rev_file_path)
    print "number of reviews available: ", len(reviews)   
    
    sbux = get_starbucks(businesses)
    print "number of starbucks: ", len(sbux)
    dates = get_sbux_review_dates(reviews, sbux)
    
    print "ranges of dates of starbucks reviews in the data set:", sorted(dates)[0],sorted(dates)[-1]


if __name__ == '__main__':
    main()
