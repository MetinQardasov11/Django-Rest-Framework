import requests
from pprint import pprint

# {'key': '188d6701cd8356a52c7054faea60b7f997e4e763'}

def client():
    
    credentials = {
        'username': 'Metin',
        'password': '11112003Mm'
    }
    
    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/login/',
        data = credentials
    )
    
    print('status code: ', response.status_code)
    
    response_data = response.json()
    pprint(response_data)
    

if __name__ == '__main__':
    client()