# Criptare-XOR
# Proiect realizat de echipa UnoZero     

Membrii:          
Colceru Cosmin (grupa 142)       
Grigore Mihai-Catalin (grupa 142)        
Ispas Jany-Gabriel (grupa 142)        

Cerinta 1: 

Criptare: python encrypt.py input.txt parola output                   
Decriptare: python decrypt.py output parola text_decriptat.txt

Cerinta 2:
 
Parola folosita de echipa Odin's Triskele: kpho3ItKQCm11          
Prin xor-area fieserelor de input si output ale echipei adverse obtinem sirul de caractere cu care s-a realizat criptarea, de unde putem obtine lista caracterelor care formeaza parola. Deoarece ordinea in care sunt folosite caracterele din parola a fost obtinuta cu functia random.seed trebuie sa aflam seed-ul folosit pentru a putea reconstrui parola. Seed-ul se obtine din suma codurilor ascii ale caracterelor din parola. Stiind caracterele care formeaza parola generam combinatiile posibile de parola cu lungimi cuprinse intre lungimea listei de caractere care formeaza parola (atunci cand niciun caracter nu se repeta) si lungimea maxima permisa pentru parola si verificam daca seed-ul obtinut ne genereaza ordinea de caractere cu care s-a realizat criparea.

