# unittestReadDieren
# chatGPT
# 2023/12/19 v1

# prompt: Kan je een unit test voor me schrijven die readDieren() test?


import unittest
from Dier import Dier

class TestDier(unittest.TestCase):
    def test_read_dieren(self):
        # Maak een instantie van de Dier klasse
        dier_instance = Dier(None, None, None)

        # Testgegevens
        soort = "TestSoort"
        naam = "TestNaam"

        # Voeg een dier toe aan de database
        dier_instance.create_dier(None, soort, naam)

        # Roep de read_dieren methode aan
        dieren = dier_instance.read_dieren(None, None, None)

        # Print enkele details om te helpen bij het debuggen
        print("Verwacht dier in de lijst:", (soort, naam))
        print("Dieren in de database:", dieren)

        # Assert dat het toegevoegde dier aanwezig is in de lijst
        toegevoegd_dier_aanwezig = any(d[1] == soort and d[2] == naam for d in dieren)
        self.assertTrue(toegevoegd_dier_aanwezig, "Het toegevoegde dier is niet gevonden in de lijst.")

if __name__ == '__main__':
    unittest.main()
