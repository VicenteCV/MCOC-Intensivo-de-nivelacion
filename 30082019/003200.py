#10ma entrega
#Matplotlib
#Ejemplo 1
print 'Ejemplo 1'
from matplotlib import pyplot as plt
import numpy as np
#print plt.style.available
plt.style.use('grayscale')
a=np.arange(25,36)
b=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(a,b,color='#444444',marker='.',label='Todos los desarrolladores') #Se detallan los ejes, el color y tipo de linea, el marcador para cada punto y un label para la serie de datos
c=[45372,48872,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(a,c,color='#5a7d9a',marker='o',linewidth=4,label='Python') #Se detallan los colores, markers y lineas de forma distinta para diferenciar datos
#etiquetas de color representan forma de escribir codigos de colores
#Linewidth engrosa la linea de datos
d=[37810,43515,46823,49293,53437,56373,62375,66674,68745,68746,74583]
plt.plot(a,d,color='#222222',marker='x',label='Java')
plt.xlabel('Edad')
plt.ylabel('Salario medio')
plt.title('Salario medio en dolares por edad')
plt.legend()# Cumple la misma funcion que cuando se utiliza label dentro del ploteo 
plt.grid(True) #Para poner grilla
plt.tight_layout() #ajusta automaticamente parametros
plt.savefig('Grafico.png',)
plt.show()




























