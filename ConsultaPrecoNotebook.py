from ConexaoBDHeroku import notebooks_dataframe

lista,lista_notebooks_precos,precos_note = [],[],{}
menor_valor_avista,menor_valor_aprazo = 0, 0
menor_valor_avista_str,menor_valor_aprazo_str,lista_note,notebook_dado = '','','',''


def coletar_preco(pref,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,tipo_notebook, pref_modelo):
  
  global lista_note, notebooks_dataframe,menor_valor_avista,menor_valor_aprazo,menor_valor_avista_str,menor_valor_aprazo_str, lista_notebooks_precos, precos_note

  def correcao(valor_avista, valor_aprazo):
    global menor_valor_avista,menor_valor_aprazo,menor_valor_avista_str,menor_valor_aprazo_str
    a = valor_avista.split('Name')[0][5:-1].strip(" ")
    b = '{:,.2f}'.format(float(a)*1000)
    c = b.replace(',','v')
    d = c.replace('.',',')
    e = d.replace('v','.')
    x = e.split(',')[0]
    x = x.replace('.','')
    menor_valor_avista = int(x)
    menor_valor_avista_str = (str('R$'+e))

    f = valor_aprazo.split('Name')[0][5:-1].strip(" ")
    g = '{:,.2f}'.format(float(f)*1000)
    h = g.replace(',','v')
    i = h.replace('.',',')
    j = i.replace('v','.')
    u = j.split(',')[0]
    u = u.replace('.','')
    menor_valor_aprazo = int(u)
    menor_valor_aprazo_str = (str('R$'+j))
    
  lista_notebooks_precos.clear()
  
  lista_note = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
  lista_note_tipo = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]==0].index, inplace=False)
  lista_note = lista_note_tipo

  #         =====INICIO NOTEBOOK BÁSICO=====         #
  if(tipo_notebook == 'dia_dia' or tipo_notebook == 'trabalho_simples' or tipo_notebook == 'estudo_simples'): #RAM, CPU, SSD

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
    #CHECA SE HÁ PREFERÊNCIA DE CONFIGURAÇÃO

    #SEM PREFERÊNCIA(CONHECIMENTO POR PERGUNTAS)
    if (pref == 'não'):
      if(pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['ram']==pref_ram]
        else:
          pass
      else:
        pass
      if(pref_armazenamento != 'n/a'):
        if(len(lista_note.loc[lista_note['ssd']>=256])>0):
          lista_note = lista_note.loc[lista_note['ssd']>=256]
      else:
          pass
    #COM PREFERÊNCIA(FILTRO DAS SPECS)
    else:
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
        if(len(lista_note.loc[lista_note['resolucao_tela']==pref_tela])>0):
          lista_note = lista_note.loc[lista_note['resolucao_tela']==pref_tela]
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
  
      
    menor_valor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['avista'])
    menor_valor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
    id_menor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['id'])
    id_menor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['id'])
    
    correcao(menor_valor_avista,menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_avista)
    lista_notebooks_precos.append(menor_valor_avista_str)
    lista_notebooks_precos.append(menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_aprazo_str)
    lista_notebooks_precos.append(id_menor_avista)
    lista_notebooks_precos.append(id_menor_aprazo)
    
      #         =====FIM NOTEBOOK BÁSICO=====         #



    
      #         =====INÍCIO NOTEBOOK GAMER=====         #

  elif (tipo_notebook == 'gamer'):

        #FILTRO SO
    if (pref_so != 'n/a'):
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    else:
      lista_note = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith('Windows')==False].index, inplace=False)
      
    #COM PREFERÊNCIA(FILTRO DAS SPECS)
    if(pref == 'sim' or pref == 'não'):
      if(pref_vga != 'n/a'):
        if(len(lista_note.loc[lista_note['vga'].str.startswith(pref_vga)==True])>0):
          lista_note = lista_note.loc[lista_note['vga'].str.startswith(pref_vga)==True]
        else:
          pass
      else:
        pass
        
      if(pref_cpu != 'n/a'):
        if(len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
          lista_note = lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True]
        else:
          pass
      else:
        pass
  
      if (pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['ram']==pref_ram]
        else:
          pass
      else:
        pass
          
      if (pref_tela != 'n/a'):
        if(len(lista_note.loc[lista_note['resolucao_tela'].str.startswith(pref_tela)==True])>0):
          lista_note = lista_note.loc[lista_note['resolucao_tela'].str.startswith(pref_tela)==True]
        else:
          pass
      else:
        pass
  
      if (pref_armazenamento != 'n/a'):
        if(len(lista_note.loc[lista_note['ssd']>=pref_armazenamento])>0):
          lista_note = lista_note.loc[lista_note['ssd']>=pref_armazenamento]
        else:
          pass
      else:
        pass
    else:
      pass

    menor_valor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['avista'])
    menor_valor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
    id_menor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['id'])
    id_menor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['id'])
    
    correcao(menor_valor_avista,menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_avista)
    lista_notebooks_precos.append(menor_valor_avista_str)
    lista_notebooks_precos.append(menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_aprazo_str)
    lista_notebooks_precos.append(id_menor_avista)
    lista_notebooks_precos.append(id_menor_aprazo)


    
    #         =====FIM NOTEBOOK GAMER=====         #




    #         =====INÍCIO NOTEBOOK TRABALHO VISUAL=====         #

  elif (tipo_notebook == 'trabalho_visual'):
    #Tela IPS, SRGB acima de 90, Dell Inspiron, Avell
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
    #CHECA SE HÁ PREFERÊNCIA DE CONFIGURAÇÃO

    #SEM PREFERÊNCIA(CONHECIMENTO POR PERGUNTAS)
    if (pref == 'não'):
      if(pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['ram']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['ram']==pref_ram]
        else:
          pass
      else:
        pass
      if(pref_armazenamento != 'n/a'):
        if(len(lista_note.loc[lista_note['ssd']>=256])>0):
          lista_note = lista_note.loc[lista_note['ssd']>=256]
      else:
          pass
    #COM PREFERÊNCIA(FILTRO DAS SPECS)
    else:
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
        if(len(lista_note.loc[lista_note['resolucao_tela']==pref_tela])>0):
          lista_note = lista_note.loc[lista_note['resolucao_tela']==pref_tela]
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
  
      
    menor_valor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['avista'])
    menor_valor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
    id_menor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['id'])
    id_menor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['id'])
    
    correcao(menor_valor_avista,menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_avista)
    lista_notebooks_precos.append(menor_valor_avista_str)
    lista_notebooks_precos.append(menor_valor_aprazo)
    lista_notebooks_precos.append(menor_valor_aprazo_str)
    lista_notebooks_precos.append(id_menor_avista)
    lista_notebooks_precos.append(id_menor_aprazo)


    #         =====FIM NOTEBOOK TRABALHO VISUAL=====         #

  
  elif (tipo_notebook == 'trabalho_vga'):
    pass

  elif (tipo_notebook == 'estudos_vga'):
    pass

  elif (tipo_notebook == 'estudos_visual'):
      pass