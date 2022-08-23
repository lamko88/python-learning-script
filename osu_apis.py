import json
from os.path import exists

import requests


class osu_api_class:

    def read_config(self) -> dict:

        # Read in user's config.json file if exist
        if exists('config.json'):
            with open('config.json', 'r') as cfg:
                data = json.load(cfg)

            # Checking data validity pair: k (key) and v (value) existence
            require_keys = [
                'client_id', 'client_secret', 'host',
                'directory', 'locations', 'terms'
            ]
            for k, v in data.items():
                if (k in require_keys and v):
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
        client_id: str,
        client_secret: str,
        host: str
    ) -> str:

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
        access_token: str
    ) -> str:

        return {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

    def get_response(
        self,
        host: str,
        query_directory: str,
        headers: json,
        params: str
    ) -> str:

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
