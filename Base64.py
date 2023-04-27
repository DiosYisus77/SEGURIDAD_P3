import base64
def encode(cadena):

    return base64.b64encode(cadena.encode()).decode('utf-8')
def decode(cadena):
    return base64.b64decode(cadena).decode('utf-8')

print('Escribe un string y pulsa ENTER')
cadena = input()

print('Codificador Base64')
print('0. Codificar')
print('1. Decodificar')
print('Escribe una opción (0/1) y pulsa ENTER')
option = int(input())

if option == 0:
    print(encode(cadena))
elif option == 1:
    print(decode(cadena))
else:
    print("ERROR: Opción distinta de 0 ó 1")