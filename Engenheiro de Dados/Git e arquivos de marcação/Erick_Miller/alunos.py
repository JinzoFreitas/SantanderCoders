# precisa instalar o pyyaml: pip install pyyaml

import json
from pprint import pprint 

lista_importacao = {
    'alunos' : [
        {
            'nome': 'caio',
            'estado': 'RJ'
        },
         {
            'nome': 'bia',
            'estado': 'PE'
        },
         {
            'nome': 'josé',
            'estado': 'PB'
        },
         {
            'nome': 'maria',
            'estado': 'SP'
        }
    ]
}

with open('lista_alunos.json', 'w') as fp:
    json.dump(lista_importacao, fp)

pprint(lista_importacao, sort_dicts=False)    