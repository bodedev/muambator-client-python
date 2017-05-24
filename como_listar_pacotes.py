# -*- encoding: utf-8 -*-


import requests


if __name__ == "__main__":
    host = "www.muambator.com.br"
    api_token = "insira-seu-token-aqui"
    r = requests.get('http://%s/api/clientes/v1/pacotes/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
    r = requests.get('http://%s/api/clientes/v1/pacotes/pendentes/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
    r = requests.get('http://%s/api/clientes/v1/pacotes/entregues/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
    r = requests.get('http://%s/api/clientes/v1/pacotes/tributados/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
    r = requests.get('http://%s/api/clientes/v1/pacotes/atrasados/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
    r = requests.get('http://%s/api/clientes/v1/pacotes/arquivados/?api-token=%s' % (host, api_token), headers={"Content-type": "application/json"})
    print r.status_code
    print r.text
