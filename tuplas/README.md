# TUPLAS

- En ese apartado vamos a hablar sobre los tipos de tuplas, que son un conjunto ordenado e inmutable de elementos. La diferencia con las listas reside en que en las listas puedes manipular los elementos y en las tuplas no, es decir, no es posible añadir/eliminar elementos, modificarlos, etc. Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos, por ejemplo una tupla puede estar compuesta por cadenas de texto, por números enteros,etc.
- las tuplas en python se representan por una serie de elementos separados por comas y delimitados entre parentesis, veamos un ejemplo de tupla:
("casa","2",345,"perro",99)
- la tupla estaria compuesta por cinco elementos, las cadenas de texto"casa","2" y "perro" y los numeros enteros 345 y 99
- Al igual que en las listas, los elementos de las tuplas ocupan posiciones concretas, y mediante esa posicion que ocupan podemos acceder directamente a los elementos. En la siguiente tabla te mostramos la relacion de cada elemento con la posicion que ocupa en la tupla:

|"Elemento"|"posicion"|
|--------|----------|
|"casa"|0|
|"2"|1|
|345|2|
|"perro"|3|
|99|4|

- Tanto en las listas como en las tuplas, los elementos empiezan por la posicion 0, no por la 1 como pareceria lo obvio. tenlo en cuenta cuando utilices tuplas.