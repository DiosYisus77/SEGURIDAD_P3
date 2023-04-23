import base64

clave_codificada = input()

# Decodificación de Base64
clave_decodificada = base64.b64decode(clave_codificada)

print(clave_decodificada.decode('utf-8'))