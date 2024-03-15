import os
import requests

api_address = 'api'  # Adresse de l'API
api_port = 8000  # Port de l'API

def run_authorization_test(username, password, model_version):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v{model_version}/sentiment',
        params={'username': username, 'password': password, 'sentence': 'Test sentence'}
    )

    output = f'''
    ============================
        Authorization Test
    ============================

    Request made at "/v{model_version}/sentiment"
    | username="{username}"
    | password="{password}"
    | model_version="{model_version}"

    Expected result = 200
    Actual result = {r.status_code}

    ==>  {"SUCCESS" if r.status_code == 200 else "FAILURE"}
    '''

    print(output)

    try:
        with open('api_test.log', 'a') as file:
            file.write(output)
            print("Log file written successfully.")
    except Exception as e:
        print("Error writing to log file:", str(e))

    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output)

run_authorization_test('alice', 'wonderland', 1)
run_authorization_test('alice', 'wonderland', 2)
run_authorization_test('bob', 'builder', 1)
run_authorization_test('bob', 'builder', 2)
