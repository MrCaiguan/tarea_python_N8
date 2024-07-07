def sumatoria(numero):
  if numero==0:
    return 0
  else:
    return numero+sumatoria(numero-1)

numero=10
resultado=sumatoria(numero)
print("La sumatoria es", resultado)