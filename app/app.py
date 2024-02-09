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

@app.route('/products')
def products():

	data = {
		'title':'PABLO BAUER',
		'profession':'Filmmaker',
		'area':'products'
	}

	return render_template('products.html', data=data)

@app.route('/travels')
def travels():

	data = {
		'title':'PABLO BAUER',
		'profession':'Filmmaker',
		'area':'travels'
	}

	return render_template('travels.html', data=data)

@app.route('/portraits')
def portraits():

	data = {
		'title':'PABLO BAUER',
		'profession':'Filmmaker',
		'area':'portraits'
	}

	return render_template('portraits.html', data=data)

if __name__ == '__main__':
	app.run(debug=True, port=5000)