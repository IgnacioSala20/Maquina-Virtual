#Es para ejecutar desde terminal
#python3 MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin
#python MaquinaVirtual.py /home/ignacio/PruebasComandos/Maquina-Virtual/prog1.bin

  #git add .
  #git commit -m “Mensaje sobre el cambio que hicimos”
  #git push origin master
 
  #xxd -s 53744 -l 128 /home/ignacio/PruebasComandos/Maquina-Virtual/mem.dump Para mostrar el volcado de memoria desde 53744 a la longitud 128
 
  #xxd /home/ignacio/PruebasComandos/Maquina-Virtual/mem.dump Muestra todo el mem.dump en linux
import sys
xp=0
def xor(cadena1,cadena2):
  return cadena1 ^ cadena2
def negar(cadena):
   var=str()
   for i in range(len(cadena)):
       if cadena[i]=="1":
           var=var+"0"
       elif cadena[i]=="0":
           var=var+"1"
   return var

c=100
def a0(c,memoria):
  q=extraerOp(memoria[c+1])
  w=str(extraerOp(memoria[c+2]))
  if len(q)<2:
     q="0"+q
  elif len(w)<2:
     w="0"+w
  var=int(q+w,16)
  memoria[var]=int(extraerOp(memoria[c+3]),16)
  c=c+4
  return memoria,c
def a1(c, memoria):
  var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  N1=str(c)
  if c<255:
     N1="0"+str(N1)
  else:
     N1=str(may255(c))
     if int(N1)<100:
        N1="00"+str(N1)
     else:
        N1="0"+str(N1)
  memoria[var]=int(N1[0:2])
  memoria[var+1]=int(N1[2:len(N1)])
  c=c+3
  return memoria,c
def a2():
  pass
def a3(c,memoria):
  var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  memoria[var2]=memoria[var]
  memoria[var]=0
  c=c+5
  return memoria,c
def a4(c, memoria):
  global xp
  q=extraerOp(memoria[c+1])
  w=str(extraerOp(memoria[c+2]))
  if len(q)<2:
     q="0"+q
  elif len(w)<2:
     w="0"+w
  var=int(q+w,16)
  if xp>1024 and xp<len(memoria):
    memoria[xp]=memoria[var]
  else:
      print("Error")
  c=c+2
  return memoria, c


def a5(c,memoria):
  global xp
  var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  if xp>1024 and xp<len(memoria):
    memoria[var]=memoria[xp]
    memoria[xp]=0
  else:
     print("Error")
     c=len(memoria)
  c=c+2
  return memoria, c
def a6(c,memoria):
  global xp
  var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  N1=str(xp)
  if xp<255:
     N1="0"+str(N1)
  else:
     N1=str(may255(xp))
     if int(N1)<100:
        N1="00"+str(N1)
     else:
        N1="0"+str(N1)
  memoria[var]=int(N1[0:2])
  memoria[var+1]=int(N1[2:len(N1)])
  c=c+3
  return memoria,c
def a7(c, memoria):
   global xp
   var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   q=extraerOp(memoria[var])
   w=str(extraerOp(memoria[var+1]))
   if len(q)<2:
      q="0"+q
   elif len(w)<2:
      w="0"+w
   total=int(q+w,16)
   xp=total
   c=c+3
   return memoria, c

def b0():
   var=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
   if memoria[var2]==0:
      c=var
   else:
      c=c+5

def b1(c,memoria):
   var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
   c=var1
   return memoria, c

def c0(c, memoria):
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  memoria[var1]=negar(bin(memoria[var1]))
def c1(c,memoria):
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  conjuncion = memoria[var1] and memoria[var2]
  c=c+5
  memoria[var2]=conjuncion
def c2(c,memoria):
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  disyuncion = memoria[var1] or memoria[var2]
  c=c+5
  memoria[var2]=disyuncion

def c3(c, memoria):
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  resultado=xor(memoria[var1],memoria[var2])
  if len(bin(resultado))>8:
     resultado=may255(resultado)
     memoria[var2]=resultado
  else:
     memoria[var2]=resultado
  return memoria,c

def d0(c,memoria): #Suma
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  a=memoria[var1]+memoria[var2]
  if len(bin(a))>8:
     a=may255(a)
     memoria[var2]=a
  else:
     memoria[var2]=a
  c=c+5
  return memoria,c

def d1(c,memoria): #Resta
  var1=int(extraerOp(memoria[c+1])+extraerOp(memoria[c+2]),16)
  var2=int(extraerOp(memoria[c+3])+extraerOp(memoria[c+4]),16)
  suma=memoria[var2]-memoria[var1]
  if len(bin(suma))>8:
     suma=may255(suma)
     memoria[var2]=suma
  else:
     memoria[var2]=suma
  c=c+5
  return memoria,c

def d2(c,memoria): #Modulo
  var1=int(memoria[c+1]+memoria[c+2],16)
  var2=int(memoria[c+3]+memoria[c+4],16)
  suma=memoria[var1]%memoria[var2]
  memoria[var2]=suma
  if len(bin(a))>8:
     a=may255(a)
  else:
     memoria[var2]=a
  c=c+5
  return memoria
def d3(c,memoria): #Revisar
  global xp
  xp=xp+1
  c=c+1
  return memoria,c
  
def d4(c, memoria): #Revisar
   global xp
   xp=xp-1
   c=c+1
   return memoria,c

def f0(c,memoria):
  c=c+1
  with open('mem.dump','wb') as d:
      memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
      d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump
  return memoria,c

def f1(c, memoria):
  c=len(memoria)+1
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
  "0xd3":d3,
  "0xd4":d4,
  "0xf0":f0,
  "0xf1":f1,
}
def extraerOp(valor): #a0 d1 f4 10 ejemplo
  return hex(valor)[2:len(hex(valor))] #le saca la x al hexa

def may255(valor): #Cuando usemos valores mayores a 255
  return int(bin(valor)[len(bin(valor))-8:len(bin(valor))],2)
 
memoria = [0] * 65535#vector memoria

operaciones=["a0","a1","a2","a3","a4","a5","a6","a7","b0","b1","c0","c1","c2","c3","d0","d1","d2","d3","d4","f0","f1"]

# Abrimos el programa a ejecutar
with open(sys.argv[1], 'rb') as programa:
  code = programa.read()
print(code)
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
   
