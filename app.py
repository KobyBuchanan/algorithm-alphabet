from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alphabet')
def alphabet():
    letters = [chr(c) for c in range(ord("A"),ord('Z') + 1)]
    return render_template('alphabet.html', letters = letters)

if __name__ == '__main__':
    app.run(debug=True)