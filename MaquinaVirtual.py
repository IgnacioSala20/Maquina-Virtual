import sys
xp=0
memoria = [0] * 65535
c=100

def a0():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   memoria[var]=memoria[c+3]
   c=c+4
def a1():
   global c,memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   memoria[var]=(c>>8) & 0xFF
   memoria[var+1]=c & 0xFF 
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
   memoria[var]=(xp>>8) & 0xFF 
   memoria[var+1]=xp & 0xFF 
   c=c+3
def a7():
   global xp, c, memoria
   var=(memoria[c+1] << 8) + memoria[c+2]
   N1 = (memoria[var] << 8) + memoria[var + 1]
   xp=N1
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
   memoria[var1]=~(bin(memoria[var1])) & 0xFF
   c=c+3
def c1(): 
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   conjuncion = memoria[var1] & memoria[var2]
   c=c+5
   memoria[var2]=conjuncion
def c2(): 
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   disyuncion = memoria[var1] | memoria[var2]
   c=c+5
   memoria[var2]=disyuncion
def c3():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   resultado=(memoria[var1] ^ memoria[var2]) & 0xFF
   memoria[var2]=resultado
   c=c+5
def d0(): 
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   a=memoria[var1]+memoria[var2]
   a=a & 0xFF
   memoria[var2]=a
   c=c+5
def d1():
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   suma=memoria[var2]-memoria[var1]
   suma=suma & 0xFF
   memoria[var2]=suma
   c=c+5
def d2(): 
   global c,memoria
   var1=(memoria[c+1] << 8) + memoria[c+2]
   var2=(memoria[c+3] << 8) + memoria[c+4]
   suma=memoria[var1]%memoria[var2]
   suma=suma % 0xFF
   memoria[var2]=suma
   c=c+5
   return memoria
def d3(): 
   global xp, c, memoria
   xp=xp+1
   c=c+1
def d4(): 
   global xp, c, memoria
   xp=xp-1
   c=c+1
def f0():
   global c,memoria
   c=c+1
   with open('mem.dump','wb') as d:
      memoria_bytes=bytes(memoria) 
      d.write(memoria_bytes)
def f1():
   global c,memoria
   c=len(memoria)+1

funciones={"0xa0":a0, "0xa1":a1, "0xa2":a2, "0xa3":a3, "0xa4":a4, "0xa5":a5, "0xa6":a6, "0xa7":a7, "0xb0":b0, "0xb1":b1, "0xc0":c0, "0xc1":c1, "0xc2":c2, "0xc3":c3, "0xd0":d0, "0xd1":d1, "0xd2":d2, "0xd3":d3, "0xd4":d4, "0xf0":f0, "0xf1":f1,}
operaciones=["a0","a1","a2","a3","a4","a5","a6","a7","b0","b1","c0","c1","c2","c3","d0","d1","d2","d3","d4","f0","f1"]

with open(sys.argv[1], 'rb') as programa:
   code = programa.read()
print(code)
pos = 100
for i in code:
   if pos<1025:
      memoria[pos]=i
      pos+= 1

while c<len(memoria):
   a=hex(memoria[c])
   if a in funciones:
      funciones[a]()
   else:
      c+= 1