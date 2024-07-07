def separar(lista):
    pares=[]
    impares=[]
    for num in lista:
        if num%2==0:
         pares.append(num)
        else:
         impares.append(num)

    pares.sort()
    impares.sort()
    return pares, impares
numeros=[10,20,5,6,3,13,9,8,7,2,1,16,12]
pares, impares= separar(numeros)
print("Los numeros pares son", pares)
print("Los numeros impares son",impares)
