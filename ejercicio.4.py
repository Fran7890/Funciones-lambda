#Dado un arreglo de números enteros, crea una función anónima que retorne una lista con los números pares.
numero=[1,2,3,4,5,6,7,8,9,10]
numeros_inpares=filter(lambda numero:numero%2==1,numero)
print(list(numeros_inpares))