
def ColetarNotebookBarato(NotebookUsuario,NotebooksFiltradosTipo):

  return NotebooksFiltradosTipo.sort_values(by=NotebookUsuario.tipo_pagamento, ascending=True).head(1)