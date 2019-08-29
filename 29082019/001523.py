#9na entrega
#Tutorial completo de numpy
#Ejemplo 1
print 'Ejemplo 1'
a=[1,2,3]
b=[5,4,3]
c=a+b #Se crea llista conteniendo ambas listas a y b
print c
salida=[]
for i,j in zip(a,b): #Recorre ambas listas simultaneamente
	salida.append(i+j)
print salida
#Ejemplo 2
print 'Ejemplo 2'
import numpy as np
d=list(range(100000))
d_array=np.array(d)
a=np.array(a)
b=np.array(b)
c=a+b #Se suman valores de los arrays
print c
c=a*b
print c
print a.dtype
print type(a)
print a.ndim
print a.shape
print a.itemsize




