#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin
#python MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin




   #git add .
   #git commit -m “Mensaje sobre el cambio que hicimos”
   #git push origin master


import sys
c=100
def a0(c,memoria):
   var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16) #agarro pos 1 y 2 y las paso a decimal
   memoria[var]=int(extraerOp(memoria[c+3]),16)
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
def c1(c,memoria):
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   conjuncion = memoria[var1] and memoria[var2]
   memoria[var2]=conjuncion
def c2(c,memoria):
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   disyuncion = memoria[var1] or memoria[var2]
   memoria[var2]=disyuncion

def c3():
   pass

def d0(c,memoria): #Suma
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   suma=memoria[var1]+memoria[var2]
   a=may255(suma)
   memoria[var2]=a
   c=c+5
   return memoria,c

def d1(c,memoria): #Resta
   var1=int(memoria[c+1]+memoria[c+2],16)
   var2=int(memoria[c+3]+memoria[c+4],16)
   suma=memoria[var2]-memoria[var1]
   memoria[var2]=suma
   return memoria,c

def d2(c,memoria): #Modulo
   var1=int(memoria[c+1]+memoria[c+2],16)
   var2=int(memoria[c+3]+memoria[c+4],16)
   suma=memoria[var1]%memoria[var2]
   memoria[var2]=suma
   return memoria

def f0(c,memoria):
   c =c+1
   with open('mem.dump','wb') as d:
       memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
       d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump
       return memoria,c

def f1(c, memoria):
   c=len(memoria)+1
   print("Finalizado")
   return memoria,c

funciones={ #si "a0" esta en el vevtor operaciones va a hacer tal funcion que esta determinada aca:
   "0xa0":a0,
   "0xa1":a1,
   "0xa2":a2,
   "0xa3":a3,
   "0xa4":a4,
   "0xa5":a5,
   "0xa6":a6,
   "0xa7":a7,
   "0xb0":b0,
   "0xb1":b1,
   "0xc0":c0,
   "0xc1":c1,
   "0xc2":c2,
   "0xc3":c3,
   "0xd0":d0,
   "0xd1":d1,
   "0xd2":d2,
   "0xf":f0, #Falta completar y que quede f0, CORREGIR FUNCION
   "0xf1":f1,
}
def extraerOp(valor): #a0 d1 f4 10 ejemplo
   return hex(valor)[2:len(hex(valor))] #le saca la x al hexa

def may255(valor): #Cuando usemos valores mayores a 255
   return bin(valor)[len(bin(valor))-8:len(bin(valor))]
   

memoria = [0] * 65535#vector memoria


operaciones=["a0","a1","a2","a3","a4","a5","a6","a7","b0","b1","c0","c1","c2","c3","d0","d1","d2","f0","f1"]

# Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
   code = programa.read()

# Recorremos y colocamos cada codigo en una posicion de memoria
pos = 100
for i in code:
   if pos < 1025:
       memoria[pos]=i
       pos += 1

while c < len(memoria):
    a = hex(memoria[c])
    if a in funciones: # compara con funciones
        memoria, c =funciones[a](c,memoria)   
        
    else:
        c += 1
