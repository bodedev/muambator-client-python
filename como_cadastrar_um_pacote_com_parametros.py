# -*- encoding: utf-8 -*-


import requests


if __name__ == "__main__":
    host = "www.muambator.com.br"
    api_token = "insira-seu-token-aqui"
    codigo_pacote = "PL970650197BR"
    parametros = {
        "nome": "Meu Fogãozinho <3",
        "tags": ["acampamento", "jetcook"],
        "categoria": "camping"
    }
    r = requests.post('http://%s/api/clientes/v1/pacotes/%s/?api-token=%s' % (host, codigo_pacote, api_token), json=parametros, headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
