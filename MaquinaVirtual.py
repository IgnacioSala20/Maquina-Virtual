#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin

    #git add .
    #git commit -m “Mensaje sobre el cambio que hicimos”
    #git push origin master



#El programa comenzara comparando la primer direccion con un VECTOR con todas las operaciones, si se encuentra la misma, lo que hacemos sera mandarlo a esa funcion,
#Esa funcion lo que hara es que tendra un valor que retornara que sera el valor que aumentara en la memoria para seguir leyendo los programas,
#Luego lo que hara es depende el OP code,  sera ver los parametros y luego realizar lo que tenga que hacer esa operacion.

import sys

#Definimos el Tamaño de la memoria
memoria = [0] * 10

def dump_mem(): #Almacenamos todo el contenido de memoria en un archivo llamado mem.dump
    with open('mem.dump', 'wb') as d:
        maux = [0, 0, 0, 160]
        for m in maux:
            d.write(bytes([m]))
            
#Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
    code = programa.read()

#Recorremos y colocamos cada codigo en una posicion de memoria
pos = 0
for c in code:
    if pos < 1025:
        memoria[pos] = hex(c)
        pos += 1

print(memoria)
