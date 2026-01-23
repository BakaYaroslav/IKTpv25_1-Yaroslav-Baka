# paev=input("Sisesta päeva nimetus (näiteks esmaspäev): ")
# #1. Kui on neljapäev, siis "Huraaa, Prgrammeerimine!
# if paev.lower()=="neljapäev":
#     print("Huraaa, Programmeerimine!")

# #2. Kui on neljapäev, siis "Huraaa, Prgrammeerimine!, kui on reede, siis "Igatsen, prgrammeerida tahaks!".
# if paev.lower()=="neljapäev":
#     print("Huraaa, Programmeerimine!")
# else:
#     print("Igatsen, programmeerida tahaks!")
# #3. Tööpaevad ja nädalavahetus
# if paev.lower()=="laupäev" or paev.lower()=="pühapäev":
#     print("Lõpuks ometi nädalavahetus!")
# else:
#     print("Tööpäev, pean tööl käima!")

# 1-esmaspäev, 2-teisipäev, 3-kolmapäev, 4-neljapäev, 5-reede, 6-laupäev, 7-pühapäev
# paev_number=int(input("Sisesta päeva number (1-7): "))
# if paev_number==1:
#     print("Esmaspäev")
# elif paev_number==2:
#     print("Teisipäev")
# elif paev_number==3:
#     print("Kolmapäev")
# elif paev_number==4:
#     print("Neljapäev")
# elif paev_number==5:
#     print("Reede")
# elif paev_number==6:
#     print("Laupäev")
# elif paev_number==7:
#     print("Pühapäev")
# else:
#     print("Vale number! Palun sisesta number vahemikus 1-7.")

#1. Juku
# a Kui eesnimi on Juku siis lähme Jukuga kinno. 
# Aga teeme seda nii, kui nimi oli kirjutatud suurtähtedega.
# b Lisa valiku, kus Juku vanuse alusel otsustate 
# mis pilet talle vaja osta. 
# (Tee kontroll, kas sisestatud arv on täisarv)
#     <6 aastad  - tasuta
#     6-14 - lastepilet
#     15-65 - täispilet
#     >65 - sooduspilet
#     <0 ja >100 viga andmetega
# eesnimi=input("Sisesta eesnimi: ")
# if eesnimi=="JUKU":
#     print("Lähme Jukuga kinno!")
#     vanus=input("Sisesta Juku vanus: ")
#     if vanus.isdigit():
#         vanus=int(vanus)
#         if vanus<0 or vanus>100:
#             print("Viga andmetega!")
#         elif vanus<6:
#             print("Pilet on tasuta!")
#         elif vanus<=14:
#             print("Lastepilet")
#         elif vanus<=65:
#             print("Täispilet")
#         else:
#             print("Sooduspilet")
#     else:
#         print("Palun sisesta vanus täisarvuna!")
#2 Pinginaabrid

# Küsi kahe inimese nimed. Kui nimed koosnevad 
# ainult tähedest siis  teavita kasutajat, 
# kas nad on täna pinginaabrid või ei mitte.
# 5 Temperatuur

# Küsi temperatuur ning teata, 
# kas see on üle 18 kraadi (soovitav toasoojus talvel)
try:
    t=float(input("Sisesta temperatuur: "))
    if t>18:
        print("Soovitatav toasoojus talvel")
    else:
        print("Võib olla jahe")
except:
    print("Palun sisesta temperatuur ujukomaarvuna!")