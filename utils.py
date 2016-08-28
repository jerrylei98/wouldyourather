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

#=== Adds a would you rather question into database ===#
def add_question(optA, optB):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("INSERT INTO game VALUES(?,0,?,0)", (optA,optB,))
    conn.commit()
    conn.close()
    return True

#=== Counts how many questions there are and returns a list of that length ===#
def num_rows():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT COUNT(*) FROM game")
    num = c.fetchone()[0]
    conn.close()
    return num
    """
    l = []
    for x in xrange(num):
        l.append(0)
    """

#=== Get question by rowid - Returns dict containing optA, optB, optAres, optBres ===#
def get_ques(rowid):
    ret_dict = {}
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT * FROM game WHERE rowid = ?", (rowid,))
    ret = c.fetchone()
    ret_dict['optA'] = ret[0]
    ret_dict['optAres'] = ret[1]
    ret_dict['optB'] = ret[2]
    ret_dict['optBres'] = ret[3]
    conn.close()
    return ret_dict

def update_row(rowid, opt):
    if opt == 0:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("UPDATE game SET optAnum = optAnum + 1 WHERE rowid = ?", (rowid,))
        conn.commit()
        conn.close()
    elif opt == 1:
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("UPDATE game SET optBnum = optBnum + 1 WHERE rowid = ?", (rowid,))
        conn.commit()
        conn.close()
