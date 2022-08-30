lista = []

def ajuste_dataframe(result_filtro_tipo_recom):
  global lista
  id = str(result_filtro_tipo_recom['ID'])
  lista.append(str(id.split('Name')[0][5:-1].strip(" ")))
  
  marca = str(result_filtro_tipo_recom['marca'])
  lista.append( marca.split('Name')[0][5:-1].strip(" "))

  linha = str(result_filtro_tipo_recom['linha'])
  lista.append(linha.split('Name')[0][5:-1].strip(" "))

  modelo = str(result_filtro_tipo_recom['modelo'])
  lista.append(modelo.split('Name')[0][5:-1].strip(" "))

  memoria = str(result_filtro_tipo_recom['ram'])
  lista.append(memoria.split('Name')[0][3:-1].strip(" ")+'GB')

  cpu = str(result_filtro_tipo_recom['processador'])
  lista.append(cpu.split('Name')[0][5:-1].strip(" "))

  vga = str(result_filtro_tipo_recom['vga_dedicaca'])
  lista.append(vga.split('Name')[0][5:-1].strip(" ").replace('-',' '))
  
  ssd = str(result_filtro_tipo_recom['ssd'])
  ssd = ssd.split('Name')[0][5:-1].strip(" ")
  if (ssd == '1.0'):
    lista.append(ssd + 'TB')
  else:
    lista.append(ssd + 'GB')
    
  hd = str(result_filtro_tipo_recom['hd'])
  lista.append(hd.split('Name')[0][5:-3].strip(" ")+'GB')

  tela = str(result_filtro_tipo_recom['tela_resolucao'])
  lista.append(tela.split('Name')[0][5:-1].strip(" "))

  so = str(result_filtro_tipo_recom['so'])
  lista.append(so.split('Name')[0][5:-1].strip(" "))

  avista = str(result_filtro_tipo_recom['preco_avista'])
  a = avista.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a))
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_avista = d.replace('v','.')
  lista.append(str('R$'+note_avista))


  aprazo = str(result_filtro_tipo_recom['preco_aprazo'])
  a = aprazo.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a))
  c = b.replace(',','v')
  d = c.replace('.',',')
  note_aprazo = d.replace('v','.')
  lista.append(str('R$'+note_aprazo))

  link_avista = str(result_filtro_tipo_recom['link_avista'])
  lista.append(link_avista.split('Name')[0][5:-1].strip(" "))

  link_aprazo = str(result_filtro_tipo_recom['link_aprazo'])
  lista.append(link_aprazo.split('Name')[0][5:-1].strip(" "))

  loja_avista = str(result_filtro_tipo_recom['loja_avista'])
  lista.append(loja_avista.split('Name')[0][5:-1].strip(" "))

  loja_aprazo = str(result_filtro_tipo_recom['loja_aprazo'])
  lista.append(loja_aprazo.split('Name')[0][5:-1].strip(" "))

  imagem = str(result_filtro_tipo_recom['link_imagem'])
  lista.append(imagem.split('Name')[0][5:-1].strip(" "))
  
  return lista