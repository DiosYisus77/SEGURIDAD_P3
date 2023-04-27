ALPHABET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def vigenere_encode(plaintext, key):
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_shift = ALPHABET.index(key_char)
            cipher_index = (char_index + key_shift) % len(ALPHABET)
            ciphertext += ALPHABET[cipher_index]
        else:
            ciphertext += char
    return ciphertext


def vigenere_decode(ciphertext, key):
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        if char in ALPHABET:
            char_index = ALPHABET.index(char)
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index %= len(key)
            key_shift = ALPHABET.index(key_char)
            plain_index = (char_index - key_shift) % len(ALPHABET)
            plaintext += ALPHABET[plain_index]
        else:
            plaintext += char
    return plaintext

mensaje_descifrado = vigenere_decode("QqmiaiiiYmisqmwmxijs", "Vigenere")
print("Mensaje descifrado: ", mensaje_descifrado)