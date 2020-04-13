from flask import Flask,render_template
app=Flask(__name__,template_folder='template')

@app.route("/")
@app.route("/about")
def about():
	return render_template("about.html")

recomendations = [
	{
		'call' : 'buy',
		'name' : 'reliance'	
	},

	{
		'call' : 'buy',
		'name' : 'sid'	
	},

	{
		'call' : 'sell',
		'name' : 'mid'	
	}
]


@app.route("/recomendation")
def recomendation():
	return render_template("recomendation.html",recos=recomendations);

if __name__=="__main__":
	app.run(debug=True)