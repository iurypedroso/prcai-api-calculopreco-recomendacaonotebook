
def coletar_melhor_cpu_performance(pref_cpu,lista_note):
  if (len(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True])>0):
    melhor_cpu_equivalente = str(lista_note.loc[lista_note['processador'].str.startswith(pref_cpu)==True].sort_values(by='processador_performance', ascending = False).head(1)['processador_performance']).split('Name')[0][5:-1].strip(" ")
    return float(melhor_cpu_equivalente)