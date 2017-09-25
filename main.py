from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

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
		<form action="/caesar" method="POST">
			<label for="rotate"><h2>Rotate By:</h2></label>
			<input id="rotate" type="text" name="rot" value="0" />
			<textarea rows="5" cols="50" name="text" value="The quick, brown fox jumped over the lazy dog."/>
			<input type="submit" value="Submit Query">
		
		
		</body>
	
</html>

"""


@app.route("/")
def index():
	return form
	
app.run
