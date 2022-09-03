import numpy as np
import pandas as pd

def euclidiana(melhor_maquina,dataframe):
  data = []
  for i in dataframe.index:
    id = float(dataframe['ID'][i])
    marca = dataframe['marca'][i]
    modelo = dataframe['modelo'][i]
    processador = float(dataframe['processador_performance'][i])
    ram = float(dataframe['ram'][i])
    vga = float(dataframe['vga_performance'][i])

    if (dataframe['tela_resolucao'][i] == '4K'):
      tela_resolucao = 8294
    elif (dataframe['tela_resolucao'][i] == 'Full HD+'):
      tela_resolucao = 3317
    elif (dataframe['tela_resolucao'][i] == 'Full HD'):
      tela_resolucao = 2073
    else:
      tela_resolucao = 921
    ssd = float(dataframe['ssd'][i])
    performance = float(dataframe['performance'][i])
    
    
    maquina = np.array((processador,ram,vga,tela_resolucao,ssd,performance))
    resultado = 100-(np.sqrt(np.sum(np.square(melhor_maquina-maquina)))/1000)
    data.append([id,marca,modelo,ram, processador,vga,tela_resolucao,ssd,resultado])
  df = pd.DataFrame(data,columns=['ID','Marca','Moelo','RAM','CPU','VGA','Resolucao','SSD','Similaridade'])
  print(df.sort_values(by='Similaridade', ascending = False))
