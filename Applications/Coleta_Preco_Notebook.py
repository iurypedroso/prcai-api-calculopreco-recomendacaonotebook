from Calculo_Metricas_Notebooks import coletar_preco
from Calculo_Metricas_Notebooks import lista_notebooks_precos
from Classes.InputUsuario import InputUsuario

def ColetarMenorPrecoNotebook(body):
    NotebookUsuario = InputUsuario(body)

    coletar_preco('consulta_preco', NotebookUsuario)

    dicio = {
        'avista': lista_notebooks_precos[0],
        'avista_str': lista_notebooks_precos[1],
        'aprazo': lista_notebooks_precos[2],
        'aprazo_str': lista_notebooks_precos[3],
        'id_menor_avisa': lista_notebooks_precos[4],
        'id_menor_aprazo': lista_notebooks_precos[5],
    }

    return (dicio)