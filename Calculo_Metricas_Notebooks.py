import Funcoes.Conv_FloatBRL
import Funcoes.DistanciaEuclidiana
from funcoes import calculo_media
from Classes.InputUsuario import InputUsuario
from Classes.Notebooks import NotebookResultadoPreco
from Funcoes.ConversaoFloatxBRL import correcao_valor_avista_str,correcao_valor_avista_float,correcao_valor_aprazo_str,correcao_valor_aprazo_float
from Classes.Conexao_Banco import Database
from Applications.Modulos import Simples


def coletar_preco(tipo_operacao, NotebookUsuario):

  BancoDadosPROD = Database()
  ResultColetaNotebooksBancoDados = BancoDadosPROD.coleta_banco_completo()

  NotebooksFiltradosTipo = ResultColetaNotebooksBancoDados.drop(ResultColetaNotebooksBancoDados.loc[ResultColetaNotebooksBancoDados[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
  
  #         =====INICIO NOTEBOOK BÁSICO=====         #
  if(NotebookUsuario.tipo_notebook == 'dia_dia' or NotebookUsuario.tipo_notebook == 'trabalho_simples' or NotebookUsuario.tipo_notebook == 'estudos_simples'): #RAM, CPU, SSD
    ResultadoNotebooksUsuario = NotebookSimples.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)
      #         =====FIM NOTEBOOK BÁSICO=====         #

      #         =====INÍCIO NOTEBOOK GAMER=====         #
  elif (NotebookUsuario.tipo_notebook == 'gamer'):
    ResultadoNotebooksUsuario = NotebookGamer.ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario)

    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #

  elif (NotebookUsuario.tipo_notebook == 'trabalho_visual' or NotebookUsuario.tipo_notebook == 'estudos_visual'):
    
  
    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento]
      else:
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.sort_values(by=NotebookUsuario.tipo_pagamento, ascending = True).head(5)
        print(NotebooksFiltradosTipo)

    #         =====FIM NOTEBOOK TRABALHO/ESTUDO VISUAL=====         #


    #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO VGA=====         #
  elif (NotebookUsuario.tipo_notebook == 'trabalho_vga' or NotebookUsuario.tipo_notebook == 'estudos_vga'):
    NotebooksFiltradosTipo = ResultColetaNotebooksBancoDados.drop(ResultColetaNotebooksBancoDados.loc[ResultColetaNotebooksBancoDados['preco_avista']==0].index, inplace=False)
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.drop(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
    NotebooksFiltradosTipo = NotebooksFiltradosTipo
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
      NotebooksFiltradosTipo = NotebooksFiltradosTipo
      
    #CHECA PREFERÊNCIA DE VGA
    if(NotebookUsuario.vga != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(NotebookUsuario.cpu != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM
    if (NotebookUsuario.ram != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA
    if (NotebookUsuario.tela != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (NotebookUsuario.armazenamento != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento]
      else:
        pass
    else:
      pass

    #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
    if tipo_operacao == 'consulta_preco':
      menor_valor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_aprazo', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_aprazo', ascending = True).head(1)['ID'])
      
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(Funcoes.Conv_FloatBRL.correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    else:
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento]
      else:
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.sort_values(by=NotebookUsuario.tipo_pagamento, ascending = True).head(5)
        print('INVESTIMENTO INSUFICIENTE')
    
  #         =====FIM NOTEBOOK TRABALHO/ESTUDO VGA=====         #

  #         =====INÍCIO NOTEBOOK TRABALHO/ESTUDO PERSONALIZADO=====         #
  elif (NotebookUsuario.tipo_notebook == 'trabalho_cpu' or NotebookUsuario.tipo_notebook == 'trabalho'):
    NotebooksFiltradosTipo = ResultColetaNotebooksBancoDados.drop(ResultColetaNotebooksBancoDados.loc[ResultColetaNotebooksBancoDados['preco_avista']==0].index, inplace=False)
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.drop(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_notebook]==0].index, inplace=False)
    NotebooksFiltradosTipo = NotebooksFiltradosTipo
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
      NotebooksFiltradosTipo = NotebooksFiltradosTipo
      
    #CHECA PREFERÊNCIA DE VGA
    if(NotebookUsuario.vga != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE CPU    
    if(NotebookUsuario.cpu != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE RAM
    if (NotebookUsuario.ram != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE TELA
    if (NotebookUsuario.tela != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True]
      else:
        pass
    else:
      pass
    #CHECA PREFERÊNCIA DE ARMAZENAMENTO
    if (NotebookUsuario.armazenamento != 'n/a'):
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento]
      else:
        pass
    else:
      pass

  #CHECA OPERAÇÃO(SE PRECISA CONSULTAR PREÇO OU PEDIR RECOMENDAÇÃO)
  
  if tipo_operacao == 'consulta_preco':
      NotebookAvista = NotebookResultadoPreco()
      NotebookAprazo = NotebookResultadoPreco()
      
      menor_valor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['preco_avista'])
      menor_valor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['preco_aprazo'])
      id_menor_avista = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      id_menor_aprazo = str(NotebooksFiltradosTipo.sort_values(by='preco_avista', ascending = True).head(1)['ID'])
      lista_notebooks_precos.append(correcao_valor_avista_float(menor_valor_avista))
      lista_notebooks_precos.append(correcao_valor_avista_str(menor_valor_avista))
      lista_notebooks_precos.append(correcao_valor_aprazo_float(menor_valor_aprazo))
      lista_notebooks_precos.append(correcao_valor_aprazo_str(menor_valor_aprazo))
      lista_notebooks_precos.append(id_menor_avista)
      lista_notebooks_precos.append(id_menor_aprazo)
    elif tipo_operacao == 'media_valores':
      print('entrou')
      calculo_media(NotebooksFiltradosTipo)
    else:
      if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento])>0):
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo[NotebookUsuario.tipo_pagamento]<=NotebookUsuario.investimento]
      else:
        NotebooksFiltradosTipo = NotebooksFiltradosTipo.sort_values(by=NotebookUsuario.tipo_pagamento, ascending = True).head(5)
        print(NotebooksFiltradosTipo)
    
  #         =====FIM NOTEBOOK TRABALHO/ESTUDO PERSONALIZADO=====         #
