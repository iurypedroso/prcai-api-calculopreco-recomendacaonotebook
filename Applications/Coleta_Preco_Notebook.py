from Calculo_Metricas_Notebooks import coletar_preco
from Calculo_Metricas_Notebooks import lista_notebooks_precos
from Classes.InputUsuario import InputUsuario

def ColetarMenorPrecoNotebook(body):
    NotebookUsuario = InputUsuario(body)
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

    coletar_preco('consulta_preco', pref, pref_ram,
                                        pref_cpu, pref_vga, pref_armazenamento,
                                        pref_so, pref_tela, tipo_notebook,
                                        pref_modelo, 'sem_investimento',
                                        'sem_tipo_pagamento')

    dicio = {
        'avista': lista_notebooks_precos[0],
        'avista_str': lista_notebooks_precos[1],
        'aprazo': lista_notebooks_precos[2],
        'aprazo_str': lista_notebooks_precos[3],
        'id_menor_avisa': lista_notebooks_precos[4],
        'id_menor_aprazo': lista_notebooks_precos[5],
    }

    return (dicio)