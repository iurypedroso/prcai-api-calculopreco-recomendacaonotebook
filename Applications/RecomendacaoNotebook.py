import json
from Calculo_Metricas_Notebooks import ColetarMelhorPrecoNotebook
from Funcoes.Ajustar_Dataframe import ajuste_dataframe
from Funcoes.Menor_Valor import menor_valor
from Funcoes.Custo_Beneficio import custo_beneficio
from Funcoes.Maior_Performance import maior_performance
from Classes.Notebooks import Notebook

def recomendacao_notebook(body):
  
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
      if (pref_armazenamento == 1000 or pref_armazenamento == 1024):
        pref_armazenamento = 1024
      else:
        pass
    pref_so = (body['pref_so'])
    pref_vga = (body['pref_vga'])
    pref_tela = (body['pref_tela'])

    investimento = float(body['investimento'])

    tipo_pagamento = (body['tipo_pagamento'])
    if tipo_pagamento == 'avista':
        tipo_pagamento = 'preco_avista'
    else:
        tipo_pagamento = 'preco_aprazo'
    ColetarMelhorPrecoNotebook('outros', pref, pref_ram,
                                        pref_cpu, pref_vga, pref_armazenamento,
                                        pref_so, pref_tela, tipo_notebook,
                                        pref_modelo, investimento,
                                        tipo_pagamento)

    #NOTEBOOK MAIS BARATO
    lista = ajuste_dataframe(menor_valor(tipo_pagamento))

    notebook_barato = Notebook(lista[0],lista[1],lista[2],lista[3],
                                       lista[4],lista[5],lista[6],lista[7],
                                       lista[8],lista[9],lista[10],
                                       lista[11],lista[12],lista[13],
                                       lista[14],lista[15],lista[16],lista[17])
    notebook_barato_json = json.loads(json.dumps(notebook_barato.__dict__))
    lista.clear()
    #NOTEBOOK CUSTO BENEFÍCIO
    lista = ajuste_dataframe(custo_beneficio(tipo_pagamento))
    notebook_beneficio = Notebook(lista[0], lista[1], lista[2],
                                          lista[3], lista[4], lista[5],
                                          lista[6], lista[7], lista[8],
                                          lista[9], lista[10], lista[11],
                                          lista[12], lista[13], lista[14],
                                          lista[15], lista[16],lista[17])
    notebook_beneficio_json = json.loads(
        json.dumps(notebook_beneficio.__dict__))
    lista.clear()

    #NOTEBOOK MELHOR PERFORMANCE
    lista = ajuste_dataframe(maior_performance())
    notebook_performance = Notebook(lista[0], lista[1], lista[2],
                                            lista[3], lista[4], lista[5],
                                            lista[6], lista[7], lista[8],
                                            lista[9], lista[10], lista[11],
                                            lista[12], lista[13], lista[14],
                                            lista[15], lista[16],lista[17])

    notebook_performance_json = json.loads(
        json.dumps(notebook_performance.__dict__))
    lista.clear()

    lista_final = {
        'barato': notebook_barato_json,
        'beneficio': notebook_beneficio_json,
        'potente': notebook_performance_json
    }

    return (lista_final)