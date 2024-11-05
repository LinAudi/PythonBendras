import sqlite3

connection = sqlite3.connect("people.sqlite")
c = connection.cursor()

# query = """INSERT INTO friends (f_name, l_name, email)
# VALUES ('Jonas','JONAs','j.jon@gmail.com')
# """

# c.execute(query)
# connection.commit()
# connection.close()

# with connection:
#     c.execute(query)




# query = """
# SELECT * FROM friends WHERE l_name = 'Goldman'
# """
#
# query3 = """
# SELECT * FROM friends
# """


# query = """
# SELECT email FROM friends WHERE l_name = 'Goldman'
# """
#
# query3 = """
# SELECT * FROM friends
# """
#
# #
# with connection:
#     c.execute(query)
#     record = c.fetchone()
#     print(record[0:1:])
#
# with connection:
#     c.execute(query3)
#     record = c.fetchall()
#     print(record)
#
#
# name = input("enter your name: ")
#
# query = """
# SELECT * FROM friends WHERE f_name = ?
# """
#
# with connection:
#     c.execute(query, (name,))
#     record = c.fetchall()
#
# if len(record)> 0:
#     print(record)
#
# else:
#     print("No such name")


query4 = """
INSERT INTO friends (f_name, l_name, email)
VALUES (?, ?, ?)
"""

friends = [
    ("Jonas", "Jonaitis", "fdfs@ffs.lt"),
    ("Jane", "Ve", "dffs@ffs.lt"),
]

with connection:
    c.executemany(query4, friends)