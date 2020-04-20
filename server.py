from flask import Flask,render_template
import pandas as pd


##############################  data from csvs

reco_df = pd.read_csv (r'D:/Users/Shravan/Documents/GitHub/Stonks/recos.csv')
recomendations  = reco_df.to_dict('Records')
#print (recomendations)

perf_df = pd.read_csv (r'D:/Users/Shravan/Documents/GitHub/Stonks/performance1.csv')
performance = perf_df.to_numpy()
print(performance)

# recomendations = [
# 	{
# 		'call' : 'buy',
# 		'name' : 'reliance'	
# 	},

# 	{
# 		'call' : 'buy',
# 		'name' : 'sid'	
# 	},

# 	{
# 		'call' : 'sell',
# 		'name' : 'mid'	
# 	}
# ]


##################################  functions

app=Flask(__name__,template_folder='template')

@app.route("/")
@app.route("/about")
def about():
	return render_template("about.html")




@app.route("/recomendation")
def recomendation():
	return render_template("recomendation.html",recos=recomendations);

if __name__=="__main__":
	app.run(debug=True)