# Dier.py
# Anjo Eijeriks
# 2023/11/30 V3

class Dier:
    # CONSTRUCTOR MET PROPERTIES ----------------------------------------------
    def __init__(self, dierid, soort, naam):
        self.dierid = dierid  # Let op: we gebruiken dubbele 
        self.soort  = soort   # underscores om de attributen 
        self.naam   = naam    # privé te maken
        
  