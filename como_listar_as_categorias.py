# -*- encoding: utf-8 -*-


import requests


if __name__ == "__main__":
    host = "www.muambator.com.br"
    api_token = "insira-seu-token-aqui"
    r = requests.get('http://%s/api/clientes/v1/categorias/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
