from cryptography.fernet import Fernet
import sqlite3

# called by rpi to log in 
def login(id):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (id,))
    if c.fetchone():
        c.execute("UPDATE users SET loggedIn = 1 WHERE id = ?", (id,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

# called by web client to log out
def logout(name):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE name = ?", (name,))
    if c.fetchone():
        c.execute("UPDATE users SET loggedIn = 0 WHERE name = ?", (name,))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False
    
# caled by web client to check if user is logged in
def is_logged_in():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
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
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("INSERT INTO users (id, name, loggedIn) VALUES (?, ?, 0)", (id, name))
    conn.commit()
    conn.close()
    return True

# utility function
def deleteUser(id):
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return True

# utility function
def initTable():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()
    # id numbers too large to be simple integers
    # booleans must to 0/1 ints in sqlite
    c.execute("CREATE TABLE users (id text, name text, loggedIn integer)")
    conn.commit()
    conn.close()
    return True
    
# code to allow us to manually execute database commands
if __name__ == '__main__':
    deleteUser("243532354")
    addUser("584190492038", "Miles")
    addUser("584183342306", "Will")
