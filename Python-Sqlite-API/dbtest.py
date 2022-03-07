import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

#Crear la tabla Tracks
cur.execute('DROP TABLE IF EXISTS Tracks')
cur.execute('CREATE TABLE Tracks (title TEXT, plays INTEGER)')

#Añadir datos a la tabla Tracks
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)', 
            ('Thunderstruck', 20))
cur.execute('INSERT INTO Tracks (title, plays) VALUES (?, ?)',
            ('My Way', 15))
conn.commit()

#Mostrar los datos de la tabla Tracks
print('Tracks:')
cur.execute('SELECT title, plays FROM Tracks')
for row in cur:
     print(row)

#Eliminar canciones con menos de 100 reproducciones
#cur.execute('DELETE FROM Tracks WHERE plays < 100')
#conn.commit()

conn.close()