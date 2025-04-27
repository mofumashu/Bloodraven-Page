from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/nerissa')
def nerissa():
    return render_template('nerissa.html')

@app.route('/erb')
def erb():
    return render_template('erb.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ← this is important for Railway
    app.run(host='0.0.0.0', port=port)