from flask import render_template, jsonify, Flask, send_file
import requests

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/download')
def test():
	return send_file('./Adde.zip', attachment_filename='Adde.zip',as_attachment= True)

if __name__ == '__main__':
	app.run(debug = True, use_reloader = True)
