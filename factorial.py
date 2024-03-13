#Crear una función que dado un número "n" calcular su factorial sin utilizar el operador "*"
def factorial(n):
    if n == 0:
        return 1
    else:
        loop = n
        for i in range(1, loop):
            loop -= 1
            n += sumarLoop(loop, n)
        return n

def sumarLoop(loop, number):
    if loop == 0 or loop == 1:
        return 0
    else:
        acc = 0
        for i in range(1, loop):
            acc += number
        return acc

print(factorial(5))
print(factorial(6))
                    
    

