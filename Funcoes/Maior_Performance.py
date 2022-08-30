def maior_performance():
  from ConsultaPrecoNotebook import resul_pesq_usuario
  resultado_maior_performance = resul_pesq_usuario.sort_values(by='performance', ascending=False)
  return resultado_maior_performance.head(1)
