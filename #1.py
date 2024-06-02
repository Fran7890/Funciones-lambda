#1. Crea una función anónima (lambda) que calcule el promedio de un arreglo de números entero
# Definir la función lambda
promedio = lambda arr: sum(arr) / len(arr) if arr else float('nan')

# Usar la función lambda con un arreglo de números enteros
numeros = [8, 2, 6, 4, 5]
resultado = promedio(numeros)
print(f"El promedio de {numeros} es {resultado}")

# Usar la función lambda con un arreglo vacío
numeros_vacios = []
resultado_vacio = promedio(numeros_vacios)
print(f"El promedio de un arreglo vacío es {resultado_vacio}")
