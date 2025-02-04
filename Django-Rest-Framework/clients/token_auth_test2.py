import requests
from pprint import pprint

# {'key': '188d6701cd8356a52c7054faea60b7f997e4e763'}
# {'key': '821eec18162c1bfbc1990f4ffe0409b9059610be'}

def client():
    
    token = 'Token 821eec18162c1bfbc1990f4ffe0409b9059610be'
    
    headers = {
        'Authorization': token
    }
    
    response = requests.get(
        url = 'http://127.0.0.1:8000/api/profiles/',
        headers = headers,
    )
    
    print('status code: ', response.status_code)
    
    response_data = response.json()
    pprint(response_data)
    

if __name__ == '__main__':
    client()