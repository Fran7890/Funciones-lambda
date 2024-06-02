#Escribe una función anónima que calcule el factorial dado un número entero

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)
print(factorial(3)) 
