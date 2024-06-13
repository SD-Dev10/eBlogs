import mysql.connector 


def dbconnect():
    try:
          db = mysql.connector.connect(
          database='credentials',
          user='root',
          passwd='root',
          host='localhost',
          port='3306',
          auth_plugin='mysql_native_password',
       )

    except Exception as e:
        print(f"""DB Connection failed, error ==> {e}""")

    else:
        return db.cursor(),db

mycursor,connection = dbconnect()

 
# mycursor.execute(f"""
#    SELECT * FROM USER
# """)    
# data = list(mycursor.fetchall())
# print(data)


