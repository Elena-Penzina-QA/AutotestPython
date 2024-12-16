import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = 'f540709e88bf83cdf7797dd9cccf6526'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': Token}
Body_create = {"name": "Чери", "photo_id": 1}

def test_status_code_get_trainers(): #Список тренеров
    response_list = requests.get(url = f'{URL}/trainers')
    assert response_list.status_code == 200

def test_status_code_get_mytrainers():#Проверка, что мой тренер есть в списке
    response_list = requests.get(url = f'{URL}/trainers', params = {'trainer_id': 12339})
    assert response_list.json()['data'][0]['id'] == '12339'

def test_status_code_create_pokemon(): #Создание покемона
    global response_create
    response_create = requests.post(url = f'{URL}/pokemons', json = Body_create, headers = HEADERS)
    assert  response_create.status_code == 201

@pytest.fixture()
def f_list_mypokemon():
    list_mypokemon = requests.get(url = f'{URL}/pokemons', params = {'trainer_id': 12339, 'in_pokeball': 0, 'status': 1})
    return list_mypokemon.json()['data'][0]['id']

def test_status_code_create_catch(f_list_mypokemon): #Поймать покемона в покеболл
    Body_catch = { "pokemon_id": f_list_mypokemon}
    response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', json = Body_catch, headers = HEADERS)
    assert  response_catch.status_code == 200

@pytest.fixture()
def f_list_in_pokebol():
    in_pokebol = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball': 1}) #Список покемонов в покеболе
    return in_pokebol.json()['data'][6]['id']

@pytest.fixture()
def f_list_in_pokebol_mytrainer():
    in_pokebol_mytrainer = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball': 1, 'trainer_id': 12339}) #Список моих покемонов в покеболе
    return in_pokebol_mytrainer.json()['data'][0]['id']

def test_status_code_battle(f_list_in_pokebol, f_list_in_pokebol_mytrainer): #Битва покемонов
    Body_battle = { "attacking_pokemon": f_list_in_pokebol_mytrainer, "defending_pokemon": f_list_in_pokebol}
    response_create = requests.post(url = f'{URL}/battle', json = Body_battle, headers = HEADERS)
    assert  response_create.status_code == 200
