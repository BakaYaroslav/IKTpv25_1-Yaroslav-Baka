# 1 Sisesta sõna või lause.
# Loenda:
#     mitu täishäälikut 
#     mitu kaashäälikut 
#     kui sisestati lause – loenda ka tühikud ja kirjavahemärgid
import string
t=[ 'a', 'e', 'i', 'o', 'u', 'ü','ä','ö','õ']
k=[ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 'š', 'z', 'ž', 't', 'v', 'w', 'x', 'y']
m=string.punctuation + string.whitespace
sõna_lause=input("Sisesta sõna või lause: ").lower()
täishäälikud=0
kaashäälikud=0
märgid=0
for täht in sõna_lause:
    if täht in t:
        täishäälikud+=1
    elif täht in k:
        kaashäälikud+=1
    elif täht in m:
        märgid+=1
print(f"Sõnas/lauses on {täishäälikud} täishäälikut,")
print(f"{kaashäälikud} kaashäälikut ja {märgid} märki.")

#4
indexid=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa"," Läänemaa, Hiiumaa, Saaremaa"]
while True:
    try:
        index=int(input("Sisesta oma postiindeks (5-kohaline arv): "))
        if 10000<=index<=99999: #len(str(index))==5)
            break
        else:
            print("Postiindeks peab olema 5-kohaline arv")
    except:
        print("vigane andmetüüp")
index_list=list(str(index)) # index=37521 -> list("37521")=["3","7","5","2","1"]
n1=int(index_list[0]) #esimene number -> "3" -> int("3")=3
print(f"Sinu postiindeksiga {index} kuulud piirkonda: {indexid[n1-1]}")
if n1 in [0,1,2,7]:
    print("Mine merre!")
else:
    print("Mine metsa!")
#5️ Vahetus
from random import *
#Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
#Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.
loend_arvud=[]
loend_tähed=[]
loend_kaashäälikud=[]
mitu=randint(2,20)

for i in range(mitu):
    elem=randint(0,100)
    loend_arvud.append(elem)
    elem=chr(randint(65,90)) #A-Z
    loend_tähed.append(elem)
    elem=choice(k) # kaashäälikud k listist 
    loend_kaashäälikud.append(elem)
print(f"Kokku on {mitu} elemente loendis")
while True:
    try:
        paaride_arv=int(input(f"Sisesta mitu paari soovid vahetada: "))
        if 1<=paaride_arv<=mitu//2: #paaride arv peab olema vahemikus 1 kuni mitu//2
            break
        else:
            print(f"Arv peab olema vahemikus 1 kuni {mitu//2}")
    except:
        print("Vigane andmetüüp, proovi uuesti")

#6
loend_arvud=[] # loend arvudest
mitu=randint(2,20) # loendi pikkus 2-20
for i in range(mitu):
    elem=randint(0,100) # juhuslik arv 0-100
    loend_arvud.append(elem)
print(f"Alguses loend: {loend_arvud}")
suurim=max(loend_arvud)
kus_asub=loend_arvud.index(suurim) # leiame suurima arvu indeksi
suurim_muudatud=suurim/mitu
loend_arvud[kus_asub]=round(suurim_muudatud,2)# muudame suurima väärtuse ja ümardame 2 kohta pärast koma
print(f"Muutmise järel: {loend_arvud}")