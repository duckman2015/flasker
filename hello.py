from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route a decorator 
@app.route('/')

#def index():
#	return "<h1>Hello World!</h1>"  


def index():
	first_name = "John"
	stuff = "This is  Bold Text "

	favorite_pizza = ["cheese","mozzarella","mushrooom"]
	return render_template("index.html",
		first_name=first_name,
		stuff=stuff,
		favorite_pizza = favorite_pizza)

# localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", user_name=name)

# Create Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

#Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
