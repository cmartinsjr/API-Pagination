# python3 -m venv env
# source env/bin/activate

import requests
import json

CA_CERT = False

api_endpoint   = "https://us-east1.cloud.twistlock.com/us-1-111573456"
access_key     = "#######################"
secret_key    = "########################"

user_auth = {
    'username':access_key,
    'password':secret_key
}

#Generate a Token for access to Prisma Cloud CSWP. 
TOKEN = requests.post(api_endpoint+"/api/v1/authenticate", json=user_auth).json()['token']

#Set Prisma Cloud Headers for Login with token
auth_headers = {
    'Authorization': 'Bearer '+TOKEN,
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'Total-Count': ''
}

#Looping Defaults
limit = 10
offset = 0
response = True
more = True

while offset == 0 or more is True:
    
    payload = {
        'limit':limit,
        'offset':offset
    }

    response = requests.get(api_endpoint+"/api/v1/defenders", params=payload, headers=auth_headers, verify=CA_CERT)


    if 'Total-Count' in response.headers:
            print('Retrieving Next Page of Results: Offset/Total Count: %s/%s' % (offset, response.headers['Total-Count']))
            total_count = int(response.headers['Total-Count'])
            offset += limit
            more = bool(offset < total_count)
            for items in response.json():
                print (items['hostname'])
