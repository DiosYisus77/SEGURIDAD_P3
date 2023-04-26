def xor(message, key):
    message_bytes = message.encode('iso-8859-1')
    key_bytes = key.encode('iso-8859-1')

    encoded_bytes = bytearray(len(message_bytes))

    for i in range(len(message_bytes)):
        encoded_bytes[i] = message_bytes[i] ^ key_bytes[i % len(key_bytes)]

    return encoded_bytes.decode('iso-8859-1')
mensaje, key= input().strip().split()
print(xor(mensaje,key))
