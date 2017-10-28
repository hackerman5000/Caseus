def main(UID):
    import sqlite3 as sql
    import os.path

    db = sql.connect(r"WineRecords.db")
    cur = db.cursor()

    db.execute("CREATE TABLE IF NOT EXISTS USERS(ID TEXT, NUM INTEGER)")
    cur.execute("SELECT * FROM USERS WHERE ID = {}".format(UID))
    Query = cur.fetchall()

    if len(Query) > 0:
        print("Updating Values in DB for {}".format(UID))
        db.execute("UPDATE USERS SET NUM = NUM + 1 WHERE ID = {};".format(UID))
        db.commit()

    else:
        print("Record for {} not found, Creating one instead...".format(UID))
        db.execute("INSERT INTO USERS VALUES ({}, 0)".format(UID))
        db.commit()

    cur.execute("SELECT * FROM USERS WHERE ID = {}".format(UID))
    vals = cur.fetchall()[0]
    return "*<@{0}> has been given {1} glasses of :wine_glass:!*".format(vals[0], (vals[1]+1))
