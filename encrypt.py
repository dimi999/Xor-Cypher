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
    with open(file_in, 'r') as f:
        to_encrypt = f.read()
except FileNotFoundError:
    print('Fisier de citire inexistent')
    sys.exit()

out = open(file_out, 'wb')

encrypted = ''
for i, j in enumerate(to_encrypt):
    encrypted += chr(ord(j) ^ ord(password[i % len(password)]))
encrypted = bytes(encrypted.encode('utf8'))

out.write(encrypted)
out.close()







