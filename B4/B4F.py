from flask import Flask, request, jsonify
from functools import reduce

app = Flask(__name__)

woerter = ['Apfel', 'Banane', 'Kirsche', 'Mango', 'Erdbeere']

@app.route('/verarbeite_woerter', methods=['POST'])
def endpoint_verarbeite_woerter():
    try:
        data = request.json

        if data is not None and 'operation' in data:
            operation = data['operation']

            if operation == 'kombination':
                # Kombination von Map, Filter und Reduce
                result = reduce(lambda x, y: x + y,
                                map(lambda word: word.upper(),
                                    filter(lambda word: len(word) > 5, woerter)))
                return jsonify({'result': result})
            else:
                return jsonify({'error': 'Ungültige Operation.'}), 400
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte eine Operation enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
