# unittestCreateDier.py
# chatGPT
# 2023/12/19 v1

import unittest
from Dier import Dier

class TestDier(unittest.TestCase):
    def test_create_dier(self):
        # Maak een instantie van de Dier klasse
        dier_instance = Dier(None, None, None)

        # Testgegevens
        dierid = 101
        soort = "TestSoort"
        naam = "TestNaam"

        # Voer de create_dier methode uit
        dier_instance.create_dier(dierid, soort, naam)

        # Lees de dieren uit de database en zoek het toegevoegde dier
        dieren = dier_instance.read_dieren(None, None, None)
        toegevoegd_dier = None
        for dier in dieren:
            if dier[0] == dierid and dier[1] == soort and dier[2] == naam:
                toegevoegd_dier = dier
                break

        # Assert dat het toegevoegde dier aanwezig is in de database
        self.assertIsNotNone(toegevoegd_dier, "Het toegevoegde dier is niet gevonden in de database.")

        # Assert de waarden van het toegevoegde dier
        self.assertEqual(toegevoegd_dier[0], dierid, "Onjuiste dierid in de database.")
        self.assertEqual(toegevoegd_dier[1], soort, "Onjuiste soort in de database.")
        self.assertEqual(toegevoegd_dier[2], naam, "Onjuiste naam in de database.")

if __name__ == '__main__':
    unittest.main()
