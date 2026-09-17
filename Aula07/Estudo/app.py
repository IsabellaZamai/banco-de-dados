import requests

url ="https://viacep.com.br/ws/01000-000/json/"

dados = requests.get(url)

resposta = dados.json()

print(f"Você mora na rua {resposta["logradouro"]}")