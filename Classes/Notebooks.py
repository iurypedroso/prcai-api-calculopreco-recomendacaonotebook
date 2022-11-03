class NotebookRecomendacao():
  def __init__(self,RecomendacaoUsuario):
    self.id = self.SetID(RecomendacaoUsuario)
    self.marca = self.SetMarca(RecomendacaoUsuario)
    self.linha = self.SetLinha(RecomendacaoUsuario)
    self.modelo = self.SetModelo(RecomendacaoUsuario)
    self.ram = self.SetRAM(RecomendacaoUsuario)
    self.cpu = self.SetCPU(RecomendacaoUsuario)
    self.vga = self.SetVGA(RecomendacaoUsuario)
    self.ssd = self.SetSSD(RecomendacaoUsuario)
    self.hd = self.SetHD(RecomendacaoUsuario)
    self.tela = self.SetTela(RecomendacaoUsuario)
    self.so = self.SetSO(RecomendacaoUsuario)
    self.avista = self.SetAvista(RecomendacaoUsuario)
    self.aprazo = self.SetAprazo(RecomendacaoUsuario)
    self.link = self.SetLink(RecomendacaoUsuario)
    self.imagem = self.SetImagem(RecomendacaoUsuario)

  def SetID(self,RecomendacaoUsuario):
    return int(RecomendacaoUsuario['ID'].to_string(index=False))
    
  def SetMarca(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['marca'].to_string(index=False)
    
  def SetLinha(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['linha'].to_string(index=False)
    
  def SetModelo(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['modelo'].to_string(index=False)
    
  def SetRAM(self, RecomendacaoUsuario):
    return (str(RecomendacaoUsuario['ram'].to_string(index=False))+'GB')
    
  def SetCPU(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['processador'].to_string(index=False)
    
  def SetVGA(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['vga_dedicaca'].to_string(index=False)
    
  def SetSSD(self, RecomendacaoUsuario):
    if(str(RecomendacaoUsuario['ssd'].to_string(index=False)) == '1.0'):
      return (str(RecomendacaoUsuario['ssd'].to_string(index=False))+'TB')
    else:
      return (str(RecomendacaoUsuario['ssd'].to_string(index=False))+'GB')
      
  def SetHD(self,RecomendacaoUsuario):
    return (str(RecomendacaoUsuario['hd'].to_string(index=False)) +'GB')
    
  def SetTela(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['tela'].to_string(index=False)
    
  def SetSO(self,RecomendacaoUsuario):
    return RecomendacaoUsuario['so'].to_string(index=False)
    
  def SetAvista(self, RecomendacaoUsuario):
    a = str(RecomendacaoUsuario['preco_avista'].to_string(index=False))
    b = '{:,.2f}'.format(float(a))
    c = b.replace(',','v')
    d = c.replace('.',',')
    avista = d.replace('v','.')
    return str('R$'+avista)
    
  def SetAprazo(self, RecomendacaoUsuario):
    a = str(RecomendacaoUsuario['preco_aprazo'].to_string(index=False))
    b = '{:,.2f}'.format(float(a))
    c = b.replace(',','v')
    d = c.replace('.',',')
    aprazo = d.replace('v','.')
    return str('R$'+aprazo)
    
  def SetLink(self, RecomendacaoUsuario):
    return RecomendacaoUsuario['link_avista'].to_string(index=False)
    
  def SetImagem(self, RecomendacaoUsuario):
    return RecomendacaoUsuario['imagem'].to_string(index=False)
  
  
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
    self.imagem = self.SetImagem(inputUsuario)

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
  def SetImagem(self, inputUsuario):
    return inputUsuario['imagem'].to_string(index=False)

