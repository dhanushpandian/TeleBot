import base64
def xor_encrypt(text, key):
    encrypted_bytes = bytearray([ord(c) ^ ord(key[i % len(key)]) for i, c in enumerate(text)])
    return base64.b64encode(encrypted_bytes).decode('utf-8')

def xor_decrypt(encrypted_text, key):
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted_text = ''.join(chr(b ^ ord(key[i % len(key)])) for i, b in enumerate(encrypted_bytes))
    return decrypted_text

KEY = "mysecretkey"

text = """

"""

# encrypted_text = xor_encrypt(text, KEY)
# print("Encrypted:", encrypted_text)


decrypted_text = xor_decrypt(text, KEY)
print("Decrypted:", decrypted_text)


