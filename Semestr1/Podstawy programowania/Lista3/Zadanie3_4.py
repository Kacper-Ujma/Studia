
#Zdanie = str(input('wpisz zdanie do przetlumaczenia\n'))
#Zdanie = "N zna, n cyna, n pnany: Cnanzn!"

Zdanie = "N PBQR BS RGUVPNY ORUNIVBE SBE CNGVRAGF:\n\
1. QB ABG RKCRPG LBHE QBPGBE GB FUNER LBHE QVFPBZSBEG. Vaibyirzrag\n\
jvgu gur cngvrag’f fhssrevat zvtug pnhfr uvz gb ybfr inyhnoyr\n\
fpvragvsvp bowrpgvivgl.\n\
2. OR PURRESHY NG NYY GVZRF. Lbhe qbpgbe yrnqf n ohfl naq gelvat\n\
yvsr naq erdhverf nyy gur tragyrarff naq ernffhenapr ur pna trg.\n\
3. GEL GB FHSSRE SEBZ GUR QVFRNFR SBE JUVPU LBH NER ORVAT GERNGRQ.\n\
Erzrzore gung lbhe qbpgbe unf n cebsrffvbany erchgngvba gb\n\
hcubyq."

Szyfr = []
for i in range(len(Zdanie)):
    if Zdanie[i].islower()==True:
        if (ord(Zdanie[i]) >= ord("a")) and (ord(Zdanie[i]) <= ord("z")):
            if ord(Zdanie[i])+13<=ord("z"):
                Szyfr.append(chr(ord(Zdanie[i])+13))
            else:
                Szyfr.append(chr(ord(Zdanie[i])-13))
    elif Zdanie[i].isupper()==True:
        if (ord(Zdanie[i]) >= ord("A")) and (ord(Zdanie[i]) <= ord("Z")):
            if ord(Zdanie[i])+13<=ord("Z"):
                Szyfr.append(chr(ord(Zdanie[i])+13))
            else:
                Szyfr.append(chr(ord(Zdanie[i])-13))
    else:
        Szyfr.append(Zdanie[i])

def Zamiana (s):
    Str1 = ""
    return(Str1.join(s))

print(Zamiana(Szyfr))

            
