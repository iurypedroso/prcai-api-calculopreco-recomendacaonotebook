def maior_performance():
  from Calculo_Metricas_Notebooks import resul_pesq_usuario
  resultado_maior_performance = resul_pesq_usuario.sort_values(by='performance', ascending=False)
  return resultado_maior_performance.head(1)
