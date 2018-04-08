from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)

app.config['DEBUG'] = True  


def valid_length(text):    
    if 2 < len(text) < 21:
        return True
    else:
        return False 

# def valid_email_address(email):

#def alphabet_numb(letter):
#    for chara in letter:
#        x = ord(chara)
#        return(x)  

#def is_space(letter):
#    z = alphabet_numb(letter)
#    if z == 32:
#        return True
#    else:
#        return False

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
    
    user_error = ""
    email_error = ""
    p_word_error = ""
    P_word_2_error = ""



    if user.strip()=="":
        user_error = "No"
        return render_template("input.html", email_address = email, user_name_error = "Please enter a user name.")
    else:
        user = user
        if valid_length(user)== False:
            user_error = "No"
            return render_template("input.html", user_name = user, email_address = email, user_name_error = 
        "The name you have entered is not the required 3-20 characters in length.  Please try a new name.")

    if p_word.strip()=="":
        p_word_error = "No"
        return render_template("input.html", user_name = user, email_address = email, new_password_error = 
        "Please enter a password.")
    else:
        p_word = p_word
        if valid_length(p_word)== False:
            p_word_error = "No"
            return render_template("input.html", user_name = user, email_address = email, new_password_error = 
        "The password you have entered is not the required 3-20 characters in length.  Please try a new password.")
        
        
   # if p_word_2()=="":
   #     return render_template("input.html", verify_password_error = "Please re-enter your password for verification.")

    if not user_error and not p_word_error:
        return render_template("welcome.html", user_name = user)

        




@app.route("/")
def index():
    show_error = request.args.get("error")
    return render_template("input.html", error=show_error)


app.run() 