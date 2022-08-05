# class for OSU APIs common functions:
# read_config, access_token, headers
#
import json

import requests

class osu_api_class:
    
    # def access_token(self):
    
    def read_config(self):
    
    # read config.json
    
        with open('config.json', 'r') as cfg:
            data = json.load(cfg)

    # creating a dictionary for config data

        dict = {
                    'client_id': data['client_id'],
                    'client_secret': data['client_secret'],
                    'client_credentials': "client_credentials",
                    'host_url': data['host'],
                    'directory_url': data['directory'],
                    'location_url': data['locations'],
                    'terms_url': data['terms'],
                }

        return dict

    def get_access_token(self, cid, csec, gtype, host):
       
        # setting up params 
       
        params = {
                    'client_id': cid,
                    'client_secret': csec,
                    'grant_type': gtype,
                  }   

        # requesting token
        
        token_response = requests.post(f'{host}oauth2/token', params)
        token_response.raise_for_status()
        token = token_response.json()['access_token']

        return token

    def get_headers(self,access_token):
        
        return {
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'
                }

    def get_response(self, host, query, headers, params):

        r = requests.get(
                            f'{host}{query}', 
                            headers=headers, 
                            params=params
                        )
        r.raise_for_status()
        data = r.json()

        return data['data']

