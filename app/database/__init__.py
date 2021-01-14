from flask import g
import sqlite3


DATABASE="users"

def get_db():
    db=getattr(g, "_database", None)
    if not db:
        db = g._database = sqlite3.connect(DATABASE)
        return db

def output_formatter(results: tuple):
    out = {"body": []}
    for result in results:
        res_dict = {}
        res_dict["id"] = result[0]
        res_dict["first_name"] = result[1]
        res_dict["last_name"] = result[2]
        res_dict["position"] = result[3]
        res_dict["department"] = result[4]
        res_dict["active"] = result[5]
        out["body"].append(res_dict)
    return out

def scan():
    cursor = get_db().execute("SELECT * FROM users", ())
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)


def read(prod_id):
    query = """ SELECT *
                FROM users
                WHERE id = ?
                """
    cursor = get_db().execute(query, (prod_id,))
    results = cursor.fetchall()
    cursor.close()
    return output_formatter(results)

def update(prod_id, fields: dict):
    field_string = ", ".join(
                    "%s=\"%s\"" % (key, val)
                    for key, val
                    in fields.item())
    query = """
            UPDATE users
            SET %s
            WHERE id = ?
            """ % field_string
    cursor = get_db()
    cursor.execute(query, (prod_id,))
    cursor.commit()
    return True
    

def create(first_name, last_name, postion, department):
    value_tuple = (first_name, last_name, postion, department)
    query = """
            INSERT INTO users (
                first_name,
                last_name,
                position,
                department)
            VALUES (?, ?, ?, ?)
            """
    cursor = get_db()
    last_row_id = cursor.execute(query, value_tuple).lastrowid
    cursor.commit()
    return last_row_id
    

def delete(prod_id):
    query = "DELETE FROM users WHERE id=%s" % prod_id
    cursor = get_db()
    cursor.execute(query, ())
    cursor.commit()
    return True