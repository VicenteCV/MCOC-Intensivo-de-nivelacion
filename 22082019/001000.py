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
b=[1949,1954,1961,1966,1984,1987,1997,2002,2005,2010,2016,2016,2018]
print 'Club glorioso, con un basto palmares de campeonatos nacionales, obentidos en los anios:'
total=0
for j in b:
	print j, #Impresion de todos los valores dentro de la lista en una linea.
	total=total + j
print
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
	if l%3==0: #Modulo que entrega resto de division entre l y 3
		total3+=l
print total3
#Ejemplo 5
print 'Ejemplo 5'
lista_de_multiplos=[]
for m in range(1,100):
	if m%3==0 :
		lista_de_multiplos.append(m)
	elif m%5==0:
		lista_de_multiplos.append(m)
#Ciclo for en rango 1 hasta menos de 100 que recopila valores multiplos de 3 y de 5 pero no repite aquellos numeros que son multiplos de ambos.
sumatoria=0
for n in lista_de_multiplos:
	sumatoria+=n
#Ciclo for que suma numeros seleccionados anteriormente que fueron depositados en una lista.
print lista_de_multiplos
print sumatoria
#Impresion de lista y de sumatoria posterior.