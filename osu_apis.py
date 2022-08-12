from os.path import exists

import json

import requests

class osu_api_class:
      
    def read_config(self):
        """Read in user's config.json file if exist
        """        
        if exists('config.json'):
            with open('config.json', 'r') as cfg:
                data = json.load(cfg)

            """Checking data validity

            :param k: key in dictionary data
            :param v: value in dictionary data
            """
            for k,v in data.items():
                if (k == "client_id" and v.isalnum() and len(v) > 0):
                   continue
                elif (k == "client_secret" and v.isalnum() and len(v) > 0):
                   continue
                elif (k == "grant_type" and v.isascii() and len(v) > 0):
                    continue
                elif (k == "host" and v.isascii() and len(v) > 0):
                    continue
                elif (k == "directory" and v.isascii() and len(v) > 0):
                    continue
                elif (k == "locations" and v.isascii() and len(v) > 0):
                    continue
                elif (k == "terms" and v.isascii() and len(v) > 0):
                    continue
                else:
                    print("\nInvalid data",(k,v),"found in config.json file.")
                    print("Exiting!\n")
                    exit()
              
            """Creating a dictionary using the config.file data

            :param client_id: User's client_id value
            :param client_secret: User's client_secret
            :param grant_type: This a hard-coded as "client_credentials"
            :param host_url: Host url
            :param directory_url: Directory url to be used in query
            :param location_url: Location url to be used in query
            :param terms_url: Terms url to be used in query
            :returns: Dictionary, config_dict
            """    
            config_dict = {
                    'client_id': data['client_id'],
                    'client_secret': data['client_secret'],
                    'grant_type': "client_credentials",
                    'host_url': data['host'],
                    'directory_url': data['directory'],
                    'location_url': data['locations'],
                    'terms_url': data['terms'],
            }

            return config_dict
        else:
            print("\nconfig.json file not found. Exiting!!!\n")
            exit()

    def get_access_token(self, client_id, client_secret, grant_type, host):
        """Get access token using these input parameters listed below.

        :param client_id: User's client_id value
        :type client_id: string
        :param client_secret: User's client_secret
        :type client_secret: string
        :param grant_type: Hard-coded value, "client_credentials"
        :type grant_type: string
        :param host: host url
        :type host: string
        """
       
        params = {
                    'client_id': client_id,
                    'client_secret': client_secret,
                    'grant_type': grant_type,
                  }   
        
        """Parameter values to be used as client's information to request
           for access token

        :param client_id: User's client_id value
        :type client_id: string
        :param client_secret: User's client_secret value
        :type client_secret: string
        :param grant_type: Hard-coded value, "client_credentials"
        :type grant_type: string
        :return: token, the access token
        :rtype: string
        """

        token_response = requests.post(f'{host}oauth2/token', params)
        if (token_response.status_code != 200):
            print(  
                    "\nToken response error. "+
                    "Expected status code is 200."+
                    "\nPlease review client credentials in "+
                    "config.json for valid data.\n"
                  )
            exit()
        else:
            token = token_response.json()['access_token']
            return token

    def get_headers(self,access_token):
        """Setting up headers information using input parameter, access_token

        :param access_token: Token value obtained from get_access_token function
        :type: string
        :return: Header information
        :rtype: string
        """
        return {
                    'Authorization': f'Bearer {access_token}',
                    'Content-Type': 'application/json'
                }

    def get_response(self, host, query_directory, headers, params):
        """Get response from query directory using the following input
           parameters and then returning the response data

        :param host: host url
        :type: string
        :param query_directory: query url to use
        :type: string
        :param headers: header information
        :type: json
        :param params: user's input parameters for query
        :type: string
        :return: response data value, data['data']
        :rtype: json format
        """
        
        get_query_response = requests.get(
                            f'{host}{query_directory}', 
                            headers=headers, 
                            params=params
                        )
        if (get_query_response.status_code != 200):
            print(  
                    "\nHeader response errors. "+
                    "Expected status code = 200, but got",
                    get_query_response.status_code,"."
                    "\nPlease review query directories in config.json "+
                    "for valid data.\n"
                  )
            exit()
        else:
            data = get_query_response.json()
            return data['data']

