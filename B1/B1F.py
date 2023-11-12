from flask import Flask, request, jsonify

app = Flask(__name__)

def funktion_a(input_data):
    # Implementierung von Funktion A
    return input_data * 2

def funktion_b(input_data):
    # Implementierung von Funktion B
    return input_data + 5

def zusammenhaengender_algorithmus(input_data):
    # Funktionen in einen zusammenhängenden Algorithmus integrieren
    ergebnis_a = funktion_a(input_data)
    ergebnis_b = funktion_b(ergebnis_a)
    return ergebnis_b

@app.route('/zusammenhaengender_algorithmus', methods=['POST'])
def endpoint_zusammenhaengender_algorithmus():
    try:
        input_data = request.json.get('input_data')

        if input_data is not None:
            # Aufruf des zusammenhängenden Algorithmus
            ergebnis = zusammenhaengender_algorithmus(input_data)

            # Rückgabe der Ergebnisse als JSON
            return jsonify({'result': ergebnis})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Der Schlüssel "input_data" fehlt.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
