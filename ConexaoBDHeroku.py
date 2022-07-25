import mysql.connector
import pandas as pd
import os

db_host = os.environ['heroku_db_host']
db_name = os.environ['heroku_db']
db_secret = os.environ['heroku_db_password']
db_username = os.environ['heroku_db_username']

#CRIAÇÃO CONEXÃO DB
con2 = mysql.connector.connect(host=db_host,
                                   database=db_name,
                                   user=db_username,
                                   password=db_secret)
cursor = con2.cursor()
#CONCLUSÃO CONEXÃO DB
  
#PUXANDO TODO A TABELA DE NOTEBOOKS PARA UM DATAFRAME
notebooks_dataframe = pd.read_sql('SELECT * FROM notebooks', con=con2)
#Limpando quantidade total de caracteres em coluna do dataframe
pd.set_option('display.max_colwidth', None)
#Filtrando as colunas necessárias no dataframe
notebooks_dataframe = notebooks_dataframe[['ID','marca','modelo','linha','serie','ram','processador','vga_dedicaca','tela','tela_resolucao','ssd','so','gamer','performance','preco_avista','preco_aprazo','link_avista','link_aprazo','loja_avista','loja_aprazo']]

#FINALIZAÇÃO CONEXÃO BD
cursor.close()
con2.close()