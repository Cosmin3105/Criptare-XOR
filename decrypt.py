import sys

input_file = sys.argv[1]
parola = sys.argv[2]
output_file = sys.argv[3]

decrypted_text = []
p_index = 0

with open(input_file, 'rb') as f:
    while True:
        b = f.read(1)
        if not b:
            break
        c = int.from_bytes(b, byteorder='big')
        decrypted_c = c ^ ord(parola[p_index])
        p_index = (p_index + 1) % len(parola)
        decrypted_text.append(chr(decrypted_c))

decrypted_text = "".join(decrypted_text)

with open(output_file, 'w') as f:
    f.write(decrypted_text)
    