from flask import Flask, render_template, request, jsonify
import webscraper
import json
import os

app = Flask(__name__)
debug_info_file = "debug_info.json"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle web scraping
        url = request.form.get('url', '')
        tag = request.form.get('tag', '')
        # Ensure that webscraper.scrape_website properly handles the request
        result = webscraper.scrape_website(url, tag)
        return jsonify({'result': result})
    else:
        # Load debug info for GET requests
        debug_info = load_debug_info()
        return render_template('index.html', debug_info=debug_info)

@app.route('/add_debug_info', methods=['POST'])
def add_debug_info():
    data = request.json
    if not data:
        return jsonify({"message": "No data provided"}), 400
    debug_info = load_debug_info()
    debug_info.append(data)
    save_debug_info(debug_info)
    return jsonify({"message": "Debug info added successfully"})

def load_debug_info():
    """ Load debug info from the file """
    if not os.path.exists(debug_info_file):
        return []
    with open(debug_info_file, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_debug_info(debug_info):
    """ Save debug info to the file """
    with open(debug_info_file, "w") as file:
        json.dump(debug_info, file)

# Run the Flask application if the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
