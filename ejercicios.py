def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n3 and n2 > n1:
        return n2
    else:
        return n3

#Definir una función que calcule la longitud de una lista o una cadena dada.
def calculaLongitud(array):
    acumulador = 0
    for i in array:
        acumulador += 1

    return acumulador

#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
def isVocal(var1):
    vocales = ['a','e','i','o','u']
    var2 = var1.lower()
    if var2 in vocales:
        return True
    else:
        return False

#Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
def sum(popo):
    acumulador = 0
    for i in popo:
        acumulador += i

    return acumulador

def multi(popo):
    acumulador = 1
    for i in popo:
        acumulador *= i

    return acumulador

#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
def inversa(cadena):
    #invertir = cadena[::-1]
    #print(invertir)
    lista = [char for char in cadena]
    lista.reverse()
    cadena = ''.join(lista)
    print(cadena)

#Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def palindromo(cadena):
    lista = [char for char in cadena]
    lista.reverse()
    cadena2 = ''.join(lista)
    if cadena == cadena2:
        return True
    else:
        return False

#Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
def superposicion(array1, array2):
    acumuladorsi = 0
    for i in array1:
        for j in array2:
            if i in array2 or j in array1:
                acumuladorsi += 1
            else:
                pass
            print(f"i = {i} ---- j = {j}")

    if acumuladorsi > 0:
        return True
    else:
        return False

#Definir una funcion factorial() que saque el factorial de un numero
def factorial(num):
    acumulador = 1
    for i in range(1,num+1):
        acumulador *= i

    return acumulador
    
    

if __name__ == '__main__':
    
    #lista = [8,9,8,7,2,1,3,8,8]
    #print(calculaLongitud(lista))
    #variable = input("Digita el caracter a comparar: ")
    #print(isVocal(variable))
    #print(sum(lista))
    #print(multi(lista))
    #inversa("estoy probando")
    #print(palindromo("ana"))
    #ar1 = ['t','y','u','i','o','p']
    #ar2 = ['a','s','d','f','g']
    #print(superposicion(ar1,ar2))
    #print(factorial(4))

    
