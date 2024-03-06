# Dier.py
# Anjo Eijeriks
# 2023/11/30 V3

class Dier:
    # CONSTRUCTOR MET PROPERTIES ----------------------------------------------
    def __init__(self, dierid, soort, naam):
        self.dierid = dierid  # Let op: we gebruiken dubbele 
        self.soort  = soort   # underscores om de attributen 
        self.naam   = naam    # privé te maken
        
        self.conn   = None    # initialiseer connection variabele
        self.cursor = None    # initialiseer cursor variabele
             
    # DATABASE METHODEN -------------------------------------------------------
    def open_database(self):
        import sqlite3
        self.conn = sqlite3.connect('dierentuin.db')
        self.cursor = self.conn.cursor()
        
    def sluit_database(self):
        self.conn.commit()
        self.conn.close()

    # CRUD METHODEN -----------------------------------------------------------
    # dier toevoegen aan de tabel dieren        
   

    # alle dieren van de tabel laten zien
    def read_dieren(self, dierid, soort, naam):
        self.open_database()
        select_query = """
        SELECT * FROM dieren
        """
        self.cursor.execute(select_query)
        dieren = self.cursor.fetchall()
        return dieren           # array 'dieren' gaat terug naar formReadDieren.py
        self.sluit_database()
            
    # dier in de tabel updaten
  
    # dier uit de tabel verwijderen
   
    # dier in de tabel opzoeken
    def search_dier(self, dierid, soort, naam):
        self.__dierid = dierid
        self.open_database()

        select_query = """
        SELECT * FROM dieren
        WHERE dierid = ?
        """
   
        self.cursor.execute(select_query, (dierid,))
        dieren = self.cursor.fetchall()
        return dieren           # array met gevonden dier terug naar formSearchDier.py
        self.sluit_database()
    
    # SETTERS EN GETTERS ZIJN NIET NODIG --------------------------------------