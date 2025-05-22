from flask import Flask, render_template, abort
import json
import renderer

app = Flask(__name__)

with open("static/algorithms_database.json",'r') as file:
    algorithms_database = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alphabet')
def alphabet():
    letters = [chr(c) for c in range(ord("A"),ord('Z') + 1)]
    return render_template('alphabet.html', letters = letters, data=algorithms_database)

@app.route("/<letter>/<algo_key>")
def show_algorithm(letter, algo_key):
    letter = letter.upper()
    
    #validate input
    try:
        algo_data = algorithms_database[letter][algo_key]
    except KeyError:
        abort(404)

    try:
        render_fn_name = algo_data.get("render", f"render_{algo_key.lower()}")
        render_fn = getattr(renderer, render_fn_name)
        image_data = render_fn()

        return render_template(
            "algorithm.html",
            algo_name = algo_data["title"],
            description = algo_data["description"],
            image_data = image_data)
    
    except Exception as e:
        print(e)
        abort(500)


if __name__ == '__main__':
    app.run(debug=True)