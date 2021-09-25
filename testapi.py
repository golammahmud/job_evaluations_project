import requests
import json

User_Based_Inputs_URL = "http://127.0.0.1:8000/api/user-based-inputs/"
All_Inputs_URL ="http://127.0.0.1:8000/api/all-userinputs/"

#get all the data from the given url using jwt token
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-type':'application/json'}
    headers['Authorization']="Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM3NzQ2NTU2LCJqdGkiOiI5NmQ1NzY2NzRmZGM0ZjEwYWI3ZjI0MmMzNDM3MDUxYyIsInVzZXJfaWQiOjF9.L19n4koaIlttlYL1LC4SBbxXVt6_TLk0xFNfksV-HIo"
    response = requests.get(url=User_Based_Inputs_URL,headers=headers,data=json_data)
    data = response.json()
    print(data)
get_data()




