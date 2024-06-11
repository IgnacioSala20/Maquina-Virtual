#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin

    #git add .
    #git commit -m “Mensaje sobre el cambio que hicimos”
    #git push origin master

import sys
def a0(instrucciones,i,memoria):
    var=int(instrucciones[i+1]+instrucciones[i+2],16) #agarro pos 1 y 2 y las paso a decimal
    var=9
    memoria[var]=int(instrucciones[i+3])
    return memoria
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
funciones={ #si "a0" esta en el vevtor operaciones va a hacer tal funcion que esta determinada aca:
    "a0":a0,
    "a1":a1,
    "a2":a2,
    "a3":a3,
    "a4":a4,
    "a5":a5,
    "a6":a6,
    "a7":a7,
}

def extraerOp(valor): #a0 d1 f4 10 ejemplo
    return hex(valor)[2:len(hex(valor))] #le saca la x al hexa

def may255(valor): #Cuando usemos valores mayores a 255
    return bin(valor)[len(bin(valor))-8:len(bin(valor))]

# Definimos el Tamaño de la memoria
# Inicializar la memoria con enteros en lugar de cadenas
memoria = [0] * 10 #vector memoria
#El programa comenzara comparando la primer direccion con un VECTOR con todas las operaciones, si se encuentra la misma, lo que hacemos sera mandarlo a esa funcion,
#Esa funcion lo que hara es que tendra un valor que retornara que sera el valor que aumentara en la memoria para seguir leyendo los programas,
#Luego lo que hara es depende el OP code,  sera ver los parametros y luego realizar lo que tenga que hacer esa operacion.

operaciones=["a0","a1","a2","a3","a4","a5","a6","a7"]

def dump_mem(memoria):
    with open('mem.dump','wb') as d:
        memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
        d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump

# Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
    code = programa.read()
    
print(code)

intrucciones=[int for ind0 in range(len(code))]

for i in range(len(code)):
    intrucciones[i]=extraerOp(code[i])
print(intrucciones)


# Recorremos y colocamos cada codigo en una posicion de memoria
pos = 0
for c in code:
    if pos < 1025:
        memoria[pos] = c
        pos += 1
print(memoria)  

for i in range(len(memoria)): #lee memoria
    a=extraerOp(memoria[i]) #
    if a in operaciones: #si esta en el vector operaciones (compara)
        b=funciones[a](intrucciones,i,memoria)
        print(b)

print()

#for i in range(len(memoria)):
 #   print(memoria[i])

dump_mem(memoria)
