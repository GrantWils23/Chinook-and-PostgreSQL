import psycopg2


# connect to 'chinook' database
connection = psycopg2.connect(database="chinook")


# built a cursor object of the database
cursor = connection.cursor()


# Query1 - select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')


# Query2 - select only the "Name" column from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')


# Query3 - select only "Queen" from the "Artist" Table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])


# Query4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])


# Query5 - select only the albums with the "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])


# Query6 - select all tracks where the composer is "Queen" from the "Track"
# table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])


# CUSTOM QUERY - select only "Black Sabbath" from the "Artist" table
cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Black Sabbath"])

# fetch the results (multiple)
results = cursor.fetchall()


# feth the result (single)
# results = cursor.fetchone()


# close the connection
connection.close()


# print results
for result in results:
    print(result)
