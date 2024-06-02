#Utiliza una función lambda para elevar al cuadrado cada elemento de una lista de números.
numeros=[2,4,5,7,9,12]
numero_cuadrado=list(map(lambda x:x**2,numeros))
print(list(numero_cuadrado))