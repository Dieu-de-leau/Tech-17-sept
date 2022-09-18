from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("C:\Users\Karan\Desktop\Virtual-Personal-Assistant-using-Python-master\templatesindex.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	flash("Hi " + str(request.form['0']) + ", great to see you!")
	return render_template("C:\Users\Karan\Desktop\Virtual-Personal-Assistant-using-Python-master\templates\index.html")
