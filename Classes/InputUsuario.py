
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
      return int(inputUsuario['pref_armazenamento'])

  def SetTipoPagamento(self,inputUsuario):
    self.tipo_pagamento = inputUsuario

  def SetInvestimento(self,inputUsuario):
    self.investimento = float(inputUsuario)
    
    