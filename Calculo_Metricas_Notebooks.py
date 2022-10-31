import Classes.Conexao_Banco
from funcoes import calculo_media
lista_notebooks_precos,resul_pesq_usuario = [],[]
menor_valor_avista,menor_valor_aprazo = 0, 0
menor_valor_avista_str,menor_valor_aprazo_str,result_filtro_tipo_recom = '','',''
import Funcoes.Conv_FloatBRL
import Funcoes.DistanciaEuclidiana

def coletar_preco(tipo_operacao, NotebookUsuario):
  
  global resul_pesq_usuario, notebooks_dataframe,menor_valor_avista,menor_valor_aprazo,menor_valor_avista_str,menor_valor_aprazo_str, lista_notebooks_precos

  Database = Classes.Conexao_Banco.Database()
  notebooks_dataframe = Database.coleta_banco_completo()
    
  lista_notebooks_precos.clear()
  resul_pesq_usuario=notebooks_dataframe
  lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
  resul_pesq_usuario = lista_note_tipo

  #         =====INICIO NOTEBOOK BÁSICO=====         #
  if(NotebookUsuario.tipo_notebook == 'dia_dia' or NotebookUsuario.tipo_notebook == 'trabalho_simples' or NotebookUsuario.tipo_notebook == 'estudos_simples'): #RAM, CPU, SSD
    resul_pesq_usuario = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
    resul_pesq_usuario = lista_note_tipo
    #FILTRO SO
    if (NotebookUsuario.pref_so != 'MacOS' and NotebookUsuario.pref_so != 'n/a'):
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(NotebookUsuario.so)==False].index, inplace=False)
    elif (NotebookUsuario.so == 'MacOS'):
      resul_pesq_usuario = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (NotebookUsuario.pref_modelo != 'n/a'):
        if(len(resul_pesq_usuario.loc[resul_pesq_usuario['linha']==NotebookUsuario.pref_modelo])>0):
          resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['linha']==NotebookUsuario.pref_modelo]
        else:
          pass
      else:
        pass
    else:
      resul_pesq_usuario = lista_note_tipo
     #CHECA SE TEM PREFERÊNCIA DE CPU OU NÃO
    if(NotebookUsuario.cpu != 'n/a'):
      if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(NotebookUsuario.cpu)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(NotebookUsuario.cpu)==True]
      else:
        pass 
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE RAM OU NÃO
    if(NotebookUsuario.ram != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==NotebookUsuario.ram])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==NotebookUsuario.ram]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE TELA OU NÃO
    if(NotebookUsuario.tela != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']==NotebookUsuario.tela])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']==NotebookUsuario.tela]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO OU NÃO
    if(NotebookUsuario.armazenamento != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=NotebookUsuario.armazenamento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=NotebookUsuario.armazenamento]
      else:
        pass
    else:
      pass

    
     #CHECAR DADOS
    # melhor_cpu = float(str(resul_pesq_usuario.sort_values(by='processador_performance', ascending=False).head(1)['processador_performance']).split('Name')[0][5:-1].strip(" "))
    # melhor_cpu_nome =str(resul_pesq_usuario.sort_values(by='processador_performance', ascending=False).head(1)['processador']).split('Name')[0][5:-1].strip(" ")
    # melhor_ram = float(str(resul_pesq_usuario.sort_values(by='ram', ascending=False).head(1)['ram']).split('Name')[0][5:-1].strip(" "))
    # melhor_ram_quantidade = float(str(resul_pesq_usuario.sort_values(by='ram', ascending=False).head(1)['ram']).split('Name')[0][5:-1].strip(" "))
    # melhor_vga = float(str(resul_pesq_usuario.sort_values(by='vga_performance', ascending=False).head(1)['vga_performance']).split('Name')[0][5:-1].strip(" "))
    # melhor_vga_modelo =str(resul_pesq_usuario.sort_values(by='vga_performance', ascending=False).head(1)['vga_dedicaca']).split('Name')[0][5:-1].strip(" ")
    # melhor_ssd = float(str(resul_pesq_usuario.sort_values(by='ssd', ascending=False).head(1)['ssd']).split('Name')[0][5:-1].strip(" "))
    # melhor_performance = float(str(resul_pesq_usuario.sort_values(by='performance', ascending=False).head(1)['performance']).split('Name')[0][5:-1].strip(" "))
    # melhor_performance_valor = float(str(resul_pesq_usuario.sort_values(by='performance', ascending=False).head(1)['performance']).split('Name')[0][5:-1].strip(" "))
    # maior_tela = float(str(resul_pesq_usuario.sort_values(by='tela', ascending=False).head(1)['tela']).split('Name')[0][5:-1].strip(" "))
    # melhor_resolucao = float(8294)
    
    # print('CPU: '+melhor_cpu_nome)
    # print('RAM: '+str(melhor_ram_quantidade))
    # print('VGA: '+melhor_vga_modelo)
    # print('SSD: '+str(melhor_ssd))
    # print('MAIS POTENTE: '+str(melhor_performance_valor))
    
    # melhor_maquina = np.array((melhor_cpu,melhor_ram,melhor_vga,melhor_resolucao,melhor_ssd,melhor_performance))
    # print(melhor_maquina)
    # resul_pesq_usuario = Funcoes.DistanciaEuclidiana.euclidiana(melhor_maquina,resul_pesq_usuario)

    
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    elif tipo_operacao == 'media_valores':
      print('entrou')
      calculo_media(resul_pesq_usuario)
    else:
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento]
      else:
        resul_pesq_usuario = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print(resul_pesq_usuario)
    
      #         =====FIM NOTEBOOK BÁSICO=====         #



    
      #         =====INÍCIO NOTEBOOK GAMER=====         #

  elif (NotebookUsuario.tipo_notebook == 'gamer'):
    resul_pesq_usuario = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
    resul_pesq_usuario = lista_note_tipo
    #FILTRO SO
    if (pref_so != 'n/a'):
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    else:
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith('Windows')==False].index, inplace=False)
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        if(pref_vga == 'GeForce RTX 3070'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3060')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3060')==True]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True]
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
              else:
                pass
        if(pref_vga == 'GeForce RTX 3060'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
            else:
              pass
        if(pref_vga == 'GeForce RTX 3050'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
          else:
            pass
        else:
          pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(pref_cpu != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True]
      else:
        if(pref_cpu == 'Intel Core i9'):
          if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i7')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i7')==True]
          else:
            if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i5')==True])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i5')==True]
            else:
              pass
        elif (pref_cpu == 'Intel Core i7'):
          if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i5')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('Intel Core i5')==True]
          else:
            pass
        elif (pref_cpu == 'AMD Ryzen 7'):
          if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('AMD Ryzen 5')==True])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith('AMD Ryzen 5')==True]
          else:
            pass
        else:
          pass
    else:
      pass
      
    #CHECA PREFERÊNCIA DE RAM  
    if(pref_ram != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram]
      else:
        #Tratando RAM 32GB
        if(pref_ram == 32):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==16])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==16]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==12])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==12]
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8]
              else:
                pass

        #Tratando RAM 16GB
        elif(pref_ram == 16):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==12])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==12]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8]
            else:
              pass
        #Tratando RAM 12GB
        elif(pref_ram == 12):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==8]
          else:
            pass
        else:
          pass
    else:
      pass
      
    #CHECA PREFERÊNCIA DE TELA    
    if (pref_tela != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True]
      else:
        #Tratando tela 4K
        if(pref_tela == '4K'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD+'])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD+']
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD'])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD']
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD'])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD']
              else:
                pass
        #Tratando tela Full HD+
        elif(pref_tela == 'Full HD+'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD'])>0):
             resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='Full HD']
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD'])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD']
            else:
              pass
        #Tratando tela Full HD
        elif(pref_tela == 'Full HD'):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD'])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']=='HD']
          else:
            pass
        #Tratando tela HD
        else:
          pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (pref_armazenamento != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento]
      else:
        if (pref_armazenamento == 1024):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==512])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==512]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==480])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==480]
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==256])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==256]
              else:
                if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240])>0):
                  resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240]
                else:
                  if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128])>0):
                    resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128]
                  else:
                    if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120])>0):
                      resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120]
                    else:
                      pass
        elif (pref_armazenamento == 512):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==480])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==480]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==256])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==256]
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240]
              else:
                if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128])>0):
                  resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128]
                else:
                  if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120])>0):
                    resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120]
                  else:
                    pass
        elif (pref_armazenamento == 256):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==240]
          else:
            if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128])>0):
              resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==128]
            else:
              if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120])>0):
                resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120]
              else:
                pass
        elif (pref_armazenamento == 128):
          if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120])>0):
            resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']==120]
          else:
            pass
        else:
          pass
    else:
      pass
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)  
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento]
      else:
        resul_pesq_usuario = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print(resul_pesq_usuario)


    
    #         =====FIM NOTEBOOK GAMER=====         #




    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #

  elif (tipo_notebook == 'trabalho_visual' or tipo_notebook == 'estudos_visual'):

    resul_pesq_usuario = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_notebook]==0].index, inplace=False)
    resul_pesq_usuario = lista_note_tipo
    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      resul_pesq_usuario = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        if(len(resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo])>0):
          resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo]
        else:
          pass
      else:
        pass
    else:
      resul_pesq_usuario = lista_note_tipo
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE TELA
    if(pref_tela != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']==pref_tela])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao']==pref_tela]
      else:
        pass
    else:
      pass
      #CHECA SE TEM PREFERÊNCIA DE CPU
    if(pref_cpu == 'sim' or pref_cpu == 'nao'):
      if (len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA SE TEM PREFERÊNCIA DE RAM
    if(pref_ram != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram]
      else:
        pass
    else:
      pass
    
    #CHECA SE TEM PREFERÊNCIA DE ARMAZENAMENTO
    if(pref_armazenamento != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass
  
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento]
      else:
        resul_pesq_usuario = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print(resul_pesq_usuario)

    #         =====FIM NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #


    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VGA=====         #
  elif (tipo_notebook == 'trabalho_vga' or tipo_notebook == 'estudos_vga'):
    resul_pesq_usuario = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_notebook]==0].index, inplace=False)
    resul_pesq_usuario = lista_note_tipo
    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      resul_pesq_usuario = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        if(len(resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo])>0):
          resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo]
        else:
          pass
      else:
        pass
    else:
      resul_pesq_usuario = lista_note_tipo
      
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(pref_cpu != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM
    if (pref_ram != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA
    if (pref_tela != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (pref_armazenamento != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass

    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento]
      else:
        resul_pesq_usuario = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print('INVESTIMENTO INSUFICIENTE')
    
  #         =====FIM NOTEBOOK TRABALHO/ESTUDO VGA=====         #

  #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO PERSONALIZADO=====         #
  elif (tipo_notebook == 'trabalho_cpu' or tipo_notebook == 'trabalho'):
    resul_pesq_usuario = notebooks_dataframe.drop(notebooks_dataframe.loc[notebooks_dataframe['preco_avista']==0].index, inplace=False)
    lista_note_tipo = resul_pesq_usuario.drop(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_notebook]==0].index, inplace=False)
    resul_pesq_usuario = lista_note_tipo
    #FILTRO SO
    if (pref_so != 'MacOS' and pref_so != 'n/a'):
      resul_pesq_usuario = lista_note_tipo.drop(lista_note_tipo.loc[lista_note_tipo['so'].str.startswith(pref_so)==False].index, inplace=False)
    elif (pref_so == 'MacOS'):
      resul_pesq_usuario = lista_note_tipo.loc[lista_note_tipo['marca']=='Apple']
      if (pref_modelo != 'n/a'):
        if(len(resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo])>0):
          resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['linha']==pref_modelo]
        else:
          pass
      else:
        pass
    else:
      resul_pesq_usuario = lista_note_tipo
      
    #CHECA PREFERÊNCIA DE VGA
    if(pref_vga != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['vga_dedicaca'].str.startswith(pref_vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(pref_cpu != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['processador'].str.startswith(pref_cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM
    if (pref_ram != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ram']==pref_ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA
    if (pref_tela != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['tela_resolucao'].str.startswith(pref_tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (pref_armazenamento != 'n/a'):
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario['ssd']>=pref_armazenamento]
      else:
        pass
    else:
      pass

    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(resul_pesq_usuario.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(resul_pesq_usuario.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento])>0):
        resul_pesq_usuario = resul_pesq_usuario.loc[resul_pesq_usuario[tipo_pagamento]<=investimento]
      else:
        resul_pesq_usuario = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending = True).head(5)
        print('INVESTIMENTO INSUFICIENTE')
    
  #         =====FIM NOTEBOOK TRABALHO/ESTUDO PERSONALIZADO=====         #
