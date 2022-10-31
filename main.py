from gevent import monkey
from flask import Flask, request
from gevent.pywsgi import WSGIServer
from Applications.RecomendacaoNotebook import recomendacao_notebook
from Applications.Coleta_Preco_Notebook import ColetarMenorPrecoNotebook
from Calculo_Metricas_Notebooks import coletar_preco

monkey.patch_all()
app = Flask('__name__')
app.config['JSON_AS_ASCII'] = False
app.debug = True


@app.route('/')
def welcome():
  return 'THE API IS RUNNING!'


@app.route('/prcai_recomendacao_notebooks', methods=['POST'])
def resultado():
  return recomendacao_notebook(request.json)


@app.route('/prcai_checagem_preco_notebook', methods=['POST'])
def coleta_preco():
  NotebookUsuario = InputUsuario(request.json)
  coletar_preco('consulta_preco', NotebookUsuario)
  
  # return ColetarMenorPrecoNotebook(request.json)



http_server = WSGIServer(('0.0.0.0', 8080), app)
http_server.serve_forever()
