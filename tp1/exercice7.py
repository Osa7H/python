nmbr1=float(input("Entrer un nombre : "))
nmbr2=float(input("Entrer un nombre : "))
op=input("Entrer l'operateur : ")
if(op=="+"):
    print(nmbr1," + ",nmbr2," = ",nmbr1+nmbr2)
if(op=="-"):
    print(nmbr1," - ",nmbr2," = ",nmbr1-nmbr2)
if(op=="*"):
    print(nmbr1," * ",nmbr2," = ",nmbr1*nmbr2)
if(op=="/"):
    if(nmbr2==0):
        print(nmbr1," / ",nmbr2," = ",nmbr1/nmbr2)
    else:
        print("Impossible")