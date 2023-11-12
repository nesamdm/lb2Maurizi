from flask import Flask, request, jsonify

app = Flask(__name__)

def addition(x, y):
    return x + y

def multiplikation(x, y):
    return x * y

def berechne(operation, x, y):
    return operation(x, y)

@app.route('/berechne', methods=['POST'])
def endpoint_berechne():
    try:
        data = request.json

        if data is not None and 'operation' in data and 'x' in data and 'y' in data:
            operation = None

            if data['operation'] == 'addition':
                operation = addition
            elif data['operation'] == 'multiplikation':
                operation = multiplikation

            if operation:
                result = berechne(operation, data['x'], data['y'])
                return jsonify({'result': result})
            else:
                return jsonify({'error': 'Ungültige Operation.'}), 400
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte Operation, x und y enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
