from flask import Flask, request,render_template, redirect, session,url_for,flash
import dbConnect as dbConnect
import blogDbConnect as blogDbConnect


app = Flask(__name__)

app.secret_key = '@23Fl*aswerjjfiJI(L$)'

# ---Native route---

@app.route("/")
def index():
    #query for the current blog
    blogDbConnect.blogcursor.execute(
        f"""SELECT * FROM blogcontent ORDER BY id DESC """
    )

    blogs = blogDbConnect.blogcursor.fetchall()
 
    print(blogs)
      
    return render_template("index.html", blogs=blogs)


# --- Blog submission process ---
@app.route("/blog",methods = ['POST','GET'])
def blog():
    if request.method == "POST":
           bloggername = request.form["name"]
           blogtype = request.form["topic"]
           blogcontent = request.form["content"]
           try:
               blogDbConnect.blogcursor.execute(
                     f"""INSERT INTO blogcontent (name,topic,writing) VALUES (%s,%s,%s)""",(bloggername,blogtype,blogcontent) 
               )
               blogDbConnect.blogconnection.commit()
               flash("blog is successfully submitted")
               return redirect(url_for("index"))
           except Exception as e:
               flash("could not submit the blog")
    else:   
          return render_template("blog.html")
    
# ---Registration process--- 

@app.route("/signup", methods = ["POST","GET"])
def signup():
    if request.method == "POST":
         uname = request.form["username"]
         uemail = request.form["email"]
         upassword = request.form["password"]
         try:
             dbConnect.mycursor.execute(
                  f"""  INSERT INTO user (name,email,password) VALUES (%s,%s,%s)""",(uname,uemail,upassword)
             )
             dbConnect.connection.commit()
             flash('signup successful')
             return redirect(url_for("login"))
         except Exception as e:
             flash('signup failed')
             print(f"error occured {e}")
    else:  
     return render_template('signup.html')
    
# ---Authentication Process---    
            
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

# ---Logut process---

@app.route("/logout")
def logout():
     session.pop('userid','None')
     session.pop('username','None')
     flash("you have been logged out")
     return redirect(url_for('index'))
if __name__ == "__main__":
  app.run(debug=True)
