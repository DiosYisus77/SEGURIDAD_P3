def descifrar_xor(encoded, key):

    decoded = ""
    for i in range(len(encoded)):
        decoded += chr(ord(encoded[i]) ^ ord(key[i % len(key)]))
    return decoded

    cadena_descifrada = decoded
    print(f' Resultado: {cadena_descifrada}')

cadena_cifrada = input()
clave = input()

descifrar_xor(cadena_cifrada, clave)