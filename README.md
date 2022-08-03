
# Python-Extracting-Directory-Terms-Locations-script ![python](https://img.shields.io/badge/python-3.9.13-blue.svg)

Owner: Kok-Meng Lam  
Created: 08-01-2022  

## Files to be used: 
  - main_osuAPI_test.py
  - osuAPIs.py
  - config.json

## Configuration

The config.json file contained user's information that are required in order to receive a valid   
token to access the respective OSU API's. Here is an example of the config.json file:   

  ```json
  {
    "client_id" : "your client_id",
    "client_secret" : "your client_secret",
    "grant_type" : "client_credentials",
    "host": "https://api.oregonstate.edu/",
    "directory" : "your query directory url",
    "locations" : "your query locations url",
    "terms" : "your query terms url"
  }
  ```

  These python scripts: main_osuAPI_test.py and osuAPIs.py, can be expandable to test out other   
  OSU APIs by simply adding/modifying the function calls in main_osuAPI.py and add functions in 
  osuAPIs.py.

  **Note:**
    
    Please ensure that your config.json, main_osuAPI_test.py, and osuAPIs.py files are in the same  
    directory.  

## Usage

  1. Install dependencies via pip:

     ```shell
      $ pip3 install -r requirements.txt
     ```
     
  2. Run the script:

    ```shell
      $ python3 main_osuAPI_test.py
    ```
