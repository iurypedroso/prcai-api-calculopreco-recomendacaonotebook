
def ChecarNotebooks(NotebooksFiltradosTipo,NotebookUsuario):
  if (NotebookUsuario.so != 'n/a'):
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.drop(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['so'].str.startswith(NotebookUsuario.so)==False].index, inplace=False)
  else:
    NotebooksFiltradosTipo = NotebooksFiltradosTipo.drop(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['so'].str.startswith('Windows')==False].index, inplace=False)
  #CHECA PREFERÊNCIA DE VGA
  if(NotebookUsuario.vga != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith(NotebookUsuario.vga)==True]
    else:
      if(NotebookUsuario.vga == 'GeForce RTX 3070'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3060')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3060')==True]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True]
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
            else:
              pass
      if(NotebookUsuario.vga == 'GeForce RTX 3060'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce RTX 3050')==True]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
          else:
            pass
      if(NotebookUsuario.vga == 'GeForce RTX 3050'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['vga_dedicaca'].str.startswith('GeForce GTX 1650')==True]
        else:
          pass
      else:
        pass
  else:
    pass
  #CHECA PREFERÊNCIA DE CPU    
  if(NotebookUsuario.cpu != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith(NotebookUsuario.cpu)==True]
    else:
      if(NotebookUsuario.cpu == 'Intel Core i9'):
        if (len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i7')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i7')==True]
        else:
          if (len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i5')==True])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i5')==True]
          else:
            pass
      elif (NotebookUsuario.cpu == 'Intel Core i7'):
        if (len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i5')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('Intel Core i5')==True]
        else:
          pass
      elif (NotebookUsuario.cpu == 'AMD Ryzen 7'):
        if (len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('AMD Ryzen 5')==True])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['processador'].str.startswith('AMD Ryzen 5')==True]
        else:
          pass
      else:
        pass
  else:
    pass
      
    #CHECA PREFERÊNCIA DE RAM  
  if(NotebookUsuario.ram != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==NotebookUsuario.ram]
    else:
      #Tratando RAM 32GB
      if(NotebookUsuario.ram == 32):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==16])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==16]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==12])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==12]
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8]
            else:
              pass

      #Tratando RAM 16GB
      elif(NotebookUsuario.ram == 16):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==12])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==12]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8]
          else:
            pass
      #Tratando RAM 12GB
      elif(NotebookUsuario.ram == 12):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ram']==8]
        else:
          pass
      else:
        pass
  else:
    pass
      
  #CHECA PREFERÊNCIA DE TELA    
  if (NotebookUsuario.tela != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao'].str.startswith(NotebookUsuario.tela)==True]
    else:
      #Tratando tela 4K
      if(NotebookUsuario.tela == '4K'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD+'])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD+']
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD'])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD']
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD'])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD']
            else:
              pass
      #Tratando tela Full HD+
      elif(NotebookUsuario.tela == 'Full HD+'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD'])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='Full HD']
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD'])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD']
          else:
            pass
      #Tratando tela Full HD
      elif(NotebookUsuario.tela == 'Full HD'):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD'])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['tela_resolucao']=='HD']
        else:
          pass
      #Tratando tela HD
      else:
        pass
  else:
    pass
  #CHECA PREFERÊNCIA DE ARMAZENAMENTO
  if (NotebookUsuario.armazenamento != 'n/a'):
    if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento])>0):
      NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']>=NotebookUsuario.armazenamento]
    else:
      if (NotebookUsuario.armazenamento == 1024):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==512])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==512]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==480])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==480]
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==256])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==256]
            else:
              if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240])>0):
                NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240]
              else:
                if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128])>0):
                  NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128]
                else:
                  if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120])>0):
                    NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120]
                  else:
                    pass
      elif (NotebookUsuario.armazenamento == 512):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==480])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==480]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==256])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==256]
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240]
            else:
              if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128])>0):
                NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128]
              else:
                if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120])>0):
                  NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120]
                else:
                  pass
      elif (NotebookUsuario.armazenamento == 256):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==240]
        else:
          if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128])>0):
            NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==128]
          else:
            if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120])>0):
              NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120]
            else:
              pass
      elif (NotebookUsuario.armazenamento == 128):
        if(len(NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120])>0):
          NotebooksFiltradosTipo = NotebooksFiltradosTipo.loc[NotebooksFiltradosTipo['ssd']==120]
        else:
          pass
      else:
        pass
  else:
    pass

  return NotebooksFiltradosTipo