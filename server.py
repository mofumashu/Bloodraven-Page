from flask import Flask, render_template

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
    app.run(debug=True)