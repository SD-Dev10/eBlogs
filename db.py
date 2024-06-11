import app as app
import dbConnect as dbConnect


class dbTable:
    name = app.request.form["username"]
    email = app.request.form["email"]
    password = app.request.form["password"]

    def __init__(self, name, email, password):
        name = self.name
        email = self.email
        password = self.password

def dbTableSturct():
    userDb = dbTable()
    return userDb

dbConnect.execute()