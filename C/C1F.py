from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)

def analyse_haeufigkeit_woerter(woerter):
    # Refactoring: Extraktion von Funktionen
    woerter_kleingeschrieben = normalisiere_woerter(woerter)
    haeufigkeiten = zaehle_haeufigkeiten(woerter_kleingeschrieben)
    return haeufigkeiten

def normalisiere_woerter(woerter):
    return [wort.lower() for wort in woerter]

def zaehle_haeufigkeiten(woerter):
    return Counter(woerter)

@app.route('/analyse_woerter', methods=['POST'])
def endpoint_analyse_woerter():
    try:
        data = request.json

        if data is not None and 'woerter' in data and isinstance(data['woerter'], list):
            woerter = data['woerter']

            # Refactoring: Verbesserte Variablennamen und klare Struktur
            haeufigkeiten = analyse_haeufigkeit_woerter(woerter)

            return jsonify({'haeufigkeiten': haeufigkeiten})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte eine Liste von Wörtern enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
