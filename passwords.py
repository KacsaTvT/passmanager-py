#password manager
import mysql.connector

passw = 3644
jelszavak = [
    ('steam', 'Zoknikukac123'),
    ('tel', '3644')
]
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'jelszavak'
)
cursor = database.cursor()

#cursor.execute("CREATE TABLE pass (forras VARCHAR(255), jelszo VARCHAR(255))")
'''
cursor.execute("""
    INSERT INTO passs VALUES
        (uj1, uj25)
""")
'''

"""
uj1 = None
uj2 = None
useri = None

folytatas = True
while folytatas:
    useri= int(input("Add meg a PIN-t: "))
    if useri == '':
        folytatas = False
    if useri == passw:
        #print(jelszavak)
        uj1 = input("Mihez adsz meg új jelszót? ")
        uj2 = input("Mi a jelszó?")
        if uj1=='' or uj2=='':
            folytatas = False
    else:
        folytatas = False
"""

#uj1 = input("Mihez adsz meg új jelszót? ")
#uj2 = input("Mi a jelszó? ")


userpass = None
folytatas = True
uj1 = None
uj2 = None
command = None

while folytatas:
    userpass=int(input("Mi a PIN? "))
    if userpass == passw:
        command=input("Mit szeretnél tenni? (megtekintés / hozzáadás) ")
        if command== '':
            folytatás=False
        if command=="hozzáadás":
            uj1 = input("Mihez adsz meg új jelszót? ")
            uj2 = input("Mi a jelszó? ")
            cursor.execute("INSERT INTO pass (forras, jelszo) VALUES (%s, %s)", (uj1,uj2))
            database.commit()
        if uj1 or uj2 == '':
            folytatas=False
        else:
            print("Feltöltve")
        if command=="megtekintés":
            cursor.execute("..........!!!!!!")
    else:
        folytatas=False

print("A program vége")
