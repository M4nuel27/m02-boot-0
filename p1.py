def sumaTodos(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += i
        
    return resultado
    
print(sumaTodos(100))


def sumaTodoslosCuadrados(limitTo):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += i*i
        
    return resultado
    
print(sumaTodos(100))
print(sumaTodosolosCuadrados(3))