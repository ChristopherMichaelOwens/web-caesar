from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True

form = """
<!doctype html>

	<html>
		<head>
			<style>
				form{
				background-color: #eee;
				padding 20px;
				margin: 0 auto;
				width: 540 px;
				font: 16px sans-serif;
				border-radius: 10px;
				
				}
			textarea {
				margin: 10px 0;
				width: 540px;
				height: 120px;
				}
			</style>
		</head>
		<body>
		<!---create your form here -->
		<form action="/" method="POST">
			<label for="rotate"><h2>Rotate By:</h2></label>
			<input id="rotate" type="text" name="rot" value="0" />
			<textarea rows="5" cols="50" name="text" >TheQuick</textarea>
			<input type="submit" value="Submit Query"/>
		
		
		</body>
	
</html>

"""




@app.route("/")
def index():
	return form
	
@app.route("/", methods=['POST'])
def encrypt():
	rotation = int(request.form['rot'])
	text = str(request.form['text'])
	
	return "<h1>" + rotate_string(text, rotation) + "</h1>"
	
	
	
app.run()
