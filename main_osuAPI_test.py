# main function to test OSU APIs:
# Directory, Location, and Terms
#
import json
import requests
import osuAPIs

def main():
    c = osuAPIs.osuAPIClass()
    # retrieving config data
    cfg = c.read_config()
    # list mapping
    # cid = cfg[0]; csec = cfg[1]; gtype = cfg[2]; host = cfg[3]; 
    # dir = cfg[4]; loc = cfg[5]; term = cfg[6]
    access_token = c.access_token(cfg[0], cfg[1], cfg[2], cfg[3])
    heads = c.headers(access_token)

    # query parameters
    onid = 'lamko'
    buildingAbbr = 'jsb'
    calendarYear = '2023'

    params = {
        'filter[onid]': onid,
        'q': buildingAbbr,
        'calendarYear': calendarYear,
    }
    
    # get directory
    r = requests.get(f'{cfg[3]}{cfg[4]}', headers=heads, params=params)
    r.raise_for_status()
    data = r.json()
    response_data = data['data']
    print("\nResponse Data for Directory:\n", response_data)

    # get Location
    r = requests.get(f'{cfg[3]}{cfg[5]}', headers=heads, params=params)
    r.raise_for_status()
    data = r.json()
    response_data = data['data']
    print("\nResponse Data for Location:\n", response_data)

    # get Terms
    r = requests.get(f'{cfg[3]}{cfg[6]}', headers=heads, params=params)
    r.raise_for_status()
    data = r.json()
    response_data = data['data']
    print("\nResponse Data for Terms:\n", response_data)


if __name__ == "__main__":
    main()