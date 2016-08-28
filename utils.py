from os import path
import md5

"""
=== Creates database.db if database is not in the main directory (runs when imported by __init__.py) ===
    Table: game
    #==|optA      |optAnum    |optB       |optBnum    |===#
    #=====================================================#
    #==|explore x |12344      |explore y  |1222       |===#
    #==|eat x     |44442      |eat y      |1233       |===#
"""
if not path.isfile("database.db"):
    conn = sqlite3.connect("database.db") #creates database.db if doesn't exist
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS login(user TEXT, password TEXT)") ##email, confirmation doable
    c.execute("CREATE TABLE IF NOT EXISTS game(optA TEXT, optAnum INT, optB TEXT, optBnum INT)")
    conn.commit()
    conn.close()

"""
=== Hashes password with user ===
Input:
- user - string
- password - string
Returns: hashed password - string
"""
def saltnhash(user,password):
    m = md5.new()
    m.update(user + password)
    return m.hexdigest()

"""
=== Checks if user is in table: login ===
=== Adds user to database.db with password hashed ===
Input:
- user - string
- password - string
Depends on fn: saltnhash(user,password)
Returns:
- True if user is added
- False if user is already taken
"""
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

"""
===Used to authenticate user===
Input:
- user - string
- password - string
Depends on fn: saltnhash(user,password)
Returns:
- True if user+pass matches
- False if user+pass does not match
"""
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

"""
Returns:
- how many rows are in table: game in database.db
"""
def num_rows():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c = c.execute("SELECT COUNT(*) FROM game")
    num = c.fetchone()[0]
    conn.close()
    return num

"""
=== Grabs row from table: game in database.db ===
Input:
- rowid - Integer
Returns:
- Dictionary containing: optionA,optionB,results of each
ex. {'optA': 'eat candy', 'optAres': 24, 'optB': 'eat chips', 'optBres': 17}
"""
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

"""
=== Increments the option number from table: game in database.db ===
Input:
- rowid - Integer
- opt - Integer (0 for optA, 1 for optB)
"""
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
