# class for OSU APIs common functions:
# read_config, access_token, headers
#
import json
import requests

class osuAPIClass:
    # def access_token(self):
    def read_config(self):
    # read config.json
        with open('config.json', 'r') as cfg:
            data = json.load(cfg)

    # get credentials
        cid = data['client_id']
        csec = data['client_secret']
        gtype = "client_credentials" 

    # get host, dir, loc, and term
        host = data['host']
        dir = data['directory']
        loc = data['locations']
        term = data['terms']

        return [cid, csec, gtype, host, dir, loc, term]

    def access_token(self, cid, csec, gtype, host):
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
        # print(token)
        return token

    def get_headers(self,access_token):
        return {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }


