from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True  


def valid_user_name(name):    
    if 2 < len(name) < 21:
        return True
    else:
        return False 

@app.route("/input", methods=["POST"])
def test():
    user = request.form["user_name"]
    user_name_error = "Ooooops!"
    if user.strip()=="":
        return "Please enter a user name."
    if valid_user_name(user) == True:
        return "success"
    else:
        return "The name you have entered is not the required 3-20 characters in length.  Please try a new name."

#@app.route("/input", methods=["POST"])
#def input():
#    user= request.form["user_name"]
#    if user.strip()=="":
#        error="Please enter a user name."
#        return redirect("/?error" + error)


 #   template=jinja_env.get_template("confirm.html")
  #  return template.render(user_name = user)

@app.route("/error", methods=["GET"])
def error():
    return "<p>Error.</p>"




@app.route("/")
def index():
    show_error = request.args.get("error")
    return render_template("input.html", error=show_error)


app.run() 