# formReadDieren.py
# Anjo Eijeriks
# 2023/11/30 v1

from Dier import Dier               # omdat we OOP doen
print("Afdrukken alle dieren")

dierid = None                       # id, soort en naam zijn niet nodig
soort = None
naam = None

nieuw_dier = Dier(dierid, soort, naam)
print("Het object is aangemaakt")

# alle dieren worden opgehaald en komen in de array 'dieren'
dieren = nieuw_dier.read_dieren(dierid, soort, naam)
for dier in dieren:
    print(f"Dier ID: {dier[0]}, Soort: {dier[1]}, Naam: {dier[2]}")

