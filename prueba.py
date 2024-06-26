memoria = [0] * 65535#vector memoria
c=100

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

def may255(valor): #Cuando usemos valores mayores a 255
 return int(bin(valor)[len(bin(valor))-8:len(bin(valor))],2)

