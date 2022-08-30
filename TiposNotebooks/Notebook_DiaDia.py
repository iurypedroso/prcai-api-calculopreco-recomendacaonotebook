
def notebook_diario(lista_notebooks,tipo_operacao,pref,pref_ram, pref_cpu,pref_vga,pref_armazenamento,pref_so,pref_tela,tipo_notebook, pref_modelo,investimento,tipo_pagamento):
  
    #FILTRO SO
  if (pref_so != 'MacOS' and pref_so != 'n/a'):
    lista_notebooks = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
  elif (pref_so == 'MacOS'):
    lista_notebooks = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
    if (pref_modelo != 'n/a'):
      if(len(lista_notebooks.loc[lista_notebooks['linha']==pref_modelo])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks['linha']==pref_modelo]
      else:
        pass
    else:
      pass
  else:
    lista_notebooks = lista_note_tipo
      
     #CHECA SE TEM PREFERÊNCIA DE CPU OU NÃO
    if(pref_cpu != 'n/a'):
      if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith(pref_cpu)==True])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith(pref_cpu)==True]
      else:
        #Tratando caso Core i7
        if (pref_cpu == 'Intel Core i7'):
          if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i5')==True])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i5')==True]
          else:
            if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i3')==True])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i3')==True]
            else:
              if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True]
              else:
                pass
        #Tratanto caso Core i5
        elif (pref_cpu == 'Intel Core i5'):
          if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i3')==True])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Core i3')==True]
          else:
            if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True]
            else:
              if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Celeron')==True])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Celeron')==True]
              else:
                pass
        #Tratando caso Core i3
        elif (pref_cpu == 'Intel Core i3'):
          if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Pentium Gold')==True]
          else:
            if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Celeron')==True])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('Intel Celeron')==True]
            else:
              pass
        #Tratando caso Ryzen 7
        elif (pref_cpu == 'AMD Ryzen 7'):
          if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 5')==True])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 5')==True]
          else:
            if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 3')==True])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 3')==True]
            else:
              pass
        #Tratando caso Ryzen 5
        elif (pref_cpu == 'AMD Ryzen 5'):
          if (len(lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 3')==True])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['processador'].str.startswith('AMD Ryzen 3')==True]
          else:
            pass
        else:
          pass
    else:
      pass
      
    #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
    if(pref_ram != 'n/a'):
      if(len(lista_notebooks.loc[lista_notebooks['ram']==pref_ram])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==pref_ram]
      else:
        #Tratando RAM 32GB
        if(pref_ram == 32):
          if(len(lista_notebooks.loc[lista_notebooks['ram']==16])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==16]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ram']==12])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==12]
            else:
              if(len(lista_notebooks.loc[lista_notebooks['ram']==8])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==8]
              else:
                if(len(lista_notebooks.loc[lista_notebooks['ram']==4])>0):
                  lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==4]
                else:
                  pass
        #Tratando RAM 16GB
        elif(pref_ram == 16):
          if(len(lista_notebooks.loc[lista_notebooks['ram']==12])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==12]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ram']==8])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==8]
            else:
              if(len(lista_notebooks.loc[lista_notebooks['ram']==4])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==4]
              else:
                pass
        #Tratando RAM 12GB
        elif(pref_ram == 12):
          if(len(lista_notebooks.loc[lista_notebooks['ram']==8])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==8]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ram']==4])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==4]
            else:
              pass
        #Tratando RAM 8GB
        elif(pref_ram == 8):
          if(len(lista_notebooks.loc[lista_notebooks['ram']==4])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ram']==4]
          else:
            pass
        #Tratando RAM 4GB
        else:
          pass
    else:
      pass
      
    #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
    if(pref_tela != 'n/a'):
      if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']==pref_tela])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']==pref_tela]
      else:
        #Tratando tela 4K
        if(pref_tela == '4K'):
          if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD+'])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD+']
          else:
            if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD'])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD']
            else:
              if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD'])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD']
              else:
                pass
        #Tratando tela Full HD+
        elif(pref_tela == 'Full HD+'):
          if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD'])>0):
             lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='Full HD']
          else:
            if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD'])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD']
            else:
              pass
        #Tratando tela Full HD
        elif(pref_tela == 'Full HD'):
          if(len(lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD'])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['tela_resolucao']=='HD']
          else:
            pass
        #Tratando tela HD
        else:
          pass
    else:
      pass
      
    #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO OU NÃO
    if(pref_armazenamento != 'n/a'):
      if(len(lista_notebooks.loc[lista_notebooks['ssd']==pref_armazenamento])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==pref_armazenamento]
      else:
        if (pref_armazenamento == 1024):
          if(len(lista_notebooks.loc[lista_notebooks['ssd']==512])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==512]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ssd']==480])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==480]
            else:
              if(len(lista_notebooks.loc[lista_notebooks['ssd']==256])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==256]
              else:
                if(len(lista_notebooks.loc[lista_notebooks['ssd']==240])>0):
                  lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==240]
                else:
                  if(len(lista_notebooks.loc[lista_notebooks['ssd']==128])>0):
                    lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==128]
                  else:
                    if(len(lista_notebooks.loc[lista_notebooks['ssd']==120])>0):
                      lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==120]
                    else:
                      pass
        elif (pref_armazenamento == 512):
          if(len(lista_notebooks.loc[lista_notebooks['ssd']==480])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==480]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ssd']==256])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==256]
            else:
              if(len(lista_notebooks.loc[lista_notebooks['ssd']==240])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==240]
              else:
                if(len(lista_notebooks.loc[lista_notebooks['ssd']==128])>0):
                  lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==128]
                else:
                  if(len(lista_notebooks.loc[lista_notebooks['ssd']==120])>0):
                    lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==120]
                  else:
                    pass
        elif (pref_armazenamento == 256):
          if(len(lista_notebooks.loc[lista_notebooks['ssd']==240])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==240]
          else:
            if(len(lista_notebooks.loc[lista_notebooks['ssd']==128])>0):
              lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==128]
            else:
              if(len(lista_notebooks.loc[lista_notebooks['ssd']==120])>0):
                lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==120]
              else:
                pass
        elif (pref_armazenamento == 128):
          if(len(lista_notebooks.loc[lista_notebooks['ssd']==120])>0):
            lista_notebooks = lista_notebooks.loc[lista_notebooks['ssd']==120]
          else:
            pass
        else:
          pass
    else:
      pass
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(lista_notebooks.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(lista_notebooks.sort_values(by='preco_avista', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(lista_notebooks.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(lista_notebooks.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    elif tipo_operacao == 'media_valores':
      print('entrou')
      calculo_media(lista_notebooks)
    else:
      if(len(lista_notebooks.loc[lista_notebooks[tipo_pagamento]<=investimento])>0):
        lista_notebooks = lista_notebooks.loc[lista_notebooks[tipo_pagamento]<=investimento]
      else:
        lista_notebooks = lista_notebooks.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print(lista_notebooks)
    