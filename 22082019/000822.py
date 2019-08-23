#4ta Entrega
#Ciclo For
#Ejemplo 1
print 'Ejemplo 1'
a=['Bananaaaa!!!','Bee do Bee do Bee do','Tu le bella comme le papaya']
for i in a: #Ciclo for que recorre lista
	print i #Al recorrer la lista elemento, por elemento, estos se imprimen durante cada ciclo.
#Ejemplo 2
print 'Ejemplo 2'
print 'Bienvenidos a la historia del club mas grande de Chile. UCDC'
b=[1997,2002,2005,2010,2016,2016,2018]
total=0
for j in b:
	total=total + j
print total
#Ejemplo 3
range(1,5) #Rango de valores del 1 al 5 sin contar el 3
c=list(range(1,5)) #Se crea una lista con los valores en ese rango
print c
total2=0
for k in range(1,5):
	print k
	total2+=k #Atajo para sumar k al valor antiguo de la variable
print total2
#Ejemplo 4
print 'Ejemplo 4'
print list(range(1,9))
total3=0
for l in range(1,9):
	if l%3==0:
		total3+=l
print total3
