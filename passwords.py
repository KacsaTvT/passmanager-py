import mysql.connector

passw = 3644

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'jelszavak'
)
cursor = database.cursor()

#cursor.execute("CREATE TABLE pass (forras VARCHAR(255), jelszo VARCHAR(255))")

userpass = None
folytatas = True
uj1 = None
uj2 = None
command = None

while folytatas:
    userpass=int(input("Mi a PIN? "))
    if userpass == passw:
        command=input("Mit szeretnél tenni? (megtekintés / hozzáadás / kilépés) ")
        if command=="hozzáadás":
            uj1 = input("Mihez adsz meg új jelszót? ")
            uj2 = input("Mi a jelszó? ")
            if uj1 =='' or uj2=='':
                folytatas=False
            else:
                cursor.execute("INSERT INTO pass (forras, jelszo) VALUES (%s, %s)", (uj1,uj2))
                database.commit()
        if command=="megtekintés":
            cursor.execute("SELECT * FROM pass")
            result= cursor.fetchall()
            for row in result:
                print(row, '\n')
    else:
        folytatas=False
    if command== '' or command=='kilépés':
        folytatas=False

print("A program vége")
