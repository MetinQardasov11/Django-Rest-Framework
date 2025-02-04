import os
import random
from pprint import pprint

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')

import django
django.setup()

from django.contrib.auth.models import User
from faker import Faker
import requests
from books.api.serializers import BookSerializer

fake = Faker(['en_US'])

def set_user():
    f_name = fake.first_name()
    l_name = fake.last_name()
    u_name = f'{f_name.lower()}_{l_name.lower()}'
    email = f'{u_name}@{fake.domain_name()}'
    print(f_name, l_name, u_name, email)
    
    user_check = User.objects.filter(username=u_name)
    
    while user_check.exists():
        u_name = u_name + str(random.randint(0, 100))
        user_check = User.objects.filter(username=u_name)
        
    user = User(
        username=u_name,
        first_name=f_name,
        last_name=l_name,
        email=email,
    )
    
    user.set_password('admin123')
    user.save()


def add_book(subject):
    url = 'https://openlibrary.org/search.json'
    payload = {'q': subject}
    response = requests.get(url, params=payload)
    
    if response.status_code != 200:
        print('Error status code:', response.status_code)
        return 
        
        
    jsn = response.json()
    books = jsn.get('docs')
    
    for book in books:
        book_name = book.get('title') 
        data = dict (
            name = book_name,
            author = book.get('author_name')[0],
            description = book.get('ia_collection_s'),
            publication_date = fake.date()
        )
        
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            print('Book saved to database: ', book_name)
        else:
            print(serializer.errors)