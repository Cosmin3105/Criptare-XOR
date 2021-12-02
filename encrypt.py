import sys

input_file = sys.argv[1]
parola = sys.argv[2]
output_file = sys.argv[3]

with open(input_file, 'r') as f:
    text = f.read()

ok = 1
p_index = 0
with open(output_file, 'wb') as f:
    for c in text:
        if ord(c) < 128:
            encrypted_c = ord(c) ^ ord(parola[p_index])
        else:
            encrypted_c = ord('?') ^ ord(parola[p_index])
            ok = 0

        p_index = (p_index + 1) % len(parola)
        f.write(encrypted_c.to_bytes(1, byteorder='big'))

if not ok:
    print("Unele caractere nu au putut fi criptate")

