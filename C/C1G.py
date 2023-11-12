from flask import Flask, request, jsonify

app = Flask(__name__)

def summiere_zahlen(zahlen):
    return sum(zahlen)

def extrahiere_ungeraede_zahlen(zahlen):
    return [zahl for zahl in zahlen if zahl % 2 != 0]

@app.route('/verarbeite_zahlen', methods=['POST'])
def endpoint_verarbeite_zahlen():
    try:
        data = request.json

        if data is not None and 'zahlen' in data and isinstance(data['zahlen'], list):
            zahlen = data['zahlen']

            # Refactoring: Extraktion von Funktionen und verbesserte Variablenbenennung
            summe = summiere_zahlen(zahlen)
            ungerade_zahlen = extrahiere_ungeraede_zahlen(zahlen)

            return jsonify({'summe': summe, 'ungerade_zahlen': ungerade_zahlen})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte eine Liste von Zahlen enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
