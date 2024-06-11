from flask import Flask, render_template, redirect, url_for, session, flash, request
import dbConnect as dbConnect

app = Flask(__name__)


@app.route("/login",methods = ['POST','GET'])
def login():
       if request.method == 'POST':
            uemail = request.form["email"]
            upassword = request.form["password"]
            try:
                 dbConnect.mycursor.execute(
                      f"""SELECT id,name,email FROM user WHERE email = %s AND password = %s""",
                      (uemail,upassword)
                 )
                 user = dbConnect.mycursor.fetchone()
                 if user:
                      session['userid'] = user[0]
                      session['usrname'] = user[1]
                      return redirect(url_for('index'))
                 else:
                      flash('invalid email or password')
                      return render_template('login.html')
            except Exception as e:
                 flash(f"error occurred: {e}, try again later")
       else:
         return render_template("login.html")

if __name__ == "__main__":
     app.run(debug = True)