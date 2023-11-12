from flask import Flask, jsonify

app = Flask(__name__)

def zaehler(startwert):
    # Closure, die den Zustand (startwert) speichert
    aktueller_wert = startwert

    def erhoehe():
        nonlocal aktueller_wert
        aktueller_wert += 1
        return aktueller_wert

    def setze_neuen_wert(neuer_wert):
        nonlocal aktueller_wert
        aktueller_wert = neuer_wert

    def get_aktuellen_wert():
        return aktueller_wert

    return {
        'erhoehe': erhoehe,
        'setze_neuen_wert': setze_neuen_wert,
        'get_aktuellen_wert': get_aktuellen_wert
    }

@app.route('/zaehler', methods=['GET'])
def endpoint_zaehler():
    try:
        # Erstelle einen Zähler mit Startwert 0
        mein_zaehler = zaehler(0)

        # Erhöhe den Zähler und erhalte den aktuellen Wert
        mein_zaehler['erhoehe']()
        aktueller_wert = mein_zaehler['get_aktuellen_wert']()

        return jsonify({'result': aktueller_wert})
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
