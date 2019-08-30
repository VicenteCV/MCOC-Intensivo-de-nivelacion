#10ma entrega
#Matplotlib
#Ejemplo 1
print 'Ejemplo 1'
from matplotlib import pyplot as plt
import numpy as np

a=np.arange(25,36)
b=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(a,b,'k--',marker='.',label='Todos los desarrolladores') #Se detallan los ejes, el color y tipo de linea, el marcador para cada punto y un label para la serie de datos
c=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(a,c,'b-',marker='o',label='Python') #Se detallan los colores, markers y lineas de forma distinta para diferenciar datos
plt.xlabel('Edad')
plt.ylabel('Salario medio')
plt.title('Salario medio en dolares por edad')
plt.legend(['Todos los desarrolladores','Python'])# Cumple la misma funcion que cuando se utiliza label dentro del ploteo 
plt.show()




























