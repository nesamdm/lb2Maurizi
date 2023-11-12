from flask import Flask, request, jsonify
from functools import reduce

app = Flask(__name__)

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@app.route('/verarbeite_zahlen', methods=['POST'])
def endpoint_verarbeite_zahlen():
    try:
        data = request.json

        if data is not None and 'operation' in data:
            operation = data['operation']

            if operation == 'map':
                # Anwendung der Map-Funktion
                transformierte_zahlen = list(map(lambda x: x * 2, zahlen))
                return jsonify({'result': transformierte_zahlen})
            elif operation == 'filter':
                # Anwendung der Filter-Funktion
                gefilterte_zahlen = list(filter(lambda x: x % 2 == 0, zahlen))
                return jsonify({'result': gefilterte_zahlen})
            elif operation == 'reduce':
                # Anwendung der Reduce-Funktion
                summe = reduce(lambda x, y: x + y, zahlen)
                return jsonify({'result': summe})
            else:
                return jsonify({'error': 'Ungültige Operation.'}), 400
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte eine Operation enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
