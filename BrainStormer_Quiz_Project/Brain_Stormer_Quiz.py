from flask import flask

app = Flask (__Quiz_Project__)

@app.route("/")
def home():
	return render_template("Brain_Stormer.html")

@app.route("/")
def home():
	return render_template("Rules.html")

@app.route("/")
def home():
	return render_template("HowToPlay.html")

@app.route("/")
def home():
	return render_template("LetsPlay.html")	

@app.route("/")
def home():
	return render_template("generalknowledge.html")	

@app.route("/")
def home():
	return render_template("filmNtv.html")

@app.route("/")
def home():
	return render_template("worldcultures.html")	

@app.route("/")
def home():
	return render_template("music.html")	



if __name__ == "__main__":
	app.run()


	