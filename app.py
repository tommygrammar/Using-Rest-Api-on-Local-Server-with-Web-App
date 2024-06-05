from flask import Flask, render_template, jsonify
import random

app = Flask(__name__, static_folder='static', template_folder='/home/tommy-grammar/Desktop/risk_management_app/templates')

# API endpoint to fetch the table data
@app.route('/api/data')
def get_data():
    # Simulate AUD/USD OHLC data for multiple days (replace with your actual model logic)
    data = {
        '2024-06-05': {'open': 0.66301, 'high': 0.66728, 'low': 0.66239, 'close': 0.66280},
        '2024-06-04': {'open': 0.66205, 'high': 0.66520, 'low': 0.66185, 'close': 0.66301},
        '2024-06-01': {'open': 0.66250, 'high': 0.66320, 'low': 0.66143, 'close': 0.66205},
        # ... more data for other dates
    }
    return jsonify(data)

# Route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True) 
