from animal_adoption import app
import pytest
from flask import json

USERNAME = 'test@test.com'
PASSWORD = 'test'

def create_new_adopter(client):
    request_obj = {
        'username': USERNAME,
        'password': PASSWORD,
        'firstName': 'Bob',
        'lastName': 'Ross',
        'userType': 'adopter',
        'shelterName': '',
        'dispositions': '',
        'goodWithAnimals': True,
        'goodWithChildren': False,
        'animalLeashed': False,
        'animalPreference': 'dog',
    }

    response = client.post(
        '/create-user-with-all-details',
        data=json.dumps(request_obj),
        content_type='application/json',
    )
    return response

def create_new_shelter_worker(client):
    request_obj = {
        'username': USERNAME,
        'password': PASSWORD,
        'firstName': 'Bob',
        'lastName': 'Ross',
        'userType': 'shelter worker',
        'shelterName': 'Save a Pet',
        'dispositions': '',
        'goodWithAnimals': None,
        'goodWithChildren': None,
        'animalLeashed': None,
        'animalPreference': '',
    }

    response = client.post(
        '/create-user-with-all-details',
        data=json.dumps(request_obj),
        content_type='application/json',
    )
    return response


def test_home_route(client):        
    response = client.get('/')
    assert response.status_code == 200

def test_create_new_adopter(client):        
    response = create_new_adopter(client)
    assert response.status_code == 200

def test_login_as_adopter(client):        
    create_new_adopter(client)
    response = client.post(
        '/login',
        data=json.dumps({'username': USERNAME, 'password': PASSWORD}),
        content_type='application/json',
    )
    assert response.status_code == 200

def test_login_without_username_failed(client):        
    create_new_adopter(client)
    response = client.post(
        '/login',
        data=json.dumps({'username': None, 'password': PASSWORD}),
        content_type='application/json',
    )
    assert response.status_code == 400

def test_login_without_username_failed(client):        
    create_new_adopter(client)
    response = client.post(
        '/login',
        data=json.dumps({'username': None, 'password': PASSWORD}),
        content_type='application/json',
    )
    assert response.status_code == 400

def test_login_without_password_failed(client):        
    create_new_adopter(client)
    response = client.post(
        '/login',
        data=json.dumps({'username': USERNAME, 'password': None}),
        content_type='application/json',
    )
    assert response.status_code == 400

def test_login_with_invalid_data_failed(client):        
    create_new_adopter(client)
    with pytest.raises(ValueError):
        client.post(
            '/login',
            data=json.dumps({'username': 'badusername', 'password': 'badpassword'}),
            content_type='application/json',
    )

def test_get_adopter_user_details(client):        
    create_new_adopter(client)
    client.post(
        '/login',
        data=json.dumps({'username': USERNAME, 'password': PASSWORD}),
        content_type='application/json',
    )
    response = client.get(
        '/get-user-details',
        data=json.dumps({'username': USERNAME, 'password': PASSWORD}),
        content_type='application/json',
    )

    data = json.loads(response.data)['message']
    assert data['userType'] == 'adopter'
    assert data['username'] == USERNAME
    assert data['firstName'] == 'Bob'
    assert data['lastName'] == 'Ross'
    assert 'animalPreference' in data
    assert 'dispositions' in data
    assert response.status_code == 200

def test_create_new_shelter_worker(client):        
    response = create_new_shelter_worker(client)
    assert response.status_code == 200

def test_get_shelter_worker_details(client):        
    create_new_shelter_worker(client)
    client.post(
        '/login',
        data=json.dumps({'username': USERNAME, 'password': PASSWORD}),
        content_type='application/json',
    )
    response = client.get(
        '/get-user-details',
        data=json.dumps({'username': USERNAME, 'password': PASSWORD}),
        content_type='application/json',
    )

    data = json.loads(response.data)['message']
    assert data['userType'] == 'shelter worker'
    assert data['username'] == USERNAME
    assert data['firstName'] == 'Bob'
    assert data['lastName'] == 'Ross'
    assert 'animalPreference' not in data
    assert 'dispositions' not in data
    assert response.status_code == 200