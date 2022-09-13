from flask import render_template, request, redirect
from app import db
from app.models import NewUser

def profile():
    user = request.args
    username = user.get("username")
    password = user.get("password")
    email = user.get("email")
    return render_template("profile.html", username=username, password=password, email=email)

def delete():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == None or password == None:
            return "Error, missing parameters."
        
        try: 
            user1 = NewUser.query.filter(NewUser.username==username).first()
            if user1 == None or user1.password != password:
                return "Invalid username or password."
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        try: 
            db.session.delete(user1)
            db.session.commit()
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        
        return render_template("index.html")
    return render_template("delete.html")

def update():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        newUsername = request.form["newUsername"]
        newPassword = request.form["newPassword"]
        newEmail = request.form["newEmail"]

        if username == None or password == None:
            return "Missing required parameters"
        
        try: 
            user1 = NewUser.query.filter(NewUser.username==username).first()
            if user1 == None or user1.password != password:
                return "Invalid username or password."
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        
        if newUsername != None and newUsername != "":
            existingUser = NewUser.query.filter(NewUser.username == newUsername).first()
            if existingUser != None:
                return "Invalid username"
            user1.username = newUsername
        if newPassword != None and newPassword != "":
            user1.password = newPassword
        if newEmail != None and newEmail != "":
            existingUser = NewUser.query.filter(NewUser.email == newEmail).first()
            if existingUser != None:
                return "Invalid email"
            user1.email = newEmail
        
        try: 
            db.session.commit()
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."

        return redirect("/profile/?username="+user1.username+"&password="+user1.password+"&email="+user1.email)
        
    return render_template("update.html")