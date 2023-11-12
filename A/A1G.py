from flask import Flask, request, jsonify

app = Flask(__name__)

# Funktionale Programmierung: Pure Funktion für die Quadratzahl
def berechne_quadratzahl(zahlen):
    return list(map(lambda x: x**2, zahlen))

# Flask-Endpoint für die Quadratzahl-Berechnung
#Gitbash
#curl -X POST -H "Content-Type: application/json" -d '{"zahlen": [2, 4, 6]}' http://127.0.0.1:5000/quadratzahl
@app.route('/quadratzahl', methods=['POST'])
def quadratzahl_endpoint():
    try:
        # Eingabedaten aus dem Request extrahieren
        data = request.get_json()
        zahlen = data.get('zahlen')

        # Funktional: Verwendung der puren Funktion für die Quadratzahl
        ergebnis = berechne_quadratzahl(zahlen)

        # Rückgabe als JSON
        return jsonify({'ergebnis': ergebnis})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    # Flask-App starten
if __name__ == '__main__':
    app.run(debug=True)