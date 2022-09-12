from app import app
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser

def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        if username == None or username == "" or password == None or password == "" or email == None or email == "":
            return "Invalid parameters"
        
        try:
            user1 = NewUser.query.filter(NewUser.username == username).first()
            user2 = NewUser.query.filter(NewUser.email == email).first()
        except Exception as err:
            print(err)
            return("Internal server error.")
        
        if user1 != None or user2 != None:
            return "Existing username or email. Try again."

        #if not validPassword(password):
        #    return "Invalid password."
        
        newUser = NewUser(username=username, email=email, password=password)

        try:
            db.session.add(newUser)
            db.session.commit()
        except Exception as err:
            print(err)
            return("Internal server error.")
        return redirect("/login")

    return render_template("register.html")
