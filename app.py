from flask import Flask,render_template
PORT= 2000
app = Flask(__name__,template_folder='template')

@app.route("/") 
def index(): 
	return render_template("stories.html")
	return render_template("stories.html")

@app.route("/recipes") 
def recipes(): 
	return render_template("recipes.html")

if __name__ == "__main__": 
	app.run(debug=True, host = '0.0.0.0', port=PORT) 
	