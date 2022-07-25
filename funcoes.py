import json
import pandas as pd
import math
from ConexaoBDHeroku import notebooks_dataframe
notebook_barato_json,notebook_beneficio_json,notebook_potente_json = '','',''

lista_note,notebook_dado = '',''
lista = []
lista_notebooks_precos = []
menor_valor_avista,menor_valor_aprazo = 0, 0
menor_valor_avista_str,menor_valor_aprazo_str = '',''
precos_note = {}


def filtro_inicial(pref,tipo_notebook,pref_modelo,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,investimento,tipo_pagamento):
  global lista_note,lista, dataframe
  lista_notebooks_precos.clear()

  
  lista_note = dataframe.drop(dataframe.loc[dataframe['avista']==0.00].index, inplace=False)
  lista_note_tipo = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]=='não'].index, inplace=False)

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
        if(len(lista_note.loc[lista_note['linha']==pref_modelo])>0):
          lista_note = lista_note.loc[lista_note['linha']==pref_modelo]
        else:
          pass
    else:
      lista_note = lista_note_tipo
    #CHECA SE HÁ PREFERÊNCIA DE CONFIGURAÇÃO
    if (pref_so != 'MacOS'):
      #SEM PREFERÊNCIA(CONHECIMENTO POR PERGUNTAS)
      if (pref == 'não'):
        if(pref_ram != 'n/a'):
          if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
            lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
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
          if (len(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True])>0):
            lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
          else:
            pass
        else:
          pass
        #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
        if(pref_ram != 'n/a'):
          if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
            lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
          else:
            pass
        else:
          pass
        #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
        if(pref_tela != 'n/a'):
          if(len(lista_note.loc[lista_note['tela']==pref_tela])>0):
            lista_note = lista_note.loc[lista_note['tela']==pref_tela]
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
      lista_note = lista_note_tipo
      
    #COM PREFERÊNCIA(FILTRO DAS SPECS)
    if(pref == 'sim'):
      if(pref_vga != 'n/a'):
        if(len(lista_note.loc[lista_note['vga'].str.startswith(pref_vga)==True])>0):
          lista_note = lista_note.loc[lista_note['vga'].str.startswith(pref_vga)==True]
        else:
          pass
      else:
        pass
        
      if(pref_cpu != 'n/a'):
        if(len(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True])>0):
          lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
        else:
          pass
      else:
        pass
  
      if (pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
        else:
          pass
      else:
        pass
          
      if (pref_tela != 'n/a'):
        if(len(lista_note.loc[lista_note['tela'].str.startswith(pref_tela)==True])>0):
          lista_note = lista_note.loc[lista_note['tela'].str.startswith(pref_tela)==True]
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
      lista_note = lista_note

    if(len(lista_note.loc[lista_note[tipo_pagamento]<=investimento])>0):
      lista_note = lista_note.loc[lista_note[tipo_pagamento]<=investimento]
    else:
      lista_note = lista_note.sort_values(by=tipo_pagamento, ascending = True).head()
    #         =====FIM NOTEBOOK GAMER=====         #

  
def menor_valor(tipo_pagamento):
  global lista_note, notebook_dado
  lista_note = lista_note.sort_values(by=tipo_pagamento, ascending=True)
  notebook_dado = lista_note.head(1)


def custo_beneficio(tipo_pagamento):
  global lista_note, notebook_dado

  if (tipo_pagamento == 'avista'):
    lista_note = lista_note.sort_values(by='beneficio_avista', ascending=True)
  else:
    lista_note = lista_note.sort_values(by='beneficio_aprazo', ascending=True)
  
  notebook_dado = lista_note.head(1)

def maior_performance():
  global lista_note, notebook_dado
  lista_note = lista_note.sort_values(by='max_performance', ascending=False)
  notebook_dado = lista_note.head(1)


#CORRIGIR OS DADOS DO DATAFRAME E ATRIBUIR AS VARIÁVIES
def ajuste_dataframe():
  global notebook_dado,lista
  
  id = str(notebook_dado['id'])
  lista.append(str(id.split('Name')[0][5:-1].strip(" ")))
  
  marca = str(notebook_dado['marca'])
  lista.append( marca.split('Name')[0][5:-1].strip(" "))

  linha = str(notebook_dado['linha'])
  lista.append(linha.split('Name')[0][5:-1].strip(" "))

  modelo = str(notebook_dado['modelo'])
  lista.append(modelo.split('Name')[0][5:-1].strip(" "))

  memoria = str(notebook_dado['memoria'])
  lista.append(memoria.split('Name')[0][3:-1].strip(" ")+'GB')

  cpu = str(notebook_dado['cpu'])
  lista.append(cpu.split('Name')[0][5:-1].strip(" "))

  vga = str(notebook_dado['vga'])
  lista.append(vga.split('Name')[0][5:-1].strip(" ").replace('-',' '))
  
  ssd = str(notebook_dado['ssd'])
  ssd = ssd.split('Name')[0][5:-1].strip(" ")
  if (ssd == '1.0'):
    lista.append(ssd + 'TB')
  else:
    lista.append(ssd + 'GB')
    
  hd = str(notebook_dado['hd'])
  lista.append(hd.split('Name')[0][5:-3].strip(" ")+'GB')

  tela = str(notebook_dado['tela'])
  lista.append(tela.split('Name')[0][5:-1].strip(" "))

  so = str(notebook_dado['so'])
  lista.append(so.split('Name')[0][5:-1].strip(" "))

  avista = str(notebook_dado['avista'])
  a = avista.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a)*1000)
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_avista = d.replace('v','.')
  lista.append(str('R$'+note_avista))


  aprazo = str(notebook_dado['aprazo'])
  a = aprazo.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a)*1000)
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_aprazo = d.replace('v','.')
  lista.append(str('R$'+note_aprazo))

  link = str(notebook_dado['link_menor'])
  lista.append(link.split('Name')[0][5:-1].strip(" "))

  notebook_dado = ''

  
    
