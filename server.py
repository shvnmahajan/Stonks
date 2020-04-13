from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route("/")
@app.route("/index")
def about():
	return render_template("about.html")

@app.route("/recomendation")
def recomendation():
	return render_template("recomendation.html",recomendations=recomendations);

if __name__=="__main__":
	app.run(debug=True)