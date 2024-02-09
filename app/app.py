from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():

	data = {
		'title':'PABLO BAUER',
		'profession':'Filmmaker'
	}

	return render_template('index.html', data=data)

if __name__ == '__main__':
	app.run(debug=True, port=5000)