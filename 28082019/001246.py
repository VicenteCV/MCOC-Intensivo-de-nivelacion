#8va entrega
#Arrays con numpy
#Ejmeplo 1
print 'Ejmeplo 1'
import numpy as np
a=np.array([4,3,2]) #Crea array con lista introducida
print a
b=np.arange(1,12,2) #Crea array desde 1 a 12 con pasos de 2
print b
c=np.linspace(1,12,6) #Crea array de 6 elementos, entre 1 y 12 con valores float espaciado de forma pareja
print c
d=c.reshape(3,2) #Cambia la forma del array. 3 filas de 2 elementos cada una
print d
e=d.size #arroja el tamano o cantidad de elementos del array
print e
#Ejemplo 2
print 'Ejemplo 2'
f=np.array([(1,2,3),(6,5,4)])#Array de dos dimensiones
print f
print b<4 #Arroja entre verdadero y falso todos los valores que son menores de 4
print f*4 #Se multiplican todos los elementos del array por 4
g=np.zeros((4,3)) #Array de ceros con dimensiones especificadas
print g
print g.dtype #Arroja el tipo de dato del array
h=np.ones((3,3)) #Array de unos
print h
i=np.array([4,3,2],dtype=np.int16) #Se crea array con datos de tipo integers 16 para usar menos memoria
print i
print i.itemsize #Arroja cantidad de bytes que utiliza cada elemento
