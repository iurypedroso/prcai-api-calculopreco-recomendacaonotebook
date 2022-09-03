
def menor_valor(tipo_pagamento):
  from Calculo_Metricas_Notebooks import resul_pesq_usuario
  global result_filtro_tipo_recom
  
  resultado_menor_valor = resul_pesq_usuario.sort_values(by=tipo_pagamento, ascending=True)
  return resultado_menor_valor.head(1)