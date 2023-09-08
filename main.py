from secret import DB_PATH_URL
import requests
import json

link = DB_PATH_URL

dados = {
    'nome': 'Mouse Gamer Logitech G203 LIGHTSYNC RGB',
    'preco': 159.00,
    'quantidade': 115
}


class Requisicoes:
    def __init__(self, db_path: str):
        self.DB_PATH = db_path

    def get(self, path: str):
        req = requests.get(f'{self.DB_PATH}/{path}/.json')
        print(req)
        print(req.json())

    def post(self, path: str, data: dict):
        req = requests.post(
            f'{self.DB_PATH}/{path}/.json', data=json.dumps(data)
        )
        print(req)
        print(req.text)

    def patch(self, path: str, data: dict):
        req = requests.patch(
            f'{self.DB_PATH}/{path}/.json', data=json.dumps(data)
        )
        print(req)
        print(req.text)

    def delete(self, path: str):
        req = requests.delete(f'{self.DB_PATH}/{path}/.json')
        print(req)
        print(req.text)


reqs = Requisicoes(link)
reqs.post('/Produtos', dados)
