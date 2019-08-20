#Que son las funciones
#Comentarios
#Utilizados para generar comentarios del codigo
#Ejemplo 1
print 'Ejemplo 1'
def Funcion1():
	print 'AHHH'
	print 'Ahhhhhaaahhh'
print 'esto es fuera de la funcion'
Funcion1()
#Ejemplo 2
print 'Ejemplo 2'
def  Funcion2(x):
	return 3*x
a= Funcion2(5)
b= Funcion2(7)
print a
print b
#Ejemplo 3
print 'Ejemplo 3'
def Funcion3(x,y):
	return x**y
c= Funcion3(2,3)
print c
#Ejemplo 4
print 'Ejemplo 4'
def Funcion4(x):
	print x
	print 'Holaaaa'
Funcion4(8)
#Calculador de IMC
print 'Ejemplo 5: CalculadorIMC'
Nombre1= 'VCV'
Altura_metros1= 1.73
Peso_Kg1= 84

Nombre2= 'BCV'
Altura_metros2= 1.83
Peso_Kg2= 82

Nombre3= 'NCG'
Altura_metros3= 1.80
Peso_Kg3= 98

def CalculadorIMC(nombre,altura, peso):
	IMC=peso/(altura**2)
	print nombre + ' Tiene un IMC de: ' , IMC
	print 'Por lo tanto....'
	if IMC<25:
		return nombre + ' No Tiene sobrepeso'
	else:
		return nombre + ' Tiene sobrepeso'
Resultado1=CalculadorIMC(Nombre1,Altura_metros1,Peso_Kg1)
print Resultado1
Resultado2=CalculadorIMC(Nombre2,Altura_metros2,Peso_Kg2)
print Resultado2
Resultado3=CalculadorIMC(Nombre3,Altura_metros3,Peso_Kg3)
print Resultado3
