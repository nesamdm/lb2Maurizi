from flask import Flask, jsonify, request

app = Flask(__name__)


def summe_von_zahlen(zahlen):
    """
    Diese Funktion berechnet die Summe von Zahlen in einer Liste.

    :param zahlen: Eine Liste von Zahlen.
    :return: Die Summe der Zahlen.
    """
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe


@app.route('/summe', methods=['POST'])
def berechne_summe():
    try:
        data = request.get_json()
        zahlen_liste = data.get('zahlen')
        ergebnis = summe_von_zahlen(zahlen_liste)
        return jsonify({'ergebnis': ergebnis})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Beispielaufruf über cURL:
# curl -X POST -H "Content-Type: application/json" -d '{"zahlen": [1, 2, 3, 4, 5]}' http://127.0.0.1:5000/summe

if __name__ == '__main__':
    app.run(debug=True)
