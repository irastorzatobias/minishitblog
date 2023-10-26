import pytest
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from blog_app.models import Entrada, CustomUser, Categoria

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_categoria(db):
    return Categoria.objects.create(nombre='Test Category')

@pytest.fixture
def test_user(db):
    return CustomUser.objects.create_user(username='user', password='user')

@pytest.fixture
def another_user(db):
    return CustomUser.objects.create_user(username='another_user', password='another_user')

@pytest.fixture
def test_entrada(db, test_user):
    return Entrada.objects.create(titulo='HASBULLAH', contenido='ES UN CAPO', autor=test_user)

@pytest.fixture
def authenticated_client(api_client, test_user):
    token = Token.objects.create(user=test_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client

@pytest.fixture
def another_authenticated_client(api_client, another_user):
    token = Token.objects.create(user=another_user)
    api_client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
    return api_client

# POST
def test_entrada_create(authenticated_client, test_categoria, test_user):
    new_data = {
        'titulo': 'New Entry',
        'contenido': 'New Content',
        'autor': test_user.id,
        'categorias': [test_categoria.id]
    }
    response = authenticated_client.post('/api/entradas/', new_data, format='json')
    assert response.status_code == 201


def test_entrada_create_unauthenticated(api_client, test_categoria):
    new_data = {
        'titulo': 'New Entry',
        'contenido': 'New Content',
        'categorias': [test_categoria.id]
    }
    response = api_client.post('/api/entradas/', new_data, format='json')
    assert response.status_code == 401

# GET
def test_entrada_list(authenticated_client, test_entrada):
    response = authenticated_client.get('/api/entradas/')
    assert response.status_code == 200
    assert 'HASBULLAH' in str(response.data)

def test_entrada_list_unauthenticated(api_client):
    response = api_client.get('/api/entradas/')
    assert response.status_code == 401

# GET by ID
def test_entrada_detail(authenticated_client, test_entrada):
    response = authenticated_client.get(f'/api/entradas/{test_entrada.id}/')
    assert response.status_code == 200
    assert 'HASBULLAH' in str(response.data)

def test_entrada_detail_unauthenticated(api_client, test_entrada):
    response = api_client.get(f'/api/entradas/{test_entrada.id}/')
    assert response.status_code == 401

# DELETE
def test_entrada_delete_by_author(authenticated_client, test_entrada):
    response = authenticated_client.delete(f'/api/entradas/{test_entrada.id}/')
    assert response.status_code == 204
    assert not Entrada.objects.filter(id=test_entrada.id).exists()

def test_entrada_delete_by_non_author(another_authenticated_client, test_entrada):
    response = another_authenticated_client.delete(f'/api/entradas/{test_entrada.id}/')
    assert response.status_code == 403
    assert Entrada.objects.filter(id=test_entrada.id).exists()

# UPDATE
def test_entrada_update_by_author(authenticated_client, test_entrada, test_categoria):
    new_data = {
        'titulo': 'New Title',
        'contenido': 'New Content',
        'autor': test_entrada.autor.id,
        'categorias': [test_categoria.id]
    }
    response = authenticated_client.put(f'/api/entradas/{test_entrada.id}/', new_data, format='json')
    assert response.status_code == 200

def test_entrada_update_by_non_author(another_authenticated_client, test_entrada):
    new_data = {'titulo': 'New Title', 'contenido': 'New Content'}
    response = another_authenticated_client.put(f'/api/entradas/{test_entrada.id}/', new_data, format='json')
    assert response.status_code == 403
