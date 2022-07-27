from gevent import monkey
monkey.patch_all()

from flask import Flask, request
import ConsultaPrecoNotebook, Classes
from gevent.pywsgi import WSGIServer
from funcoes import filtro_inicial,menor_valor,ajuste_dataframe, lista,custo_beneficio,maior_performance
from ConsultaPrecoNotebook import lista_notebooks_precos
from Classes import Notebook
import json



app= Flask('__name__')
app.config['JSON_AS_ASCII'] = False
app.debug = True
notebook_beneficio, notebook_potente = '',''


@app.route('/')
def welcome():
  return 'THE API IS RUNNING!'
  
@app.route('/prcai_recomendacao_notebooks', methods=['POST'])
def consulta_notebook():
  global notebook_barato,notebook_beneficio, notebook_potente,notebook_barato_json,notebook_beneficio_json,notebook_potente_json

  body = request.json
  pref = (body['pref'])
  tipo_notebook = (body['tipo_notebook'])
  pref_modelo = (body['pref_modelo'])
  teste = (body['pref_ram'])
  if (teste == 'n/a'):
    pref_ram = 'n/a'
  else:
    pref_ram = int(teste)
  pref_cpu = (body['pref_cpu'])
  arma = (body['pref_armazenamento'])
  if (arma == 'n/a'):
    pref_armazenamento = 'n/a'
  else:
    pref_armazenamento = int(arma)
  pref_so = (body['pref_so'])
  pref_vga = (body['pref_vga'])
  pref_tela = (body['pref_tela'])
  
  investimento_string = float(body['investimento'])
  corrigir = '{:,.0f}'.format(float(investimento_string))
  investimento = float(corrigir.replace(',','.'))
  
  tipo_pagamento = (body['tipo_pagamento'])
  
  filtro_inicial(pref,tipo_notebook,pref_modelo,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,investimento,tipo_pagamento)

  #NOTEBOOK MAIS BARATO
  menor_valor(tipo_pagamento)
  ajuste_dataframe()
  notebook_barato = Classes.Notebook(
  lista[0],
  lista[1],
  lista[2],
  lista[3],
  lista[4],
  lista[5],
  lista[6],
  lista[7],
  lista[8],
  lista[9],
  lista[10],
  lista[11],
  lista[12],
  lista[13]
    )
  notebook_barato_json = json.loads(json.dumps(notebook_barato.__dict__))
  lista.clear()
  #NOTEBOOK CUSTO BENEFÍCIO
  custo_beneficio(tipo_pagamento)
  ajuste_dataframe()
  notebook_beneficio = Classes.Notebook(
  lista[0],
  lista[1],
  lista[2],
  lista[3],
  lista[4],
  lista[5],
  lista[6],
  lista[7],
  lista[8],
  lista[9],
  lista[10],
  lista[11],
  lista[12],
  lista[13]
    )
  notebook_beneficio_json = json.loads(json.dumps(notebook_beneficio.__dict__))
  lista.clear()

  #NOTEBOOK MELHOR PERFORMANCE
  maior_performance()
  ajuste_dataframe()
  notebook_performance = Classes.Notebook(
  lista[0],
  lista[1],
  lista[2],
  lista[3],
  lista[4],
  lista[5],
  lista[6],
  lista[7],
  lista[8],
  lista[9],
  lista[10],
  lista[11],
  lista[12],
  lista[13]
    )
  
  notebook_performance_json = json.loads(json.dumps(notebook_performance.__dict__))
  lista.clear()
  
  lista_final = {'barato':notebook_barato_json,
                 'beneficio':notebook_beneficio_json,
                 'potente':notebook_performance_json}
  
  return(lista_final)


def converter_inteiro(valor):
  if(valor != 'n/a'):
    valor = int(valor)
  else:
    valor = 'n/a'







@app.route('/prcai_checagem_preco_notebook', methods=['POST'])
def coleta_preco():
  
  body = request.json
  pref = (body['pref'])
  tipo_notebook = (body['tipo_notebook'])
  pref_modelo = (body['pref_modelo'])
  validacao_ram = (body['pref_ram'])
  if (validacao_ram == 'n/a'):
    pref_ram = 'n/a'
  else:
    pref_ram = int(validacao_ram)
  pref_cpu = (body['pref_cpu'])
  validacao_armazenamento = (body['pref_armazenamento'])
  if (validacao_armazenamento == 'n/a'):
    pref_armazenamento = 'n/a'
  else:
    pref_armazenamento = int(validacao_armazenamento)
  pref_so = (body['pref_so'])
  pref_vga = (body['pref_vga'])
  pref_tela = (body['pref_tela'])
  
  ConsultaPrecoNotebook.coletar_preco(pref,pref_ram,pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,tipo_notebook,pref_modelo)

  dicio = {'avista':lista_notebooks_precos[0],'avista_str':lista_notebooks_precos[1],'aprazo':lista_notebooks_precos[2],'aprazo_str':lista_notebooks_precos[3], 'id_menor_avisa': lista_notebooks_precos[4], 'id_menor_aprazo':lista_notebooks_precos[5]}
  #json_lista = json.dumps(dicio, indent = 1)

  return(dicio)







http_server = WSGIServer(('0.0.0.0',8080), app)
http_server.serve_forever()
# app.run(host='0.0.0.0')