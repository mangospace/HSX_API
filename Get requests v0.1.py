"""Building using HSX API"""
import requests
import json
import pandas as pd

#[ Base URL: api.hsx.io/patient ]
# https://marketstreet-website.s3.amazonaws.com/sandbox/sandbox-patient-api-sandbox-swagger.json
#curl -X GET "https://api.hsx.io/patient/patients" -H "accept: application/json"


folder=r"F:\HSX\HSX.txt"

with open(folder) as f:
    lines = f.readlines()
api_key= lines[0]


url="https://api.hsx.io/patient/patients"
headers = {
    "accept": "application/json",
    "x-api-key": api_key,
}

params = {
    "state": "NJ",
}

resp = requests.get(url, params=params, headers=headers)


print(resp.status_code)
print(resp.json())
type(resp.json()[0])
atom1=json.dumps(resp.json()[0])
type(atom1)
json_object = json.loads(atom1)
type(json_object)

atom2=json.dumps(json_object)
type(json_object[0])
atom3=json_object[0]




