# Folosire:
Pentru encriptare:
```
python encrypt.py <parola> <fișier pentru criptare> <fișier encriptat(de tip binar)>
```

Pentru decriptare:
```
python decrypt.py <parola> <fișier encriptat(de tip binar)> <fișier decriptat>
```

# Explicații:
Pentru o criptare eficientă a textului din fișierul de intrare am criptat caracter cu caracter folosind operația pe biți xor(^), astfel:
```
crypt[i] = text[i] ^ parola[i % lungimea_parolei]
```

Pentru decriptare a fost folosită aceeași metodă.

 # Gestionarea erorilor:
Programul va returna în consolă următoarele mesaje în cazul în care întâlnește erori:

"Numar de argumente incorect!" - Nu a fost transmis numărul corect de parametrii

"Parola invalida" - Parola transmisă nu are între 10 și 15 caractere

"Fisier de citire inexistent" - Fișierul ce va trebui citit nu se află în folderul script-ului
