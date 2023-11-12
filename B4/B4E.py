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
                durchschnittliche_laenge = reduce(
                    lambda x, y: (x[0] * x[1] + y) / (x[1] + 1),
                    map(lambda word: len(word),
                        filter(lambda word: word.startswith('A'), woerter)),
                    (0, 0)  # Anfangswert für die Reduzierung (Summe, Anzahl)
                )
                return jsonify({'result': durchschnittliche_laenge})
            else:
                return jsonify({'error': 'Ungültige Operation.'}), 400
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte eine Operation enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
