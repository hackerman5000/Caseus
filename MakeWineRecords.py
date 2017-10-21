import sqlite3 as sql


def mkDB():
    db = sql.connect("WineRecords.db")
    db.execute("CREATE TABLE USERS(ID TEXT, NUM, INTEGER)")
    db.commit()
    return
