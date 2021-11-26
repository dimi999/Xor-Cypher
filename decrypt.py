import sys

if len(sys.argv) != 4:
    print('Numar de argumente incorect')
    sys.exit()

password = sys.argv[1]
if len(password) > 15 or len(password) < 10:
    print('Parola invalida')
    sys.exit()

file_in = sys.argv[2]
file_out = sys.argv[3]

try:
    with open(file_in, 'rb') as f:
        binary = f.read()
except FileNotFoundError:
    print('Fisier de citire inexistent')
    sys.exit()

binary = binary.decode('utf-8')
out = open(file_out, 'w')

decrypted = ''
for i, j in enumerate(binary):
    decrypted += chr(ord(j) ^ ord(password[i % len(password)]))

print(decrypted, file=out)
