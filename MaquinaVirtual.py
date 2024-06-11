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
        memoria[pos] = c
        pos += 1

print(memoria)
