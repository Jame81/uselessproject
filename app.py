from flask import Flask, send_file, render_template_string
from pathlib import Path

app = Flask(__name__)

@app.route('/')
def home():
    # Read the HTML file
    html_path = Path('index.html')
    with open(html_path, 'r') as f:
        return render_template_string(f.read())

@app.route('/BAZOOKA.ttf')
def font():
    return send_file('BAZOOKA.ttf', mimetype='font/ttf')

if __name__ == '__main__':
    app.run(debug=True)

