from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True  

@app.route("/input", methods=["POST"])
def confirm():
    user= request.form["user_name"]
    template=jinja_env.get_template("confirm.html")
    return template.render(user_name = user)

@app.route("/")
def index():
    return render_template("input.html")


app.run() 