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