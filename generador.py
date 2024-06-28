# Abre un archivo en modo binario para escribir
with open('archivo.bin', 'wb') as f:
    # Lista de valores que deseas escribir en el archivo binario
    valores = [0xA1,0xd1,0xf4 ,0xF0,0XF1]   # Puedes agregar más valores si lo deseas
    
    # Itera sobre cada valor y escríbelo en el archivo
    for valor in valores:
        # Utiliza la función 'to_bytes' para convertir el valor en su representación binaria
        # El segundo argumento indica el número de bytes que debe ocupar el valor
        f.write(valor.to_bytes(1, byteorder='big'))  # 1 byte por valor

print("Archivo binario generado correctamente.")