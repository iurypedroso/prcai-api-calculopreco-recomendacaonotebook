def calculo_media (lista_de_notebooks):
  coluna_valores_avista = lista_de_notebooks['preco_avista']
  somatorio_valor_avista = 0
  print('Entrou na função')
  for valor_avista in coluna_valores_avista:
    somatorio_valor_avista += valor_avista

  media_investimento_avista = somatorio_valor_avista/(len(coluna_valores_avista.index))
  print(media_investimento_avista)