# -*- encoding: utf-8 -*-


import requests


if __name__ == "__main__":
    host = "www.muambator.com.br"
    api_token = "insira-seu-token-aqui"
    q = "aliexpress"
    r = requests.get('http://%s/api/clientes/v1/pacotes/?q=%s&api-token=%s' % (host, q, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
