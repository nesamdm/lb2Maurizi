from flask import Flask, request, jsonify

app = Flask(__name__)

def berechne_quadrat(input_data):
    return input_data ** 2

def berechne_kubik(input_data):
    return input_data ** 3

def berechne_summe(input_data):
    return sum(input_data)

def durchschnitt_berechnen(input_data):
    return sum(input_data) / len(input_data) if len(input_data) > 0 else 0

def kombinierte_operation(input_data):
    # Berechnung des Quadrats
    quadrat_resultat = berechne_quadrat(input_data)

    # Berechnung des Kubiks
    kubik_resultat = berechne_kubik(input_data)

    # Berechnung der Summe
    summe_resultat = berechne_summe(input_data)

    # Berechnung des Durchschnitts
    durchschnitt_resultat = durchschnitt_berechnen(input_data)

    # Gesamtergebnis
    gesamtergebnis = {
        'quadrat': quadrat_resultat,
        'kubik': kubik_resultat,
        'summe': summe_resultat,
        'durchschnitt': durchschnitt_resultat
    }

    return gesamtergebnis

@app.route('/kombinierte_operation', methods=['POST'])
def endpoint_kombinierte_operation():
    try:
        input_data = request.json.get('input_data')

        if input_data is not None and isinstance(input_data, list):
            # Aufruf der kombinierten Operation
            ergebnis = kombinierte_operation(input_data)

            # Rückgabe der Ergebnisse als JSON
            return jsonify({'result': ergebnis})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Der Schlüssel "input_data" sollte eine Liste von Zahlen sein.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
