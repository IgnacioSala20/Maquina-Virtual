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
def a0():
    print("Hola Mundo")
def a1():
    pass
def a2():
    pass
def a3():
    pass
def a4():
    pass
def a5():
    pass
def a6():
    pass
def a7():
    pass
funciones={
    "a0":a0,
    "a1":a0,
    "a2":a0,
    "a3":a0,
    "a4":a0,
    "a5":a0,
    "a6":a0,
    "a7":a0,
}

def extraerOp(valor):
    print(hex(memoria[i])[2:len(hex(memoria[i]))])
    return hex(memoria[i])[2:len(hex(memoria[i]))]
# Definimos el Tamaño de la memoria
# Inicializar la memoria con enteros en lugar de cadenas
memoria = [0] * 10

operaciones=["a0","a1","a2","a3","a4","a5","a6","a7"]

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
for i in range(len(memoria)):
    a=extraerOp(memoria[i])
    if a in operaciones:
        funciones[a]()
    

dump_mem(memoria)
