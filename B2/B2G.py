from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def combine_functions(functions):
    # Diese Funktion kombiniert eine Liste von Funktionen
    def combined_function(x, y):
        result = 0
        for func in functions:
            result += func(x, y)
        return result
    return combined_function

@app.route('/combine_functions', methods=['POST'])
def endpoint_combine_functions():
    try:
        data = request.json.get('functions')

        if data is not None and isinstance(data, list):
            # Erstellen von Funktionen aus der Liste
            functions = [eval(func) for func in data]

            # Erstellen der kombinierten Funktion
            combined = combine_functions(functions)

            # Rückgabe der kombinierten Funktion als JSON
            return jsonify({'result': str(combined)})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Der Schlüssel "functions" sollte eine Liste von Funktionen sein.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
