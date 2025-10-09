import sqlite3
from flask import Flask, jsonify, render_template, request

DB_NAME = 'periodic_table.db'

app = Flask(__name__)

# A dictionary to hold a single-sentence fact for each element.
# This could be stored in the database, but for this example, a simple

# The route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/combine-page')
@app.route('/about')
def about():
    return render_template('about.html')
def combine_page():
    return render_template('combine.html')
@app.route('/api/elements', methods=['GET'])
def get_all_elements():
    """Fetches all elements from the database and returns them as a JSON list."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM elements')
    elements = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(elements)


@app.route('/api/elements/<string:symbol>', methods=['GET'])
def get_element_detail(symbol):
    """
    Fetches details for a specific element by its symbol,
    including a fun fact.
    """
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM elements WHERE symbol = ?', (symbol,))
    element = cursor.fetchone()
    conn.close()

    if element:
        element_dict = dict(element)
        element_dict['fact'] = ELEMENT_FACTS.get(symbol, 'No fun fact available for this element.')
        return jsonify(element_dict)
    else:
        return jsonify({'error': 'Element not found'}), 404
    
@app.route('/get_more_details', methods=['POST'])
def get_more_details():
    content = request.get_json()
    my_Var = content.get("myVar")

    print(my_Var)

    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM elements WHERE symbol = ?', (my_Var,))
    element = cursor.fetchone()
    conn.close()

    if element:
        element_dict = dict(element)
        element_dict['fact'] = ELEMENT_FACTS.get(my_Var, 'No fun fact available for this element.')
        return jsonify(element_dict)
    else:
        return jsonify({'error': 'Element not found'}), 404


if __name__ == '__main__':
    # You would typically create the database and table here if it doesn't exist
    # For this example, we assume it's already created.
    # The DB structure should be:
    # CREATE TABLE elements (
    #   atomic_number INTEGER PRIMARY KEY,
    #   symbol TEXT NOT NULL,
    #   name TEXT NOT NULL,
    #   atomic_mass REAL,
    #   category TEXT,
    #   xpos INTEGER,
    #   ypos INTEGER,
    #   electron_configuration TEXT,
    #   electronegativity_pauling REAL,
    #   electron_affinity REAL,
    #   density TEXT,
    #   melting_point TEXT,
    #   boiling_point TEXT
    # );
    app.run(debug=True)