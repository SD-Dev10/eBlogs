import mysql.connector

def blogconnect():
    try:
          db = mysql.connector.connect(
          database='blogs',
          user='root',
          passwd='root',
          host='localhost',
          port='3306',
          auth_plugin='mysql_native_password',
       )
    except Exception as e:
         print(f"""DB Connection failed, error ==> {e}""")
    else:
        return db.cursor(), db


blogcursor, blogconnection = blogconnect() 