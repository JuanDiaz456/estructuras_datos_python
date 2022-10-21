#EJERCICIOS LISTAS

#metodos propios

lista=[45,32,3,78]
print("lista original: ", lista)
#funcion append: añada un elemneto a la lista
lista.append(995)
lista.append(7)
print("lista despues de usar append: , lista")
# funcion sort: ordena la lista
lista.sort()
print("lista ordenada: ",lista)
#funcion reverse: invierte el orden de la lista
lista.reverse
print("lista al reves: ",lista)
#funcion extend:añade los elementos de una lista a la lista
lista_extend=[1,5,87,45]
lista.extend(lista_extend)
print("lista despues de extend: ",lista)
#funcio count: cuenta el numero de veces que aparece el elemento indicado como parametro dentro de la lista
print("numero de elementos 45: ", lista.count(45))
#funcion insert:añade el elemento pasado como un parametro a la lista en la posicion indicada tambien por parametro
lista.insert(4,111)
print("lista despues de insert: ", lista)
#funcion remove:elimina la primera ocurrencia empezando por la izquierda de la lista indicado como parametro
lista.remove(45)
print("lista despues del remove: ", lista)
#funcion index: devuelve la posicion de la primera ocurrencia de izquierda a dereche en la lista, del elemento pasado como parametro
print("posicion del elemento 111: ", lista.index(111))
#funcion pop: elimina el ultimo elemento de la lista y lo devuelve como resultado de la operacion
lista.pop()
print("lista despues de pop: ", lista)
#funcion clear:
lista.clear()
print("lista despues de clear: ", lista)
