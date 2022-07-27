import json
import pandas as pd
import math
from ConexaoBDHeroku import notebooks_dataframe
notebook_barato_json,notebook_beneficio_json,notebook_potente_json = '','',''
from ConsultaPrecoNotebook import lista_note
import ConsultaPrecoNotebook

notebook_dado = '',''
lista = []
lista_notebooks_precos = []
menor_valor_avista,menor_valor_aprazo = 0, 0
menor_valor_avista_str,menor_valor_aprazo_str = '',''
precos_note = {}


#COLETA O NOTEBOOK MAIS BARATO
def menor_valor(tipo_pagamento):
  global lista_note, notebook_dado
  print(lista_note)
  lista_note = lista_note.sort_values(by=tipo_pagamento, ascending=True)
  notebook_dado = lista_note.head(1)

#COLETA O NOTEBOOK COM O MELHOR CUSTOxBENEFICIO
def custo_beneficio(tipo_pagamento):
  global lista_note, notebook_dado

  if (tipo_pagamento == 'preco_avista'):
    lista_note = lista_note.sort_values(by='beneficio_avista', ascending=True)
  else:
    lista_note = lista_note.sort_values(by='beneficio_aprazo', ascending=True)
  
  notebook_dado = lista_note.head(1)

#COLETA O NOTEBOOK COM O MELHOR DESEMPENHO
def maior_performance():
  global lista_note, notebook_dado
  lista_note = lista_note.sort_values(by='performance', ascending=False)
  notebook_dado = lista_note.head(1)


#CORRIGIR OS DADOS DO DATAFRAME E ATRIBUIR AS VARIÁVIES
def ajuste_dataframe():
  global notebook_dado,lista
  
  id = str(notebook_dado['ID'])
  lista.append(str(id.split('Name')[0][5:-1].strip(" ")))
  
  marca = str(notebook_dado['marca'])
  lista.append( marca.split('Name')[0][5:-1].strip(" "))

  linha = str(notebook_dado['linha'])
  lista.append(linha.split('Name')[0][5:-1].strip(" "))

  modelo = str(notebook_dado['modelo'])
  lista.append(modelo.split('Name')[0][5:-1].strip(" "))

  memoria = str(notebook_dado['ram'])
  lista.append(memoria.split('Name')[0][3:-1].strip(" ")+'GB')

  cpu = str(notebook_dado['processador'])
  lista.append(cpu.split('Name')[0][5:-1].strip(" "))

  vga = str(notebook_dado['vga_dedicaca'])
  lista.append(vga.split('Name')[0][5:-1].strip(" ").replace('-',' '))
  
  ssd = str(notebook_dado['ssd'])
  ssd = ssd.split('Name')[0][5:-1].strip(" ")
  if (ssd == '1.0'):
    lista.append(ssd + 'TB')
  else:
    lista.append(ssd + 'GB')
    
  hd = str(notebook_dado['hd'])
  lista.append(hd.split('Name')[0][5:-3].strip(" ")+'GB')

  tela = str(notebook_dado['tela_resolucao'])
  lista.append(tela.split('Name')[0][5:-1].strip(" "))

  so = str(notebook_dado['so'])
  lista.append(so.split('Name')[0][5:-1].strip(" "))

  avista = str(notebook_dado['preco_avista'])
  a = avista.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a)*1000)
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_avista = d.replace('v','.')
  lista.append(str('R$'+note_avista))


  aprazo = str(notebook_dado['preco_aprazo'])
  a = aprazo.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a)*1000)
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_aprazo = d.replace('v','.')
  lista.append(str('R$'+note_aprazo))

  link_avista = str(notebook_dado['link_avista'])
  lista.append(link_avista.split('Name')[0][5:-1].strip(" "))

  link_aprazo = str(notebook_dado['link_aprazo'])
  lista.append(link_aprazo.split('Name')[0][5:-1].strip(" "))

  loja_avista = str(notebook_dado['loja_avista'])
  lista.append(loja_avista.split('Name')[0][5:-1].strip(" "))

  
  notebook_dado = ''