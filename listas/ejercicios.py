#EJERCICIOS LISTAS

#ejercicios manipulacion

#1.consiste en la definicion de una llista con elementos de diferentes tipos y en mostrarla por pantalla tanto entera como por elementos accediendo a la posicion que ocupa dentro de la lista
lista= ["python", "guanenta", 2022, "libro", 3]
print(lista)
print(lista[0])
print(lista[2])

#2.consiste en el uso del operador + para realiar uniones de listas. Ademas utilizar la funcion len para conocer el numero de elementos que componen la lista
lista1=["camiseta","pantalon","zapatillas"]
lista2=["abrigo","jersey","sudadera","calcetines"]
print("numero de elementos: lista1:", len(lista1))
print("lista1", lista1)
print("numero de elementos: lista2:", len(lista2))
print("lista2", lista2)
lista_concatenada= lista1+lista2
print("lista_concatenada", lista_concatenada)

#3.añadir elementos a la lista de diferentes formas
lista=["camiseta","pantalon","zapatillas"]
print(lista)
lista=lista+ ["abrigo"]
print(lista)
lista=lista+ ["jersey", "sudadera"]
print(lista)
lista=lista+ ["calcetines"]+["bufanda"]
print(lista)

#5.onectar elementos de una lista y borrar elementos de la misma
lista=["camiseta","pantalon","zapatillas"]
print(lista)
lista[1]="cazadora"
print(lista)
del lista[0]
print(lista)