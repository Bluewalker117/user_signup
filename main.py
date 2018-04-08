from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True  


def valid_user_name(name):    
    if 2 < len(name) < 21:
        return True
    else:
        return False 

# def valid_email_address(email):

def valid_password(password):
    if 2 < len(password) < 21:
        return True
    else:
        return False 

def validate_password(password, password_2):
    if (password) == (password_2):
        return True
    else:
        return False

    

@app.route("/input", methods=["POST"])
def input():
    user = request.form["user_name"]
    email = request.form["email_address"]
    p_word = request.form["new_password"]
    p_word_2 = request.form["verify_password"]

    if user.strip()=="":
        return render_template("input.html", user_name_error = "Please enter a user name.")
    else:
        user = user
        if valid_user_name(user)== False:
            return render_template("input.html", user_name = user, user_name_error = 
        "The name you have entered is not the required 3-20 characters in length.  Please try a new name.")


    if p_word.strip()=="":
        return render_template("input.html", new_password_error = "Please enter a password.")
    if valid_user_name(user) == True:
        return "Yes"
    else:
        return render_template("input.html", new_password = p_word, new_password_error = 
        "The password you have entered is not the required 3-20 characters in length.  Please try a new password.")

    #else:
     #   return render_template("welcome.html", user_name = user)

        




@app.route("/")
def index():
    show_error = request.args.get("error")
    return render_template("input.html", error=show_error)


app.run() 