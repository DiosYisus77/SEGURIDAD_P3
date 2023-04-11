def descifrar_cesar(cadena):
    for rotacion in range(26):
        texto_descifrado = decodificar_cesar(cadena, rotacion)
        print(f'Rotación {rotacion}: {texto_descifrado}')

def decodificar_cesar(cadena, rotacion):
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    resultado = ''
    for letra in cadena:
        if letra.upper() in alfabeto:
            indice = alfabeto.find(letra.upper())
            indice_desplazado = (indice - rotacion) % len(alfabeto)
            if letra.isupper():
                resultado += alfabeto[indice_desplazado]
            else:
                resultado += alfabeto[indice_desplazado].lower()
        else:
            resultado += letra
    return resultado

mensaje_cifrado = 'MyaolcxuxChzilguncwuWymul'
descifrar_cesar(mensaje_cifrado)