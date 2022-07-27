from ConexaoBDHeroku import notebooks_dataframe


lista_note= ''
lista_notebooks_precos,lista = [],[]


def selecao_notebooks(pref,tipo_notebook,pref_modelo,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,investimento,tipo_pagamento):
  global lista_note,lista, notebooks_dataframe
  lista_notebooks_precos.clear()

  
  lista_note = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0.00].index, inplace=False)
  lista_note_tipo = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]==0].index, inplace=False)

  if(tipo_notebook == 'dia_dia' or tipo_notebook == 'trabalho_simples' or tipo_notebook == 'estudos_simples'): #RAM, CPU, SSD

    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      lista_note = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        if(len(lista_note.loc[lista_note['linha']==pref_modelo])>0):
          lista_note = lista_note.loc[lista_note['linha']==pref_modelo]
        else:
          pass
      else:
        pass
    else:
      lista_note = lista_note_tipo
     #CHECA SE TEM PREFERÊNCIA DE CPU OU NÃO
    if(pref_cpu != 'n/a'):
      if (len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
        lista_note = lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
    if(pref_ram != 'n/a'):
      if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
        lista_note = lista_note.loc[lista_note['ram']==pref_ram]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
    if(pref_tela != 'n/a'):
      if(len(lista_note.loc[lista_note['tela_resolucao']==pref_tela])>0):
        lista_note = lista_note.loc[lista_note['tela_resolucao']==pref_tela]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO OU NÃO
    if(pref_armazenamento != 'n/a'):
      if(len(lista_note.loc[lista_note['ssd']>=pref_armazenamento])>0):
        lista_note = lista_note.loc[lista_note['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass
  
    if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
      lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
    else:
      lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head()
    
      #         =====FIM NOTEBOOK BÁSICO=====         #



    
      #         =====INÍCIO NOTEBOOK GAMER=====         #

  elif (tipo_notebook == 'gamer'):

    #FILTRO SO
    if (pref_so != 'n/a'):
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    else:
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith('Windows')==False].index, inplace=False)
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        lista_note = lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(pref_cpu != 'n/a'):
      if(len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
        lista_note = lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM  
    if (pref_ram != 'n/a'):
      if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
        lista_note = lista_note.loc[lista_note['ram']==pref_ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA    
    if (pref_tela != 'n/a'):
      if(len(lista_note.loc[lista_note['tela_resolucao'].str.startswith(pref_tela)==True])>0):
        lista_note = lista_note.loc[lista_note['tela_resolucao'].str.startswith(pref_tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (pref_armazenamento != 'n/a'):
      if(len(lista_note.loc[lista_note['ssd']>=pref_armazenamento])>0):
        lista_note = lista_note.loc[lista_note['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass
        
    if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
      lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
    else:
      lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head()
    
    #         =====FIM NOTEBOOK GAMER=====         #




    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #

  elif (tipo_notebook == 'trabalho_visual' or tipo_notebook == 'estudos_visual'):
    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      lista_note = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        pass
      else:
        if(len(lista_note.loc[lista_note['linha']==pref_modelo])>0):
          lista_note = lista_note.loc[lista_note['linha']==pref_modelo]
        else:
          pass
    else:
      lista_note = lista_note_tipo
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        lista_note = lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE TELA
    if(pref_tela != 'n/a'):
      if(len(lista_note.loc[lista_note['tela_resolucao']==pref_tela])>0):
        lista_note = lista_note.loc[lista_note['tela_resolucao']==pref_tela]
      else:
        pass
    else:
      pass
      #CHECA SE TEM PREFERÊNCIA DE CPU
    if(pref_cpu == 'sim' or pref_cpu == 'nao'):
      if (len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
        lista_note = lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE RAM
    if(pref_ram != 'n/a'):
      if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
        lista_note = lista_note.loc[lista_note['ram']==pref_ram]
      else:
        pass
    else:
      pass
    
    #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO
    if(pref_armazenamento != 'n/a'):
      if(len(lista_note.loc[lista_note['ssd']>=pref_armazenamento])>0):
        lista_note = lista_note.loc[lista_note['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass
  
    if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
      lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
    else:
      lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head()
      
    #         =====FIM NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #


    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VGA=====         #
  elif (tipo_notebook == 'trabalho_vga' or tipo_notebook == 'estudos_vga'):
    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      lista_note = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        pass
      else:
        if(len(lista_note.loc[lista_note['linha']==pref_modelo])>0):
          lista_note = lista_note.loc[lista_note['linha']==pref_modelo]
        else:
          pass
    else:
      lista_note = lista_note_tipo
      
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        lista_note = lista_note.loc[lista_note['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(pref_cpu != 'n/a'):
      if(len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
        lista_note = lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM
    if (pref_ram != 'n/a'):
      if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
        lista_note = lista_note.loc[lista_note['ram']==pref_ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA
    if (pref_tela != 'n/a'):
      if(len(lista_note.loc[lista_note['tela_resolucao'].str.startswith(pref_tela)==True])>0):
        lista_note = lista_note.loc[lista_note['tela_resolucao'].str.startswith(pref_tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (pref_armazenamento != 'n/a'):
      if(len(lista_note.loc[lista_note['ssd']>=pref_armazenamento])>0):
        lista_note = lista_note.loc[lista_note['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass

    if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
      lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
    else:
      lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head()
    
  #         =====FIM NOTEBOOK TRABALHO/ESTUDO VGA=====         #