from flask import Flask,request,redirect,url_for,session,Response


app=Flask(__name__)
app.secret_key="supersecret"   

@app.route("/",methods=["GET","POST"])

def login(): 
    if request.method=="POST":
        username=request.form.get("Username")
        password=request.form.get("Password")

        if username=="admin" and password=="mmk123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials try again",mimetype="text/plain") #text/html
        
    return """
        <h2>Login page</h2>
        <form method="POST">
        username: <input type="text" name="Username" placeholder="Username" required><br>
        password:<input type="password" name="Password" placeholder="Password" required><br>
        <button type="submit">Login</button>
    </form>
    """
# welcome page 
@app.route("/welcome")

def welcome():
    if "user" in session:
        return f'''
        <h2>welcome, {session["user"]}!</h2>
        <a href="{ url_for('logout') }">Logout</a>
'''
    return redirect(url_for("login"))

@app.route("/logout")

def logout():
    session.pop("user", None) # if user not in session none prevents from crashing
    return redirect(url_for("login"))



