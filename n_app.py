# ---- Flask Hello World ---- #

# import the Flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

@app.route("/integer/<int:value>")
def int_type(value):
	print(value + 1)
	return "correct"

@app.route("/float/<float:value>")
def float_type(value):
	print(value + 1)
	return "correct"

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print(value)
	return "correct"



# start the development server using the run() method
if __name__ == "__main__":
	app.run()

