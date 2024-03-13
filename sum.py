# Crear una función que dado dos números "a" y "b" devolver la suma de ambos sin utilizar el operador "+"

def sumar(a, b):
    while (b != 0):
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a


num1 = int(input('Ingresar el 1er número: '))
num2 = int(input('Ingresar el 2do número: '))

print(sumar(num1, num2))
