class Notebook():
  def __init__(self,id,marca,linha,modelo,memoria,cpu,vga,ssd,hd,tela,so,avista,aprazo,link_avista,link_aprazo,loja_vista,loja_aprazo,imagem):
    self.id = id
    self.marca = marca
    self.linha = linha
    self.modelo = modelo
    self.memoria = memoria
    self.cpu = cpu
    self.vga = vga
    self.ssd = ssd
    self.hd = hd
    self.tela = tela
    self.so = so
    self.avista = avista
    self.aprazo = aprazo
    self.link_avista = link_avista
    self.link_aprazo = link_aprazo
    self.loja_avista = loja_vista
    self.loja_aprazo = loja_aprazo
    self.imagem = imagem

class NotebookResultadoPreco():
  def __init__(self,inputUsuario):
    self.id = self.SetID(inputUsuario)
    self.marca = self.SetMarca(inputUsuario)
    self.linha = self.SetLinha(inputUsuario)
    self.modelo = self.SetModelo(inputUsuario)
    self.ram = self.SetRAM(inputUsuario)
    self.cpu = self.SetCPU(inputUsuario)
    self.vga = self.SetVGA(inputUsuario)
    self.ssd = self.SetSSD(inputUsuario)
    self.hd = self.SetHD(inputUsuario)
    self.tela = self.SetTela(inputUsuario)
    self.so = self.SetSO(inputUsuario)
    self.avista = self.SetAvista(inputUsuario)
    self.aprazo = self.SetAprazo(inputUsuario)
    self.link = self.SetLink(inputUsuario)

  def SetID(self,inputUsuario):
    return inputUsuario['ID'].to_string(index=False)
  def SetMarca(self,inputUsuario):
    return inputUsuario['marca'].to_string(index=False)
  def SetLinha(self,inputUsuario):
    return inputUsuario['linha'].to_string(index=False)
  def SetModelo(self,inputUsuario):
    return inputUsuario['modelo'].to_string(index=False)
  def SetRAM(self, inputUsuario):
    return inputUsuario['ram'].to_string(index=False)
  def SetCPU(self,inputUsuario):
    return inputUsuario['processador'].to_string(index=False)
  def SetVGA(self,inputUsuario):
    return inputUsuario['vga_dedicaca'].to_string(index=False)
  def SetSSD(self, inputUsuario):
    return inputUsuario['ssd'].to_string(index=False)
  def SetHD(self,inputUsuario):
    return inputUsuario['hd'].to_string(index=False)
  def SetTela(self,inputUsuario):
    return inputUsuario['tela'].to_string(index=False)
  def SetSO(self,inputUsuario):
    return inputUsuario['so'].to_string(index=False)
  def SetAvista(self, inputUsuario):
    return inputUsuario['preco_avista'].to_string(index=False)
  def SetAprazo(self, inputUsuario):
    return inputUsuario['preco_aprazo'].to_string(index=False)
  def SetLink(self, inputUsuario):
    return inputUsuario['link_avista'].to_string(index=False)