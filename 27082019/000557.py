#7ma entrega
#Numpy
#Ejemplo 1
print 'Ejemplo 1'
import numpy as np
a=np.zeros(4) #Se crea un array de tamano 4
print a
b=type(a) #Arroja el tipo de variable de a
print b
c=type(a[0]) #Arroja el tipo de variable del primer valor del array 
print c
d=a.shape #Arroja la forma del array
print d
#Ejemplo 2
e=np.zeros(9)
print e
e.shape=(9,1) #Se cambia forma de array
print e
f=np.empty(4) #Crea un array con 4 ceros
print f
g=np.linspace(3,12,4) #Crea array que empieza en 3, termina en 12 y tiene 4 elementos
print g
h=np.array([1,2,3,4,5,9])#Crea array con lista
print h
listita=[9,5,4,3,2,1]
i=np.array(listita)#Crea un array en base a una lista ya creada
print i
listita2=[[6,4,2],[7,5,3]]
j=np.array(listita2) #Se crea array con lista de dos dimensiones
print j
#Ejemplo 3
print 'Ejemplo 3'
k=np.random.randint(12,size=5)#Se crea un array con valores al azar hasta el 12 de tamano 5
print k
print k[0:3]#Imprime array de los 3 primeros valores del array llamado
print k[-1]#Ultimo valor de array

