
from os.path import exists

import json

import string

import requests


class osu_api_class:

    def read_config(self) -> dict:

        # Read in user's config.json file if exist
        if exists('config.json'):
            with open('config.json', 'r') as cfg:
                data = json.load(cfg)

            """Checking data validity

            :param k: key in dictionary data
            :param v: value in dictionary data
            """
            for k, v in data.items():
                if (k == 'client_id' and v.split()):
                    continue
                elif (k == 'client_secret' and v.split()):
                    continue
                elif (k == 'host' and v.split()):
                    continue
                elif (k == 'directory' and v.split()):
                    continue
                elif (k == 'locations' and v.split()):
                    continue
                elif (k == 'terms' and v.split()):
                    continue
                else:
                    print(
                        f'\nInvalid data {k, v} in config.json file. Exiting!!'
                        )
                    exit()

            config_dict = {
                'client_id': data['client_id'],
                'client_secret': data['client_secret'],
                'host_url': data['host'],
                'directory_url': data['directory'],
                'location_url': data['locations'],
                'terms_url': data['terms'],
            }
            return config_dict
        else:
            print('\nconfig.json file not found. Exiting!!!\n')
            exit()

    def get_access_token(
        self,
        client_id: string,
        client_secret: string,
        host: string
    ) -> string:

        params = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': 'client_credentials',
        }

        token_response = requests.post(f'{host}oauth2/token', params)

        status_code = token_response.status_code

        if (status_code != 200):
            print(
                f'\nError!! Expected 200 but got {status_code}.\
                \nPlease review config.json file. Exiting!!!\n'
            )
            exit()
        else:
            token = token_response.json()['access_token']
            return token

    def get_headers(
        self,
        access_token: string
    ) -> string:

        return {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

    def get_response(
        self, host: string,
        query_directory: string,
        headers: json,
        params: string
    ) -> string:

        get_query_response = requests.get(
                                f'{host}{query_directory}',
                                headers=headers,
                                params=params
                                )

        status_code = get_query_response.status_code

        if (status_code != 200):
            print(
                f'\nError!! Expected 200 but got {status_code}.\
                \nPlease review config.json file. Exiting!!!\n'
            )
            exit()
        else:
            data = get_query_response.json()

            return data['data']
