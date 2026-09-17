import requests

cep = input("Insira o seu CEP \n ")

url = f"https://viacep.com.br/ws/{cep}/json/"


dados = requests.get(url)

resposta = dados.json()


print(f"Voce mora na rua {resposta["logradouro"]}, a rua é {resposta["bairro"]} na cidade {resposta["localidade"]}")