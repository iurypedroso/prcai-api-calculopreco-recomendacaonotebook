import numpy as np
import pandas as pd
def maior_performance():
  from Calculo_Metricas_Notebooks import resul_pesq_usuario
  from Funcoes import Maior_Performance
  data = []
  # resultado_maior_performance = resul_pesq_usuario.sort_values(by='performance', ascending=False)
  # return resultado_maior_performance.head(1)

  #COLETAR MELHOR COMBINAÇÃO POSSÍVEL DA CATEGORIA(MESMO NÃO EXISTINDO)
  melhor_cpu = float(str(resul_pesq_usuario.sort_values(by='processador_performance', ascending=False).head(1)['processador_performance']).split('Name')[0][5:-1].strip(" "))
  melhor_cpu_nome =str(resul_pesq_usuario.sort_values(by='processador_performance', ascending=False).head(1)['processador']).split('Name')[0][5:-1].strip(" ")
  melhor_ram = float(str(resul_pesq_usuario.sort_values(by='ram', ascending=False).head(1)['ram']).split('Name')[0][5:-1].strip(" "))
  melhor_ram_quantidade = float(str(resul_pesq_usuario.sort_values(by='ram', ascending=False).head(1)['ram']).split('Name')[0][5:-1].strip(" "))
  melhor_vga = float(str(resul_pesq_usuario.sort_values(by='vga_performance', ascending=False).head(1)['vga_performance']).split('Name')[0][5:-1].strip(" "))
  melhor_vga_modelo =str(resul_pesq_usuario.sort_values(by='vga_performance', ascending=False).head(1)['vga_dedicaca']).split('Name')[0][5:-1].strip(" ")
  melhor_ssd = float(str(resul_pesq_usuario.sort_values(by='ssd', ascending=False).head(1)['ssd']).split('Name')[0][5:-1].strip(" "))
  melhor_performance = float(str(resul_pesq_usuario.sort_values(by='performance', ascending=False).head(1)['performance']).split('Name')[0][5:-1].strip(" "))
  melhor_performance_valor = float(str(resul_pesq_usuario.sort_values(by='performance', ascending=False).head(1)['performance']).split('Name')[0][5:-1].strip(" "))
  maior_tela = float(str(resul_pesq_usuario.sort_values(by='tela', ascending=False).head(1)['tela']).split('Name')[0][5:-1].strip(" "))
  melhor_resolucao = float(8294)
  #ARRAY DA PERFORMANCE DA MELHOR MÁQUINA
  melhor_maquina_categoria = np.array((melhor_cpu,melhor_ram,melhor_vga,melhor_resolucao,melhor_ssd,melhor_performance))

  #EXTRAIR DADOS DE CADA MÁQUINA DO DATAFRAME RESTANTE
  for i in resul_pesq_usuario.index:
    id = float(resul_pesq_usuario['ID'][i])
    marca = resul_pesq_usuario['marca'][i]
    modelo = resul_pesq_usuario['modelo'][i]
    processador = float(resul_pesq_usuario['processador_performance'][i])
    ram = float(resul_pesq_usuario['ram'][i])
    vga = float(resul_pesq_usuario['vga_performance'][i])

    if (resul_pesq_usuario['tela_resolucao'][i] == '4K'):
      tela_resolucao = 8294
    elif (resul_pesq_usuario['tela_resolucao'][i] == 'Full HD+'):
      tela_resolucao = 3317
    elif (resul_pesq_usuario['tela_resolucao'][i] == 'Full HD'):
      tela_resolucao = 2073
    else:
      tela_resolucao = 921
    ssd = float(resul_pesq_usuario['ssd'][i])
    performance = float(resul_pesq_usuario['performance'][i])
    
    #MONTAR ARRAY COM AS CONFIGS DA MÁQUINA
    maquina = np.array((processador,ram,vga,tela_resolucao,ssd,performance))
    #COMPARAR A MÁQUINA COM A MELHOR MÁQUINA
    resultado = 100-(np.sqrt(np.sum(np.square(melhor_maquina_categoria-maquina)))/1000)
    #SALVAR RESULTADO NUMA LISTA
    data.append([id,marca,modelo,ram, processador,vga,tela_resolucao,ssd,resultado])
  #CONVERTER LISTA DE NOTEBOOKS, EM DATAFRAME COM AS INFORMAÇÕES    
  df = pd.DataFrame(data,columns=['ID','Marca','Moelo','RAM','CPU','VGA','Resolucao','SSD','Similaridade'])
  print(df.sort_values(by='Similaridade', ascending = False))