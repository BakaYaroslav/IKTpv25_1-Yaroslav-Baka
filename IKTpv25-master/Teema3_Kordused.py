
#Töö 3.1 
#1. Sisestatakse 15 arvu.
#Määrata, mitu neist on täisarvud.
##k=0 # loendur
for i in range(15):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1}. arv: "))
            break
        except:
            print("Vale andmetüüp!")
        
    if int(arv)==arv:
         print(f"{arv} on täisarv")
         k+=1
print(f"Täisarve oli kokku {k} tk")
#2. Küsi kasutajalt arv A ja 
#leia kõigi naturaalarvude summa vahemikus 1 kuni A.
s=0 # summa
while True:
    try:
        A=int(input(f"Sisesta A: "))
        break
    except:
        print("Vale andmetüüp!")
for i in range(1,A+1):
    s=s+i
print(f"Summa vahemikus 1 kuni {A} võrdub {s}")

#3. Sisestatakse 8 arvu.
#Leida nende korrutis (ainult positiivsete arvude puhul).
korrutis=1
for i in range(8):
    while True:
        try:
            arv=float(input(f"Sisesta {i+1}. arv: "))
            if arv>0: break
        except:
            print("Vale andmetüüp!")
    korrutis*=arv
print(f"Korrutis võrdub {korrutis}")

#4. Koosta programm, 
#mis väljastab ekraanile arvude ruudud vahemikus 10 kuni 20.
for i in range(10,21):
    print(f"Arv {i} ruut on {i**2}")

#5. Koosta programm, mis arvutab ainult negatiivsete arvude summa
#N sisestatud arvu seast.
#N väärtus sisestatakse klaviatuurilt.
# Iseseisvalt





# Töö 2.3 koos kordusetega
#1. samm
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        # Küsi pikkust
        # Küsi massi
    elif soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 või 0")
except:
    print("Vale soov!")




#2. samm
print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah =>"))
    if soov==1:
        print("Indeksi leidmine")
        # Küsi pikkust kuni on õiges formaadis ja vahemikus 0–250
        while True:
            try:
                pikkus = int(input("Mis on sinu pikkus (cm)? "))
                if 0 < pikkus <= 250:
                    break
                else:
                    print("Pikkus peab olema vahemikus 0 kuni 250 cm!")
            except:
                print("Vale pikkuse formaat! Palun sisesta täisarv.")
        
        
        # Küsi massi kuni on õiges formaadis ja vahemikus 0–200
        while True:
            try:
                mass = float(input("Mis on sinu kaal (kg)? "))
                if 0 < mass <= 200:
                    break
                else:
                    print("Kaal peab olema vahemikus 0 kuni 200 kg!")
            except:
                print("Vale kaalu formaat! Palun sisesta arv.")
        
        # Arvuta kehamassiindeks (KMI)
        indeks = round(mass / (0.01 * pikkus) ** 2, 2)
        print(f"{nimi}! Sinu kehamassiindeks on: {indeks}")
        # Hinda KMI. Tee seda ise

    elif soov==0:
        print("Kahju! See on väga kasulik info!")
    else:
        print("Vale valik. Saab valida ainult 1 või 0")
except:
    print("Vale soov!")