def consulta_preco_notebook(pref,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,tipo_notebook, pref_modelo):
  global lista_note, dataframe,menor_valor_avista,menor_valor_aprazo,menor_valor_avista_str,menor_valor_aprazo_str, lista_notebooks_precos, precos_note

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
  
  lista_note = dataframe.drop(dataframe.loc[dataframe['avista']==0.00].index, inplace=False)
  lista_note_tipo = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]=='não'].index, inplace=False)
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
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
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
        if (len(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True])>0):
          lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
        else:
          pass
      else:
        pass
      #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
      if(pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
        else:
          pass
      else:
        pass
      #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
      if(pref_tela != 'n/a'):
        if(len(lista_note.loc[lista_note['tela']==pref_tela])>0):
          lista_note = lista_note.loc[lista_note['tela']==pref_tela]
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
        if(len(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True])>0):
          lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
        else:
          pass
      else:
        pass
  
      if (pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
        else:
          pass
      else:
        pass
          
      if (pref_tela != 'n/a'):
        if(len(lista_note.loc[lista_note['tela'].str.startswith(pref_tela)==True])>0):
          lista_note = lista_note.loc[lista_note['tela'].str.startswith(pref_tela)==True]
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
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
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
        if (len(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True])>0):
          lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
        else:
          pass
      else:
        pass
      #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
      if(pref_ram != 'n/a'):
        if(len(lista_note.loc[lista_note['memoria']==pref_ram])>0):
          lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
        else:
          pass
      else:
        pass
      #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
      if(pref_tela != 'n/a'):
        if(len(lista_note.loc[lista_note['tela']==pref_tela])>0):
          lista_note = lista_note.loc[lista_note['tela']==pref_tela]
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
  
  




  
  # if (pref_cpu != 'n/a' and pref_ram != 'n/a'):
  #   lista_note = lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True]
  #   lista_note = lista_note.loc[lista_note['memoria']==pref_ram]
  #   if (len(lista_note) == 0):
  #     lista_note = dataframe.drop(dataframe.loc[dataframe['avista']==0.00].index, inplace=False)
  #     lista_note = lista_note.drop(lista_note.loc[lista_note[tipo_notebook]=='não'].index, inplace=False)
  #     menor_valor_avista = str(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True].sort_values(by='avista', ascending = True).head(1)['avista'])
  #     menor_valor_aprazo = str(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True].sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
  #     correcao(menor_valor_avista,menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_avista)
  #     lista_notebooks_precos.append(menor_valor_avista_str)
  #     lista_notebooks_precos.append(menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_aprazo_str)
  #   else:
  #     menor_valor_avista = str(lista_note.sort_values(by='avista', ascending = True).head(1)['avista'])
  #     menor_valor_aprazo = str(lista_note.sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
  #     correcao(menor_valor_avista,menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_avista)
  #     lista_notebooks_precos.append(menor_valor_avista_str)
  #     lista_notebooks_precos.append(menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_aprazo_str)
  # elif (pref_cpu != 'n/a' and pref_ram == 'n/a'):
  #   menor_valor_avista = str(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True].sort_values(by='avista', ascending = True).head(1)['avista'])
  #   menor_valor_aprazo = str(lista_note.loc[lista_note['cpu'].str.startswith(pref_cpu)==True].sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
  #   correcao(menor_valor_avista,menor_valor_aprazo)
  #   lista_notebooks_precos.append(menor_valor_avista)
  #   lista_notebooks_precos.append(menor_valor_avista_str)
  #   lista_notebooks_precos.append(menor_valor_aprazo)
  #   lista_notebooks_precos.append(menor_valor_aprazo_str)
  # elif (pref_cpu == 'n/a' and pref_ram != 'n/a'):
  #   menor_valor_avista = str(lista_note.loc[lista_note['memoria']==pref_ram].sort_values(by='avista', ascending = True).head(1)['avista'])
  #   menor_valor_aprazo = str(lista_note.loc[lista_note['memoria']==pref_ram].sort_values(by='aprazo', ascending = True).head(1)['aprazo'])
  #   correcao(menor_valor_avista,menor_valor_aprazo)
  #   lista_notebooks_precos.append(menor_valor_avista)
  #   lista_notebooks_precos.append(menor_valor_avista_str)
  #   lista_notebooks_precos.append(menor_valor_aprazo)
  #   lista_notebooks_precos.append(menor_valor_aprazo_str)
  # else:
  #     menor_valor_avista = dataframe.drop(dataframe.loc[dataframe['avista']==0.00].index, inplace=False).sort_values(by='avista', ascending = True)
  #     menor_valor_avista = str(menor_valor_avista.head(1)['avista'])
  #     menor_valor_aprazo = dataframe.drop(dataframe.loc[dataframe['avista']==0.00].index, inplace=False).sort_values(by='aprazo', ascending = True)
  #     menor_valor_aprazo = str(menor_valor_aprazo.head(1)['aprazo'])
  #     correcao(menor_valor_avista,menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_avista)
  #     lista_notebooks_precos.append(menor_valor_avista_str)
  #     lista_notebooks_precos.append(menor_valor_aprazo)
  #     lista_notebooks_precos.append(menor_valor_aprazo_str)
  





  
