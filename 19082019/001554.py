#If else statements
#Inicio de ejemplos
print 'Ejemplo 1'
a=6
b=7
if a <b:
	print 'a es menor que b'
	print 'a es definitivamente menor que b'
print 'No estoy seguro que a sea menor que b'
#ejemplo 2
print 'Ejemplo 2'
c=5
d=4
if c<d:
	print 'c es menor que d'
else:
	print 'c NO es menor que d'
print 'Fuera del ciclo if'
#Ejemplo 3
print 'Ejemplo 3'
e=19
f=8
if e<f:
	print 'e es menor que f'
elif e==f:
	print 'e es igual a f'
elif e>f+10:
	print 'e es mas grande que f por mas de 10'
else:
	print 'e es mayor que f'
#Ejemplo 4
print 'Ejemplo 4'
g=7
h=8
if g<h:
	print 'g es menor que h'
else:
	if g==h:
		print 'g es igual a h'
	else:
		print 'g is mayor que h'
