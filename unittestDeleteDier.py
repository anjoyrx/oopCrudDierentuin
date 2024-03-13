# unittestDeleteDier
# chatGPT
# 2023/12/19 v1

# prompt: Kan je een unit test voor me schrijven die deleteDier() test?

import unittest
from Dier import Dier

class TestDier(unittest.TestCase):
    def test_delete_dier(self):
        # Maak een instantie van de Dier klasse
        dier_instance = Dier(None, None, None)

        # Testgegevens
        soort = "TestSoort"
        naam = "TestNaam"

        # Voeg een dier toe aan de database
        dier_instance.create_dier(None, soort, naam)

        # Lees de dieren uit de database en zoek het toegevoegde dier
        dieren_voor_verwijdering = dier_instance.read_dieren(None, None, None)
        toegevoegd_dier = None
        for dier in dieren_voor_verwijdering:
            if dier[1] == soort and dier[2] == naam:
                toegevoegd_dier = dier
                break

        # Roep de delete_dier methode aan met de gegevens van het toegevoegde dier
        if toegevoegd_dier:
            dier_instance.delete_dier(toegevoegd_dier[0], toegevoegd_dier[1], toegevoegd_dier[2])

        # Roep de read_dieren methode aan om de lijst van dieren te krijgen
        dieren_na_verwijdering = dier_instance.read_dieren(None, None, None)

        # Print enkele details om te helpen bij het debuggen
        print("Verwacht dier niet in de lijst:", (soort, naam))
        print("Dieren in de database na verwijdering:", dieren_na_verwijdering)

        # Assert dat het verwijderde dier niet aanwezig is in de lijst
        verwijderd_dier_afwezig = not any(d[1] == soort and d[2] == naam for d in dieren_na_verwijdering)
        self.assertTrue(verwijderd_dier_afwezig, "Het verwijderde dier is nog steeds aanwezig in de lijst.")

if __name__ == '__main__':
    unittest.main()
