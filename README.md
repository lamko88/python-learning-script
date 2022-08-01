# Python-Extracting-Directory-Terms-Locations-script
# Owner: Kok-Meng Lam
# Created: 08-01-2022
# Version: Python 3.9.13

Files to be used: main_osuAPI_test.py, osuAPIs.py, config.json

The config.json file contained user's information that are required in order to receive a valid 
token to access the respective API's. Here is a template of the config.json file:

{
  2   "client_id" : "<client_id value>",
  3   "client_secret" : "<client_secret value>",
  4   "grant_type" : "client_credentials",
  5   "host": "https://api.oregonstate.edu/",
  6   "directory" : "<directory url>",
  7   "locations" : "<locations url>",
  8   "terms" : "<terms url>"
  9 }

  These python scripts: main_osuAPI_test.py and osuAPIs.py, can be expandable to test out other 
  APIs by simply adding/modifying the function calls in main_osuAPI.py and add functions in 
  osuAPIs.py.
