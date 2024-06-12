#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin




   #git add .
   #git commit -m “Mensaje sobre el cambio que hicimos”
   #git push origin master




import sys


c=0
def a0(c,memoria):
   var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16) #agarro pos 1 y 2 y las paso a decimal
   #memoria[var]=int(memoria[c+3],16)
   print(f"La operacion es {memoria[c]} el valor que se va a guardar en la posicion {var} es {memoria[c+3]}")
   c=c+4
   return memoria,c
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
def b0():
   pass
def b1():
   pass
def b2():
   pass
def c0():
   pass
def c1():
   pass
def c2():
   pass
def c3():
   pass


def d0(memoria,c): #Suma
    var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
    var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
    #suma=memoria[var1]+memoria[var2]
    #a=may255(suma)
    #memoria[var2]=a
    print(f"La operacion es {memoria[c]} y se va a guardar en la posicion {var1 + var2} el valor de {var2}")
    c=c+5
    return memoria,c




def d1(memoria,c): #Resta
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   #suma=memoria[var2]-memoria[var1]
   #memoria[var2]=suma


   return memoria,c




def d2(memoria,c): #Modulo
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   suma=memoria[var1]%memoria[var2]
   memoria[var2]=suma
   return memoria


def f0(c,memoria):
   with open('mem.dump','wb') as d:
       memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
       d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump
       c =c+1
       return memoria,c
def f1(c, memoria):
   c=c+1
   return memoria,c
funciones={ #si "a0" esta en el vevtor operaciones va a hacer tal funcion que esta determinada aca:
   "a0":a0,
   "a1":a1,
   "a2":a2,
   "a3":a3,
   "a4":a4,
   "a5":a5,
   "a6":a6,
   "a7":a7,
   "b0":b0,
   "b1":b1,
   "c0":c0,
   "c1":c1,
   "c2":c2,
   "c3":c3,
   "d0":d0,
   "d1":d1,
   "d2":d2,
   "f0":f0,
   "f1":f1,
   
}


def extraerOp(valor): #a0 d1 f4 10 ejemplo
   return hex(valor)[2:len(hex(valor))] #le saca la x al hexa


def may255(valor): #Cuando usemos valores mayores a 255
   return bin(valor)[len(bin(valor))-8:len(bin(valor))]


# Definimos el Tamaño de la memoria
# Inicializar la memoria con enteros en lugar de cadenas
memoria = [0] * 35#vector memoria


#El programa comenzara comparando la primer direccion con un VECTOR con todas las operaciones, si se encuentra la misma, lo que hacemos sera mandarlo a esa funcion,
#Esa funcion lo que hara es que tendra un valor que retornara que sera el valor que aumentara en la memoria para seguir leyendo los programas,
#Luego lo que hara es depende el OP code,  sera ver los parametros y luego realizar lo que tenga que hacer esa operacion.


operaciones=["a0","a1","a2","a3","a4","a5","a6","a7","b0","b1","c0","c1","c2","c3","d0","d1","d2","f0","f1"]


# Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
   code = programa.read()
 
#print(code)


#for i in range(len(code)):
   #memoria[i]=extraerOp(code[i])
   
#print(memoria)


# Recorremos y colocamos cada codigo en una posicion de memoria
pos = 0
for i in code:
    if pos < 1025:
       memoria[pos] = i
       pos += 1


while c < len(memoria):
    a = extraerOp(memoria[c])
    #print(memoria[c])
    if a in funciones:
      memoria, c = funciones[a]( c, memoria)
      #print(c)
    else:
        c += 1
