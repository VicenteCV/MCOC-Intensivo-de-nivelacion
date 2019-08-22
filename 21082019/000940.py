#3ra Entrega
#Listas
#Ejemplo 1
print 'Ejemplo 1'
a=[3,10,-1]
print a
a.append(1)
print a
a.append('holaa')
print a
a.append([1,2])
print a
a.pop()
print a
a.pop()
print a
print a[0]
print a[3]
a[0]=100
print(a)
#Ejemplo 2
print 'Ejemplo 2'
b=['Bananaaaa!!!','Bee do Bee do Bee do','Tu le bella comme le papaya']
print b
temporal=b[0] # variable que guarda primer valor de lista
b[0]=b[1] #cambio de primer valor de lista por segundo
b[1]=temporal #cambio de segundo valor de lista por variable guardada que representa antiguo primer valor de lista
print b
b[0],b[1]=b[1],b[0] # atajo para hacer cambio de valores internos en lista
print b