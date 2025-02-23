from cryptography.fernet import Fernet

key = Fernet.generate_key()

key="KZvURnbM6cFEsMBuRN6q-IIuTIJv-vRCt3wgcFtDV2E="

cipher_suite = Fernet(key)

print(f"Key: {key}")
print(f"Cipher Suite: {cipher_suite}")

#text = b"Hello, World!"
#encrypted_text = ""
text=b'gAAAAABnu0jDYCfoGoIZNkUrGh4kZlHDtaqtIPlbWCcLEhcvswTw5j36E8R-sYrb5kTL8giRyJgM2lWGsshyyBNc03CadeMVs7L7BRBWYDP3byEoV8xw8zild2yAFgtF75wQjrvNthbHKjhlUxNLSxhPswCHlH1c5BSSQmwno_wzSSWzhTsJRrXP1G67AwquQa2OgA-OXqN99td_U4v6q5DVDt8J9DSFR-IGfW-ItSnZL4PIMBLVXUBmjH4ebapPtCUJWtXirOrudoyNbM3zgi3XM4bdRnVBVDhniCEBBWXgJvc9x8x6kzQ='
# encrypted_text = cipher_suite.encrypt(text)
# print(f"Encrypted text: {encrypted_text}")

# Decrypt the text
decrypted_text = cipher_suite.decrypt(text)
print(f"Decrypted text: {decrypted_text}")
