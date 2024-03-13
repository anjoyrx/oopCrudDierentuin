import sqlite3
# Maak verbinding met de database (of maak deze aan als deze nog niet bestaat)
conn = sqlite3.connect('dierentuin.db')
# Maak een cursor object om commando's uit te voeren
cur = conn.cursor()
# Maak de tabel
cur.execute('''
CREATE TABLE IF NOT EXISTS dieren (
    dierid INTEGER PRIMARY KEY AUTOINCREMENT,
    soort TEXT,
    naam TEXT
)
''')
# Commit de transactie
conn.commit()
# Sluit de verbinding
conn.close()
