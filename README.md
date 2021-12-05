# Folosire:
Pentru encriptare:
```
python encrypt.py <parola> <fișier pentru criptare> <fișier encriptat(de tip binar)>
```

Pentru decriptare:
```
python decrypt.py <parola> <fișier encriptat(de tip binar)> <fișier decriptat>
```
# Continuare proiect:
```
Echipa noastra: Calusarii

Echipa adversa: Grozavesti

Cheie echipa adversa: profurusuecool
```
### Solutie:

Am folosit un script pass_crack.py pentru a determina parola adversa folosind brute-force.

Am fixat lungimea parolei (de la 10 la 15 caractere), apoi am traversat fisirul binar advers, afland pentru fiecare caracter din parola multimea de valori posibile astfel incat: 
```
valoare_posibila ^ caracter_binar_advers = caracter vizibil. 
```

#### Experimental:
Am observat ca solutia este unica (14 caractere, fiecare caracter avand o singura valoare posibila), nemaifiind necesara implementarea unei metode backtracking.

De asemenea, am descoperit ca fisierul input advers (dar si al nostru...oops) contine caractere cu codul ASCII peste 255 care au fost determinante cu ajutorul scriptului helpful.py.


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
