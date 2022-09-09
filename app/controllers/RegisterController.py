from app import app
from flask import render_template, request, redirect, flash
from app import db
from app.models import NewUser

def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        if username == None or password == None or email == None:
            return "Error, missing parameters."
        
        user = NewUser(username=username, password=password, email=email)

        try: 
            user1 = NewUser.query.filter(NewUser.username==username).first()
            user2 = NewUser.query.filter(NewUser.email==email).first()
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."


        if user1 != None or user2 != None:
            return "Existing username or email"
        
        try: 
            db.session.add(user)
            db.session.commit()
        except Exception as err:
            print("Error while connecting to DB.")
            print(err)
            return "Internal server error."
        
        return render_template("login.html")
    return render_template("register.html")