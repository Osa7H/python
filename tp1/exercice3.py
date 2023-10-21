distance=float(input("Entrer la distance : "))
temps=float(input("Entrer le temps : "))
if(temps==0):
    temps=1122
vitesse=distance/temps
print("vitesse = ",vitesse)