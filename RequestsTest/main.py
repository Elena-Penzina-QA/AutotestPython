import requests
URL = 'https://api.pokemonbattle.ru/v2'
Token = 'f540709e88bf83cdf7797dd9cccf6526'
HEADERS = {'Content-Type': 'application/json', 'trainer_token': Token}
Body_create = {"name": "Чери", "photo_id": 1}


response_create = requests.post(url = f'{URL}/pokemons', json = Body_create, headers = HEADERS)
print(response_create.text)

Body_change = {"pokemon_id": response_create.json()['id'], "name": "Poni", "photo_id": 2}
response_change = requests.put(url = f'{URL}/pokemons', json = Body_change, headers = HEADERS)
print(response_change.text)

Body_catch = { "pokemon_id": response_create.json()['id']}
response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', json = Body_catch, headers = HEADERS)
print(response_catch.text)

response_list = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball': 1})
response_list_mytrainer = requests.get(url = f'{URL}/pokemons', params = {'in_pokeball': 1, 'trainer_id': 12339})


Body_battle = { "attacking_pokemon": response_list_mytrainer.json()['data'][0]['id'], "defending_pokemon": response_list.json()['data'][6]['id']}
response_create = requests.post(url = f'{URL}/battle', json = Body_battle, headers = HEADERS)
print(response_create.text)
