from flask import Flask, render_template
import os

app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/demo')
def layout():
	layoutImg = os.path.join(app.config['UPLOAD_FOLDER'], 'stand.png')
	return render_template('demo.html', layout_image=layoutImg)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')

