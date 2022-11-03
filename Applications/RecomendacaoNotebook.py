import json
from Calculo_Metricas_Notebooks import ColetarMelhorPrecoNotebook
from Funcoes.Ajustar_Dataframe import ajuste_dataframe
from Classes.Notebooks import Notebook
from Classes.InputUsuario import InputUsuario

def recomendacao_notebook(body):
  #Cria um objeto com as especificaçoes e tipo de pagamento e valor que deseja investir
    NotebookUsuario = InputUsuario(body)
    NotebookUsuario.SetInvestimento(body['investimento'])
    NotebookUsuario.SetTipoPagamento(body['tipo_pagamento'])

    #Chama a função que recebe as especificações e filtra a base de dados, retornando o resultado. Se o investimento for abaixo, pega as 5 primeiras máquinas mais baratas.
    ListaResultadoNotebooksUsuario = ColetarMelhorPrecoNotebook('recomendacao_notebook', NotebookUsuario)

    #VOU PRECISAR COLETAR O ID DO NOTEBOOK QUE O USUÁRIO DESEJA. À PARTIR DO ID SERÁ POSSÍVEL VERIFICAR

    #Cria o objeto de notebook BARATO à vista e parcelado separadamente para terem seus links e lojas de forma organizada.
    NotebookBaratoAvista = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='preco_avista', ascending=True).head(1))
    NotebookBaratoAprazo = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='preco_aprazo', ascending=True).head(1))

    #Cria o objeto de notebook BENEFICIO à vista e parcelado separadamente para terem seus links e lojas de forma organizada.
    NotebookBeneficioAvista = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='beneficio_avista', ascending=True).head(1))
    NotebookBeneficioAprazo = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='beneficio_aprazo', ascending=True).head(1))

    #Cria o objeto de notebook POTENTE à vista e parcelado separadamente para terem seus links e lojas de forma organizada.
    NotebookPotenteAvista = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='beneficio_avista', ascending=True).head(1))
    NotebookPotenteAprazo = NotebookRecomendacao(ListaResultadoNotebooksUsuario.sort_values(by='beneficio_aprazo', ascending=True).head(1))
  
    #NOTEBOOK MAIS BARATO

    lista_final = {
        'barato': notebook_barato_json,
        'beneficio': notebook_beneficio_json,
        'potente': notebook_performance_json
    }

    return (lista_final)