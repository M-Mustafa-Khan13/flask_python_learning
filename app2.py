from flask import Flask,request,redirect,url_for,session,Response,render_template


app=Flask(__name__)
app.secret_key="supersecret"   

@app.route("/")

def login():
    return render_template("login.html")

@app.route("/submit",methods=["POST"])

def submit():
    username=request.form.get("username")
    password=request.form.get("password")

    # if username=="Mustafa_khan" and password=="MMK":
    #     return render_template("welcome.html",name=username )
    # else:
    #     return "invalid credentials"

    # for multiple credentials

    valid_users={
        'Admin': '123',
        'rahil': '456',
        'khan':'6027'
    }

    if username in valid_users and password==valid_users[username]:
        return render_template("welcome.html",name=username)
    else:
        return 'invalid username or password!'