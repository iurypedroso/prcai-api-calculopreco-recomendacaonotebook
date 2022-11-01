from Calculo_Metricas_Notebooks import ColetarMelhorPrecoNotebook
from Classes.InputUsuario import InputUsuario

def ColetarMenorPrecoNotebook(body):
    NotebookUsuario = InputUsuario(body)

    resultado = ColetarMelhorPrecoNotebook('consulta_preco', NotebookUsuario)


    return resultado