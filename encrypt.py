def encrypt(text, shift):
    result = ""
    for i in range(shift):
        result += text[i::shift]  # Taking every shift-th character
    return result

def decrypt(text, shift):
    length = len(text)
    rows = [''] * shift
    index = 0

    # Calculate the length of each rail (row)
    rail_lengths = [0] * shift
    for i in range(length):
        rail_lengths[i % shift] += 1

    # Split text into rails
    start = 0
    for i in range(shift):
        rows[i] = text[start:start + rail_lengths[i]]
        start += rail_lengths[i]

    # Reconstruct the original order
    result = []
    indices = [0] * shift
    for i in range(length):
        row = i % shift
        result.append(rows[row][indices[row]])
        indices[row] += 1

    return ''.join(result)

# Sample text
a = """ """

b = encrypt(a, 3)
print("Encrypted:", b)

c = decrypt(b, 3)
print("Decrypted:", c)
