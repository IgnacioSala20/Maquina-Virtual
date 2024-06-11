def d0(instrucciones,i,memoria): #Suma 
    var1=int(instrucciones[i+1]+instrucciones[i+2],16)
    var2=int(instrucciones[i+3]+instrucciones[i+4],16)
    suma=memoria[var1]+memoria[var2]
    memoria[var2]=suma
    return memoria

vector=[] * 6

for i in range(len(vector)):
    vector[i]=str(input("hola"))

memoria = [0x10, 0x20, 0x30, 0x40, 0x50, 0x60]
for i in range(len(vector)):
    if vector[i]=="d0":
        a=d0(vector,i,memoria)
        print(a)