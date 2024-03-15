import os
import requests

api_address = 'api'  # Adresse de l'API
api_port = 8000  # Port de l'API

def run_content_test(username, password, sentence):
    r = requests.get(
        url=f'http://{api_address}:{api_port}/v1/sentiment',
        params={'username': username, 'password': password, 'sentence': sentence}
    )
    sentiment_v1 = r.json()

    r = requests.get(
        url=f'http://{api_address}:{api_port}/v2/sentiment',
        params={'username': username, 'password': password, 'sentence': sentence}
    )
    sentiment_v2 = r.json()

    output = f'''
    ============================
        Content Test
    ============================

    Test sentence: "{sentence}"

    Sentiment (v1): {sentiment_v1}
    Sentiment (v2): {sentiment_v2}
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

run_content_test('alice', 'wonderland', 'life is beautiful')
run_content_test('alice', 'wonderland', 'that sucks')
