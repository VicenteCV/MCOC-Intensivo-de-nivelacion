#5ta entrega
#Ciclos while
#Ejemplo 1
print 'Ejemplo 1'
Total=0
i=1
while i<10: #Luego de varirar i repetidas veces, se verifica si i sigue siendo menor a 10, si es asi, se vuelve a entrar al ciclo.
	Total+=i # Se agrega el valor de i al total 
	i+=1 # Se agrega 1 al valor de i
print Total
#Ejemplo 2
print 'Ejemplo 2'
Lista_U2=[1,2,3,14]
Total_2=0
j=0
while j<len(Lista_U2) and Lista_U2[j]<13: #dualidad de opciones para entrar al ciclo while.
	Total_2+=Lista_U2[j]
	j+=1
print Total_2
#Ejemplo 3
print 'Ejemplo 3'
total_3=0
Lista_3Chiflados=[7,6,5,4,00003,-2,1,-2,00001]
for k in Lista_3Chiflados:
	if k<=0:
		break
	total_3+=k
print total_3
#Ejemplo 4
print 'Ejemplo 4'
total_4=0
l=0
Lista_4Fantasticos=[4,3,2,1,0,-1,-2,-3,-4]
while True:
	total_4+= Lista_4Fantasticos[l]
	l+=1
	if Lista_4Fantasticos[l]<0.00000:
		break
print total_4

