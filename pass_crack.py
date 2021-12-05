import sys

file_in = "output"

try:
    with open(file_in, 'rb') as f:
        binary = f.read()
except FileNotFoundError:
    print('Fisier de citire inexistent')
    sys.exit()

binary = binary.decode('utf-8')

chars = " \\/,@^[]()~<>\.`_-–!?:\";\n™€“…’\t|â¦”"
for i in range(256):
    chars += chr(i)

for len_pass in range(10, 16):
    posib = []
    for i in range(len_pass):
        p = set()
        for i in range(1, 9000):
            p.add(i)
        posib.append(p)

    for i, t in enumerate(binary):
        p = set()
        for c in chars:
            p.add(ord(c) ^ ord(t))
        posib[i % len_pass] = posib[i % len_pass] & p

    we_have_pass = True

    for i in range(len_pass):
        if len(posib[i]) == 0:
            we_have_pass = False

    if we_have_pass == True:
        password = ""
        for i in range(len_pass):
            for c in posib[i]:
                password += chr(c)
        print(password)
        