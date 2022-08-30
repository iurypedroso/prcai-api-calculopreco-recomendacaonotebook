def correcao_valor_avista_str(valor_avista):
  a = valor_avista.split('Name')[0][5:-1].strip(" ")
  b = '{:,.2f}'.format(float(a))
  c = b.replace(',','v')
  d = c.replace('.',',')
  e = d.replace('v','.')
  return (str('R$'+e))

def correcao_valor_avista_float(valor_avista):
  a = valor_avista.split('Name')[0][5:-1].strip(" ")
  return (float(a))
  
def correcao_valor_aprazo_str(valor_aprazo):
  f = valor_aprazo.split('Name')[0][5:-1].strip(" ")
  g = '{:,.2f}'.format(float(f))
  h = g.replace(',','v')
  i = h.replace('.',',')
  j = i.replace('v','.')
  return (str('R$'+j))

def correcao_valor_aprazo_float(valor_aprazo):
  f = valor_aprazo.split('Name')[0][5:-1].strip(" ")
  return (float(f))