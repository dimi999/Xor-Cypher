with open("input_advers.txt", 'r') as f:
    txt = f.read()
    afis = set()

    chars = " \/,@^[]()~<>.`_-–!?:\";\n™€“…’\t|â¦"
    for i in range(256):
        chars += chr(i)

    for i, x in enumerate(txt):
        if x not in chars:
            print(x)
            afis.add(x)
    print(afis)