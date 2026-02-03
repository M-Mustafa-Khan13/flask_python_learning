from flask import Flask,render_template,request


app= Flask(__name__)
app.secret_key="supersecret"   


@app.route("/")

def login():
    return render_template("form_2.html")

@app.route("/submit", methods=['POST'])

def submit():
    username=request.form.get("user-id")
    password=request.form.get("password")

    valid_users={

        'khan':'6027',
        'tareen':'4056',
        'thanh':'7784',
        'alam':'5051'
    }

    if username in valid_users and password==valid_users[username]:
        return render_template("home_2.html",name=username)
    else:
        return render_template("form_2.html", error="Invalid credentials")

@app.route("/about")

def  about():
    return render_template("about2.html")   


if __name__ == "__main__":
    app.run(debug=True)