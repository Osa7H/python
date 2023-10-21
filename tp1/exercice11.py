a=float(input("Saisir votre pois"))
b=float(input("Saisir votre taille"))

IMC=a/b

if(IMC<16.5):
    print("Famine")
elif(IMC<18.5):
    print("Maigreur")
elif(IMC<25):
    print("Corpulence normale")
elif(IMC<30):
    print("Surpoids")
elif(IMC<35):
    print("obesite modere")
elif(IMC<40):
    print("obesite severe")
else:
    print("obesite morbide ou massive")