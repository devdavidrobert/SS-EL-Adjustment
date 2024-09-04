from datetime import datetime
import requests
import pandas as pd
from log.ss_credentials import default_credential
from Data.url import dashboard_url,login_url,file_path,params_url
from Data.payload import parameters_payload

######################################################################################################
fields = {"username": f"{default_credential.username}", "password": f"{default_credential.pswd}"}

response = requests.post(login_url, data=fields)

if response.status_code == 200:
    token = response.json()['message']['login_successful']['API_token']
    
    if len(token) > 1:
        headers = {'Content-Type': 'application/json','Authorization': f'Token token={token}'}

        if len(headers) > 1:
            dashboard_reponse = requests.get(dashboard_url, headers=headers)
            
            df = pd.read_excel(file_path)
            a = 0

            for index, row in df.iterrows():
                start_time = datetime.now()

                product_imei = row['product_imei']
                new_energy_limit = row['new_energy_limit']

                search_url = params_url(product_imei)
                parameters_response = requests.post(search_url,headers=headers,json=parameters_payload)

                end_time = datetime.now()
                duration = end_time - start_time
                print(duration)
                
                print(parameters_response.json())
                a += 1
                print(f"changes energy limit of {a} units")
        else:
            print('no headers')
    else:
        print('token not found')

else:
    print('not logged in')

######################################################################################################
############################# Created by: David Robert ###############################################
######################################################################################################