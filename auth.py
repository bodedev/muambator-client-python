# -*- coding: utf-8 -*-

u"""
Todas nossas requisições precisam de autenticação através de uma chave de acesso (token).
Na nossa API aceitamos que ela seja passada tanto pelo header HTTP ou por parâmetro de query da URL.
Abaixo temos um exemplo para cada caso na nossa chamada de status do sistema.
"""

import requests

url = 'http://www.muambator.com.br/api/clientes/v1/'

# Chamada utilizando autenticação por query parameter
querystring = {'api-token': 'SUA-TOKEN-AQUI'}
response = requests.request("GET", url, params=querystring)
print(response.text)

# Chamada utilizando autenticação por header HTTP
headers = {'api-token': 'SUA-TOKEN-AQUI'}
response = requests.request("GET", url, headers=headers)
print(response.text)
