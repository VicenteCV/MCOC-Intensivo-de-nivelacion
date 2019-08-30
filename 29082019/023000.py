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
#Ejemplo 3
print 'Ejemplo 3'
e=8 #Int
print type(e)
f=(9,7) #Tupla
print type(f)
#Operaciones con arrays
print np.sin(a)
print np.exp(a)
print np.log(a)
#Ejemplo 4
print 'Ejemplo 4'
g=np.array([2,3,2,3,2,3],dtype='float64')
print g
h=np.array([[10,13,11],[20,22,21]]) #Se crea array de lsitas de dos dimensiones
print h
print h.shape #primera dimensions es vertical, segunda es horizontal
print h.T #transposicion de array
print h.size #cantidad de elementos
print h[0,0] #item de posicion 0,0
print h[0] #primera lista de array
print g[2:6] #Arroja array entre 2 y 6
print g[1:-2] #Saca 1 de desde la izquierda y cuando se usa negativo se empieza desde la derecha 
print g[:3] #no se pone primer numero y se asume que se empieza desde el principio
print g[::2]
i=np.array([[0,1,2,3,4,5],[10,11,12,13,14,15],[20,21,22,23,24,25],[30,31,32,33,34,35],[40,41,42,43,44,45]])
print i
print i[0,3:5] 
print i[4:,4:] #imprime en ambas dimensiones desde el 4 hasta todo el resto
print i[:,2] #imprime todo en primera dimension en la columna 2 de la segunda dimension
print i[2::2,::2]#desde segunda fila hasta el final, cada 2. y desde 
#Ejemplo 5
print 'Ejemplo 5'
j=np.arange(25).reshape(5,5)
print j
naranjos = j[:,1::2]
print naranjos
azules =j[1::2,:3:2]
print azules
amarillo=j[-1,:] #-1 implica la ultima fila
print amarillo
#todos mostraron lo solicitado
print naranjos.flags
#Ejemplo 6
print 'Ejemplo 6'
k=np.array([3,-1,-2,4,-6,8])
print k
print k<0
negativos=k<0
print k[negativos]
k[k<0]=0
print k

#Binary operators, and, or not
#Bitwise operators
#& para and,| para or,~ para not y ^para xor
print((k>3) & (k<8))
print np.nonzero(negativos) #entrega las posiciones para los valores True 
#False y 0 son practicamente lo mismo y true y 1 son practicamente lo mismo
k.sort() # se ordenan de menor a mayor
print k
print k.flags.owndata
corte=k[[1,5]]
print corte
print corte.flags.owndata
#Ejemplo 6
print 'Ejemplo 6'
l=np.arange(25).reshape(5,5)
print l
divisibles3=l%3
print divisibles3
div3=l%3==0
print div3
print l[div3]
#Ejemplo 7
print 'Ejemplo 7'
#En creacion de arrays, la utlima dimension  siempre son las columnas
#Para hacer operaciones entre arrays estos deben ser del mismo tamano
#operadores matematicos se aplican elemento por elemento 
#operaciones que analizan arrays se aplican a todo el array excepto que se especifique alguna fila o oclumna
m=np.arange(25).reshape(5,5)
print m
print m.sum() #suma todos los valores del array
print m.sum(axis=0)
print m.sum(axis=-1)

#La ultima parte del video se realizo en los videos de los dias anteriores





