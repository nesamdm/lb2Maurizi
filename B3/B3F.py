from flask import Flask, request, jsonify

app = Flask(__name__)

# Lambda-Funktionen für verschiedene Operationen
operationen = {
    'addition': lambda x, y: x + y,
    'subtraktion': lambda x, y: x - y,
    'multiplikation': lambda x, y: x * y,
    'division': lambda x, y: x / y if y != 0 else 'Ungültige Division durch Null'
}

@app.route('/berechne', methods=['POST'])
def endpoint_berechne():
    try:
        data = request.json

        if data is not None and 'operator' in data and 'zahlen' in data and isinstance(data['zahlen'], list):
            operator = data['operator']

            if operator in operationen:
                # Lambda-Ausdruck mit mehreren Argumenten anwenden
                ergebnis = operationen[operator](*data['zahlen'])
                return jsonify({'result': ergebnis})
            else:
                return jsonify({'error': 'Ungültiger Operator.'}), 400
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte Operator und eine Liste von Zahlen enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
