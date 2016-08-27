from setup import *
from os import path
import md5

#=== Creates database if database isn't in main dir ===#
if not path.isfile("database.db"):
    create_db()

#=== Helper function to salt and hash ===#
def saltnhash(user,password):
    m = md5.new()
    m.update(user + password)
    return m.hexdigest()

#=== Adds user and password ===#
def create_user(user, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    d = c.execute("SELECT * FROM login WHERE user = ?", (user,))
    for row in d:
        conn.commit()
        conn.close()
        return False
    c.execute("INSERT INTO login VALUES(?,?)", (user, saltnhash(user,password),))
    conn.commit()
    conn.close()
    return True

#=== Checks if user and password are in db ===#
def check_user(user, password):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT * FROM login WHERE user = ? and password = ?", (user, saltnhash(user,password),))
    for row in c:
        conn.close()
        return True
    conn.close()
    return False
