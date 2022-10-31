def ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario):
  #FILTRO SO
  if (NotebookUsuario.so != 'MacOS' and NotebookUsuario.so != 'n/a'):
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.drop(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['so'].str.startswith(NotebookUsuario.so)==False].index, inplace=False)
  elif (NotebookUsuario.so == 'MacOS'):
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['marca']=='Apple']
    if (NotebookUsuario.pref_modelo != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['linha']==NotebookUsuario.pref_modelo])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['linha']==NotebookUsuario.pref_modelo]
      else:
        pass
    else:
      pass
  else:
    pass
    #CHECA SE TEM PREFERÊNCIA DE CPU OU NÃO
  if(NotebookUsuario.cpu != 'n/a'):
    if (len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True]
    else:
      pass 
  else:
    pass
  #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
  if(NotebookUsuario.ram != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram]
    else:
      pass
  else:
    pass
  #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
  if(NotebookUsuario.tela != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']==NotebookUsuario.tela])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']==NotebookUsuario.tela]
    else:
      pass
  else:
    pass
  #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO OU NÃO
  if(NotebookUsuario.armazenamento != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento]
    else:
      pass
  else:
    pass
    
  return NotebooksFiltradosTipo

