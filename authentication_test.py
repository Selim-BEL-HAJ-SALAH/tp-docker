import os
import requests

api_address = 'api'  # Adresse de l'API
api_port = 8000  # Port de l'API

def run_authentication_test(username, password):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/permissions',
        params={'username': username, 'password': password}
    )

    try:
        output = f'''
        ============================
            Authentication Test
        ============================

        Request made at "/permissions"
        | username="{username}"
        | password="{password}"

        Expected result = 200
        Actual result = {r.status_code}

        ==>  {"SUCCESS" if r.status_code == 200 else "FAILURE"}
        '''

        print(output)

        with open('api_test.log', 'a+') as file:
            file.write(output)
            print("Log file written successfully.")
    except Exception as e:
        print("Error writing to log file:", str(e))

    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)

run_authentication_test('alice', 'wonderland')
run_authentication_test('bob', 'builder')
run_authentication_test('clementine', 'mandarine')
