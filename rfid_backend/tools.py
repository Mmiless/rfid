from cryptography.fernet import Fernet
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

# called by server to log in (updates db)
def login(id):
    c.execute("SELECT * FROM users WHERE id = ?", (id,))
    if c.fetchone():
        c.execute("UPDATE users SET loggedIn = 1 WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

# function called by web client to log out
def logout(name):
    c.execute("SELECT * FROM users WHERE name = ?", (name,))
    if c.fetchone():
        c.execute("UPDATE users SET loggedIn = 0 WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
def is_logged_in():
    c.execute("SELECT * FROM users WHERE loggedIn = 1")
    user = c.fetchone()
    if user:
        name = user[1]
        conn.close()
        return 1, name
    else:
        conn.close()
        return 0, None
    
# utility function
def addUser(id, name):
    c.execute("INSERT INTO users (id, name, loggedIn) VALUES (?, ?, 0)", (id, name))
    conn.commit()
    conn.close()
    return True

# utility function
def deleteUser(id):
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return True

# utility function
def initTable():
    # id numbers too large to be simple integers
    # booleans must to 0/1 ints in sqlite
    c.execute("CREATE TABLE users (id text, name text, loggedIn integer)")
    conn.commit()
    conn.close()
    return True
    
# code to allow us to manually execute database commands
if __name__ == '__main__':
    #login("243532354")
    print(is_logged_in())

