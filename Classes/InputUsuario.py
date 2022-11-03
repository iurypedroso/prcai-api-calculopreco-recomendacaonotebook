
class InputUsuario():
  def __init__(self,inputUsuario):
    self.pref = inputUsuario['pref']
    self.tipo_notebook = inputUsuario['tipo_notebook']
    self.pref_modelo = inputUsuario['pref_modelo']
    self.ram = self.SetRam(inputUsuario)
    self.cpu = inputUsuario['pref_cpu']
    self.armazenamento = self.SetArmazenamento(inputUsuario)
    self.so = inputUsuario['pref_so']
    self.vga = inputUsuario['pref_vga']
    self.tela = inputUsuario['pref_tela']
    self.tipo_pagamento = 'sem_tipo_pagamento'
    self.investimento = 'sem_investimento'

  def SetRam(self,inputUsuario):
    if (inputUsuario['pref_ram'] == 'n/a'):
      return 'n/a'
    else:
      return int(inputUsuario['pref_ram'])

  def SetArmazenamento(self,inputUsuario):
    if (inputUsuario['pref_armazenamento'] == 'n/a'):
      return 'n/a'
    else:
      armazenamento = int(inputUsuario['pref_armazenamento'])
      if(armazenamento == 1000 or armazenamento ==1024)
      return int(inputUsuario['pref_armazenamento'])

  def SetTipoPagamento(self,inputUsuario):
    if inputUsuario == 'avista':
      self.tipo_pagamento = 'preco_avista'
    else:
      self.tipo_pagamento = 'preco_aprazo'
      
  def SetInvestimento(self,inputUsuario):
    self.investimento = float(inputUsuario)
    
    