import Funcoes.DistanciaEuclidiana
import json
from funcoes import calculo_media
from Classes.InputUsuario import InputUsuario
from Classes.Notebooks import NotebookResultadoPreco
from Classes.Conexao_Banco import Database
from Applications.Modulos import NotebookSimples,NotebookGamer,NotebookVisual,NotebookVGA,NotebookCPU


def ColetarMelhorPrecoNotebook(tipo_operacao, NotebookUsuario):

  BancoDadosPROD = Database()
  ResultColetaNotebooksBancoDados = BancoDadosPROD.coleta_banco_completo()

  NotebooksFiltradosTipo = ResultColetaNotebooksBancoDados.drop(ResultColetaNotebooksBancoDados.loc[ResultColetaNotebooksBancoDados[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
  
  #         =====NOTEBOOK BÁSICO=====         #
  if(NotebookUsuario.tipo_notebook == 'dia_dia' or NotebookUsuario.tipo_notebook == 'trabalho_simples' or NotebookUsuario.tipo_notebook == 'estudos_simples'): #RAM, CPU, SSD
    ResultadoNotebooksUsuario = NotebookSimples.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)

      #         =====NOTEBOOK GAMER=====         #
  elif (NotebookUsuario.tipo_notebook == 'gamer'):
    ResultadoNotebooksUsuario = NotebookGamer.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)

    #         =====NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #
  elif (NotebookUsuario.tipo_notebook == 'trabalho_visual' or NotebookUsuario.tipo_notebook == 'estudos_visual'):
    ResultadoNotebooksUsuario = NotebookVisual.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)

    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VGA=====         #
  elif (NotebookUsuario.tipo_notebook == 'trabalho_vga' or NotebookUsuario.tipo_notebook == 'estudos_vga'):
    ResultadoNotebooksUsuario = NotebookVGA.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)
    #FILTRO SO

  #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO PERSONALIZADO=====         #
  elif (NotebookUsuario.tipo_notebook == 'trabalho_cpu' or NotebookUsuario.tipo_notebook == 'trabalho'):
    ResultadoNotebooksUsuario = NotebookCPU.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)
   

  #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
  
  if tipo_operacao == 'consulta_preco':
    NotebookAvista = NotebookResultadoPreco(ResultadoNotebooksUsuario.sort_values(by='preco_avista', ascending = True).head(1))
    NotebookAprazo = NotebookResultadoPreco(ResultadoNotebooksUsuario.sort_values(by='preco_aprazo', ascending = True).head(1))

    resultadoNotebooks = {
      'MenorPreco':{
        'MaisBaratoAvista': json.loads(json.dumps(NotebookAvista.__dict__)),
        'MaisBaratoAprazo': json.loads(json.dumps(NotebookAprazo.__dict__))
        },
      'SugestaoAston': 'nenhuma'
      
    }
    return resultadoNotebooks
    
  elif tipo_operacao == 'media_valores':
    print('entrou')
    calculo_media(NotebooksFiltradosTipo)
  else:
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento])>0):
      return NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento]
    else:
      return NotebooksFiltradosTipo = NotebooksFiltradosTipo.sort_values(by=NotebookUsuario.tipo_pagamento, ascending = True).head(5)
    
