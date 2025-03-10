import sqlite3

conn = sqlite3.connect('roster.db')

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Roster")

Roster_list = [
    ('Benjamin Sisko','Human',40),
    ('Jadzia Dax','Trill',300),
    ('Kira Nerys','Bajoran',29)
    ]

c.execute("""CREATE TABLE IF NOT EXISTS Roster(
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )""")

c.executemany("INSERT OR IGNORE INTO Roster VALUES(?,?,?)", Roster_list)

c.execute("UPDATE Roster SET Name = ? WHERE Name = ?", ('Ezri Dax','Jadzia Dax'))




conn.commit()


c.execute("DELETE FROM Roster WHERE Age > 100")

c.execute("INSERT INTO Roster VALUES (?,?,?)", ('Ezri Dax','Trill', 29))

c.execute("SELECT * FROM Roster WHERE Species = ?", ('Bajoran',))
rows = c.fetchall()
for row in rows :
    print(row)


c.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")

c.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Captain', 'Benjamin Sisko'))
c.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Major', 'Kira Nerys'))
c.execute("UPDATE Roster SET Rank = ? WHERE Name = ?", ('Lieutenant', 'Ezri Dax'))

conn.commit()

c.execute ("SELECT * FROM Roster ORDER BY Age DESC")
rowss = c.fetchall()
for row in rowss :
    print(row)

conn.close()

 