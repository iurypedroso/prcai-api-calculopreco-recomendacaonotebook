import os, mysql.connector,pandas as pd

class Database():
  def __init__(self):
    self.host = os.environ['heroku_db_host']
    self.database = os.environ['heroku_db']
    self.user = os.environ['heroku_db_username']
    self.password = os.environ['heroku_db_password']

  def coleta_banco_completo(self):
    #Open DB Connection
    con2 = mysql.connector.connect(host=self.host,
                                     database=self.database,
                                     user= self.user,
                                     password= self.password)
    cursor = con2.cursor()
    #Make the Query and assign it to an DataFrame
    banco_notebook_completo = pd.read_sql(open('Querys/coleta_bd_notebooks_completo_disponivel.txt','r').read(), con=con2)
    #Format the DataFrame with the specified columns
    banco_notebook_formatado = banco_notebook_completo[['ID','marca','modelo','linha','serie','ram','processador','processador_performance','vga_dedicaca','vga_performance','tela','tela_resolucao','ssd','hd','so','trabalho','trabalho_cpu','dia_dia','trabalho_simples','estudos_simples','trabalho_vga','estudos_vga','trabalho_visual','estudos_visual','gamer','performance','preco_avista','preco_aprazo','beneficio_avista','beneficio_aprazo','link_avista','link_aprazo','loja_avista','loja_aprazo','link_imagem']]
    return banco_notebook_formatado
    #Close DB Connection
    cursor.close()
    con2.close()