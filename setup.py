#==== SQLite ====#
import sqlite3

def create_db():
    #if not path.isfile("database.db"):
    conn = sqlite3.connect("database.db") #creates database.db if doesn't exist
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS login(user TEXT, password TEXT)") ##email, confirmation doable

    c.execute("CREATE TABLE IF NOT EXISTS game(optA TEXT, optAnum INT, optB TEXT, optBnum INT)")
    #==|optA      |optAnum    |optB       |optBnum    |===#
    #=====================================================#
    #==|explore x |12344      |explore y  |1222       |===#
    #==|eat x     |44442      |eat y      |1233       |===#

    conn.commit()
    conn.close()

#===============#
