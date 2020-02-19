import sqlite3


def Create():
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS crud ( id integer PRIMARY KEY AUTOINCREMENT NULL, name text, lastname text, cid text,  \
    phone text)')
    conn.close()


def Save( name, lastname, cid, phone):
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM crud WHERE name = '{}' and cid = '{}'""".format( name, cid))
    if (cursor.fetchall()):
        print("Já cadastrado")
    else:
        cursor.execute("""INSERT INTO crud( name, lastname, cid, phone) 
        VALUES('{}','{}','{}','{}')""".format(name, lastname, cid, phone))
        conn.commit()
    conn.close()    

def Search(req):
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM crud WHERE name = '{}' or cid = '{}' or phone = '{}'""".format( req, req, req))
    resul = cursor.fetchall()
    conn.close()
    return resul

def Search_All():
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM crud""")
    resul = cursor.fetchall()
    conn.close()
    return resul

def Update( name, lastname, cid, phone):
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("""UPDATE crud SET lastname = '{}', cid = '{}', phone = '{}' WHERE name = '{}'""".format(lastname, cid, phone, name))
    conn.commit()
    conn.close()

def Delete( name):
    conn   = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM crud WHERE name = '{}' """.format(name))
    conn.commit()
    conn.close()