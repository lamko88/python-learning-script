# main function to test OSU apis:
# Directory, Location, and Terms
import json

import requests

import osu_apis

def main():
    
    # assigning an object

    c = osu_apis.osu_api_class()
    
    # retrieving config data , requesting access token, and
    # authorization headers
    
    dict = c.read_config()
 
    access_token = c.get_access_token(
                                        dict['client_id'], 
                                        dict['client_secret'], 
                                        dict['client_credentials'], 
                                        dict['host_url']
                                     )
    
    headers = c.get_headers(access_token)

    # query parameters.
    # these parameters maybe replace with other valid values
    # based on user's need.
    # for valid query parameters, please visit 
    # https://developer.oregonstate.edu/apis for more information
 
    onid = 'lamko'
    buildingAbbr = 'jsb'
    calendarYear = '2023'

    params = {
                'filter[onid]': onid,
                'q': buildingAbbr,
                'calendarYear': calendarYear,
             }

    # get directory

    print(
            "\nResponse Data for Directory:\n",
             c.get_response(
                              dict['host_url'],
                              dict['directory_url'],
                              headers=headers, 
                              params=params
                           )
         )

    # get Location

    print(
            "\nResponse Data for Location:\n", 
            c.get_response(
                              dict['host_url'],
                              dict['location_url'],
                              headers=headers, 
                              params=params
                          )
         )

    # get Terms

    print(
            "\nResponse Data for Terms:\n", 
            c.get_response(
                              dict['host_url'],
                              dict['terms_url'],
                              headers=headers, 
                              params=params
                          )
         )

if __name__ == "__main__":
    main()
