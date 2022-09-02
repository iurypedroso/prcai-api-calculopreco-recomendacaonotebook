from ConsultaPrecoNotebook import notebooks_dataframe

def notebook_diario_trabalhosimples_estudosimples(tipo_notebook,pref,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela, pref_modelo,investimento,tipo_pagamento):
  #         =====INICIO NOTEBOOK BÁSICO=====         #
  if(tipo_notebook == 'dia_dia' or tipo_notebook == 'trabalho_simples' or tipo_notebook == 'estudos_simples'): #RAM, CPU, SSD
    lista_note = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]==0].index, inplace=False)
    lista_note = lista_note_tipo
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
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(lista_note.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(lista_note.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(lista_note.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(lista_note.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      correcao(menor_valor_avista,menor_valor_aprazo)
      lista_notebooks_precos.append(menor_valor_avista)
      lista_notebooks_precos.append(menor_valor_avista_str)
      lista_notebooks_precos.append(menor_valor_aprazo)
      lista_notebooks_precos.append(menor_valor_aprazo_str)
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
        lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
      else:
        lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print(lista_note)
    
      #         =====FIM NOTEBOOK BÁSICO=====         #