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
memoria = [0] * 65535#vector memoria
c=100

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

def a0():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   memoria[var]=memoria[c+3]
   c=c+4

def a1():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
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
   
def a2():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   N1 = (memoria[var] << 8) + memoria[var + 1]
   if N1 > 100 and N1<1025:
      c= N1
   else:
      print("Error")
      c = len(memoria)
def a3():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   memoria[var2]=memoria[var]
   memoria[var]=0
   c=c+5
   
def a4():
   global xp,c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   if xp>1024 and xp<len(memoria):
      memoria[xp]=memoria[var]
   else:
      print("Error")
   c=c+2

def a5():
   global xp, c, memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   if xp>1024 and xp<len(memoria):
      memoria[var]=memoria[xp]
      memoria[xp]=0
   else:
      print("Error")
      c=len(memoria)
   c=c+2

def a6():
   global xp, c, memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
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

def a7():
   global xp, c, memoria
   total=(memoria[c+1] << 8) + memoria[c+2]
   xp=total
   c=c+3

def b0():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   if memoria[var2]==0:
      c=var
   else:
      c=c+5

def b1():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   c=var

def c0():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   memoria[var1]=negar(bin(memoria[var1]))
   c=c+3
def c1():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   conjuncion = memoria[var1] and memoria[var2]
   c=c+5
   memoria[var2]=conjuncion
   
def c2():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   disyuncion = memoria[var1] or memoria[var2]
   c=c+5
   memoria[var2]=disyuncion

def c3():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   resultado=xor(memoria[var1],memoria[var2])
   if len(bin(resultado))>8:
      resultado=may255(resultado)
      memoria[var2]=resultado
   else:
      memoria[var2]=resultado
   c=c+5

def d0(): #Suma
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   a=memoria[var1]+memoria[var2]
   if len(bin(a))>8:
      a=may255(a)
      memoria[var2]=a
   else:
      memoria[var2]=a
   c=c+5

def d1(): #Resta
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   suma=memoria[var2]-memoria[var1]
   if len(bin(suma))>8:
      suma=may255(suma)
      memoria[var2]=suma
   else:
      memoria[var2]=suma
   c=c+5

def d2(): #Modulo
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   suma=memoria[var1]%memoria[var2]
   memoria[var2]=suma
   if len(bin(a))>8:
      a=may255(a)
   else:
      memoria[var2]=a
   c=c+5
   return memoria

def d3(): #Revisar
   global xp, c, memoria
   xp=xp+1
   c=c+1

def d4(): #Revisar
   global xp, c, memoria
   xp=xp-1
   c=c+1

def f0():
   global c,memoria
   c=c+1
   with open('mem.dump','wb') as d:
      memoria_bytes=bytes(memoria) #Convertimos la variable en una cadena de bytes
      d.write(memoria_bytes) #Lo escribimos en el archivo mem.dump

def f1():
   global c,memoria
   c=len(memoria)+1

#si "a0" esta en el vevtor operaciones va a hacer tal funcion que esta determinada aca:
funciones={"0xa0":a0, "0xa1":a1, "0xa2":a2, "0xa3":a3, "0xa4":a4, "0xa5":a5, "0xa6":a6, "0xa7":a7, "0xb0":b0, "0xb1":b1, "0xc0":c0, "0xc1":c1, "0xc2":c2, "0xc3":c3, "0xd0":d0, "0xd1":d1, "0xd2":d2, "0xd3":d3, "0xd4":d4, "0xf0":f0, "0xf1":f1,}

def may255(valor): #Cuando usemos valores mayores a 255
 return int(bin(valor)[len(bin(valor))-8:len(bin(valor))],2)

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
      funciones[a]()
  else:
      c += 1
