import sqlite3

conn = sqlite3.connect('library.db')

c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Books")

Books_list = [
    ('To Kill a Mockingbird','Harper Lee',1960,'Fiction'),
    ('1984','George Orwell',1949,'Dystopian'),
    ('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic')
    ]

c.execute("""CREATE TABLE IF NOT EXISTS Books(
        Title TEXT,
        Author TEXT,
        Year_Published INTEGER,
        Genre TEXT  
    )""")

c.executemany("INSERT OR IGNORE INTO Books VALUES(?,?,?,?)", Books_list)

c.execute("UPDATE Books SET Year_Published = ? WHERE Title = ?", (1950, '1984'))




conn.commit()


c.execute("DELETE FROM Books WHERE Year_Published < 1950")

c.execute("INSERT INTO Books VALUES (?,?,?,?)", ('The Great Gatsby','F. Scott Fitzgerald',1925,'Classic'))

c.execute("SELECT * FROM Books WHERE Genre = ?", ('Dystopian',))
rows = c.fetchall()
for row in rows :
    print(row)


c.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

c.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.8, 'To Kill a Mockingbird'))
c.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.7, '1984'))
c.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (4.5, 'The Great Gatsby'))

conn.commit()

c.execute ("SELECT * FROM Books ORDER BY Year_Published ASC")
rowss = c.fetchall()
for row in rowss :
    print(row)

conn.close()

 