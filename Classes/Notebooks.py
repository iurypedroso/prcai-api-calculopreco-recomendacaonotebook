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
  def __init__():
    self.id = ''
    self.marca = ''
    self.linha = ''
    self.modelo = ''
    self.ram = ''
    self.cpu = ''
    self.vga = ''
    self.ssd = ''
    self.hd = ''
    self.tela = ''
    self.so = ''
    self.avista = 0.0
    self.aprazo = 0.0
    self.link = ''

  def SetID(self,id):
    self.id = id
  def SetMarca(self,marca):
    self.marca = marca
  def SetLinha(self,linha):
    self.linha = linha
  def SetModelo(self,modelo):
    self.modelo = modelo
  def SetRAM(self, ram):
    self.ram = ram
  def SetCPU(self,cpu):
    self.cpu = cpu
  def SetVGA(self,vga):
    self.vga = vga
  def SetSSD(self, ssd):
    self.ssd = ssd
  def SetHD(sef,hd):
    self.hd = hd
  def SetTela(self,tela):
    self.tela = tela
  def SetSO(self,so):
    self.so = so
  def SetAvista(self, avista):
    self.avista = avista
  def SetAprazo(self, aprazo):
    self.aprazo = aprazo
  def SetLink(self, link):
    self.link = link