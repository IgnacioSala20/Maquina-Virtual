#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin

    #git add .
    #git commit -m “Mensaje sobre el cambio que hicimos”
    #git push origin master



#El programa comenzara comparando la primer direccion con un VECTOR con todas las operaciones, si se encuentra la misma, lo que hacemos sera mandarlo a esa funcion,
#Esa funcion lo que hara es que tendra un valor que retornara que sera el valor que aumentara en la memoria para seguir leyendo los programas,
#Luego lo que hara es depende el OP code,  sera ver los parametros y luego realizar lo que tenga que hacer esa operacion.

#

import sys

# Definimos el Tamaño de la memoria
# Inicializar la memoria con enteros en lugar de cadenas
memoria = [0] * 65535


def dump_mem(memoria):
    with open('mem.dump','wb') as d:
        memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
        d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump

# Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
    code = programa.read()

# Recorremos y colocamos cada codigo en una posicion de memoria
pos = 0
for c in code:
    if pos < 1025:
        memoria[pos] = c
        pos += 1

dump_mem(memoria)
