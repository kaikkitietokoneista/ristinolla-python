import random
kohdat = [-1,-1,-1,-1,-1,-1,-1,-1,-1,]

vuoro = 0;

print("+------------------+")
print("|      OHJEET      |")
print("|Siirtojen muoto:  |")
print("|1 = kohta 1       |")
print("|4 = kohta 4       |")
print("+------------------+")

def taulu():
    nro = 0
    teksti = ""
    for laatikko in kohdat:
        nro += 1
        if laatikko == 0:
            laatikko = "x"
        if laatikko == 1:
            laatikko = "o"
        if laatikko == -1:
            laatikko = " "
        if nro == 3:
            teksti += laatikko + " "
            teksti += "\n--+---+---\n"
            nro = 0
        else:
            teksti += laatikko + " | "
    print(teksti)

def eikailukuooyli(luku):
    if luku == 3 or luku == 6 or luku == 9:
        return 20

def tarkastavoitto():
    #print(kohdat[luku])
    #print(kohdat[luku + 1])
    #print(kohdat[luku + 2])
    if kohdat[0] ==  kohdat[1] ==  kohdat[2] : return kohdat[0] #vertikaalit
    if kohdat[3] ==  kohdat[4] ==  kohdat[5] : return kohdat[3]
    if kohdat[6] ==  kohdat[7] ==  kohdat[8] : return kohdat[6]
    if kohdat[0] ==  kohdat[3] ==  kohdat[6] : return kohdat[0] #horisontaalit
    if kohdat[1] ==  kohdat[4] ==  kohdat[7] : return kohdat[1]
    if kohdat[2] ==  kohdat[5] ==  kohdat[8] : return kohdat[2]
    if kohdat[0] ==  kohdat[4] ==  kohdat[8] : return kohdat[0] #Diagonaali 1
    if kohdat[6] ==  kohdat[4] ==  kohdat[2] : return kohdat[6] #Diagonaali 2


taulu()
while True:
    if vuoro == 0:
        valittu = False
        while valittu == False:
            siirto = input("Siirto x: ")
            if siirto != "":
                testi = int(siirto)-1
                if kohdat[testi] == -1:
                    kohta = testi
                    valittu = True

        vuoro += 1;

        kohdat[kohta] += 1
        taulu()
        if tarkastavoitto() == 0:
            print("Voittaja oooon X!!!")
            exit()
        #print(kohdat)
    else:
        print("Robotti vastaa...")
        valittu = False
        while valittu == False:
            testi = random.randint(0, 8)
            #print(testi)
            if kohdat[testi] == -1:
                kohta = testi
                valittu = True
            else:
                pass
        vuoro -= 1;

        kohdat[kohta] += 2

        taulu()
        tarkastavoitto()
        if tarkastavoitto() == 1:
            print("Voittaja oooon O!!!")
            exit()
        #print(kohdat)
