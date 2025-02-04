import requests
from pprint import pprint

# {'key': '821eec18162c1bfbc1990f4ffe0409b9059610be'}

def client():
    
    credentials = {
        'username': 'Omer',
        'email': 'omer.osmanov11@gmail.com',
        'password1': '11112003Oo',
        'password2': '11112003Oo',
    }
    
    response = requests.post(
        url = 'http://127.0.0.1:8000/api/rest-auth/registration/',
        data = credentials
    )
    
    print('status code: ', response.status_code)
    
    response_data = response.json()
    pprint(response_data)

if __name__ == '__main__':
    client()