For this MVP, we hope to find a correlation between income and number of Starbucks stores in Meclenburg County, North Carolina. We collected the data for each of the 29 area zipcodes of Meclenburg County. A D3 Map Visualization is built with color overlay of per capita income on counties and bubbles showing number of starbucks in that county.

## Main Issues

Commerce data provides data that is optimal for planning and research of general socioeconomic and demographic patterns. Generally, increased geographic specificity equates to longer time steps. Shorter time steps equates to more geographic aggregation. 

The data does not provide sufficient resolution to develop high resolution market segmentation, which likely requires new factors of business quality and activity. By leveraging emerging data sources from tech sector, imagine what new insight emerging data can provide to improve the public’s understanding of American life and how the combination of mature and emerging may vastly improve investment decisions.

## Getting Data

US Census Bureau’s ACS-5-year Census Tract Summaries ([Census Site] (http://www.census.gov/data/developers/data-sets/acs-survey-5-year-data.html) or [NHGIS] (https://nhgis.org/) - Easier to Use)

Description: The American Community Survey (ACS) is collected annually by the US Census Bureau and aids in monitoring trends and prepare for future data collection efforts. The 5-year Census tract summaries data contains tract-level aggregates for 2009 through 2013. 

US Census Tract Shapefiles ([here] (https://www.census.gov/cgi-bin/geo/shapefiles2014/layers.cgi))

Description: In order to visualize tracts or conduct spatial join operations, the US Census Tract Shapefiles (vector polygon) are required.

Starbucks Locations ([here] (https://opendata.socrata.com/Business/All-Starbucks-Locations-in-the-World-Point-Map/7sg8-44ed))

Description: An open data post on Socrata containing Starbucks locations around the world. Candidate dataset for a lead metric of market change. 

Yelp Challenge Data ([here] (http://www.yelp.com/dataset_challenge))

Description: A multi-city selection of Yelp data (businesses, reviews, users) available through bulk download or API.
