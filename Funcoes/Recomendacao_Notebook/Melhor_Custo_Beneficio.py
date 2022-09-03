def custo_beneficio(tipo_pagamento):
  from Calculo_Metricas_Notebooks import resul_pesq_usuario

  if (tipo_pagamento == 'preco_avista'):
    resultado_custo_beneficio = resul_pesq_usuario.sort_values(by='beneficio_avista', ascending=True)
  else:
    resultado_custo_beneficio = resul_pesq_usuario.sort_values(by='beneficio_aprazo', ascending=True)
  
  return resultado_custo_beneficio.head(1)