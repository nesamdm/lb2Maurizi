from collections import namedtuple
from flask import Flask, request, jsonify

app = Flask(__name__)

#gitbash curl statement
#curl http://127.0.0.1:5000/benutzer
#curl -X PUT -H "Content-Type: application/json" -d '{"Vorname": "Eva", "Nachname": "Neu"}' http://127.0.0.1:5000/benutzer/1

Benutzer = namedtuple('Benutzer', ['id', 'vorname', 'nachname'])
benutzerdaten = [
    Benutzer(1, 'Max', 'Mustermann'),
    Benutzer(2, 'Maria', 'Musterfrau'),
    Benutzer(3, 'John', 'Doe')
]

@app.route('/benutzer', methods=['GET'])
def get_benutzer():
    return jsonify([benutzer._asdict() for benutzer in benutzerdaten])


@app.route('/benutzer/neu', methods=['POST'])
def add_benutzer():
    new_benutzer = request.get_json()

    # Create a new Benutzer instance and append it to the benutzerdaten list
    benutzerdaten.append(
        Benutzer(id=len(benutzerdaten) + 1, vorname=new_benutzer.get('Vorname'), nachname=new_benutzer.get('Nachname')))

    return jsonify({'message': 'Benutzer hinzugefügt'}), 201


@app.route('/benutzer/<int:user_id>', methods=['PUT'])
def update_benutzer(user_id):
    global benutzerdaten

    existing_user_data = benutzerdaten[user_id - 1]

    if isinstance(existing_user_data, Benutzer):
        return jsonify({'error': 'Unveränderliche Werte: Benutzerdaten können nicht direkt geändert werden.'}), 400
    else:
        updated_benutzer = request.get_json()

        # Create a new list with the updated values
        updated_benutzerdaten = benutzerdaten.copy()
        updated_benutzerdaten[user_id - 1] = Benutzer(*(updated_benutzer.values()))

        # Replace the entire benutzerdaten list with the updated one
        benutzerdaten = updated_benutzerdaten

        return jsonify({'message': 'Benutzerdaten aktualisiert'}), 200

if __name__ == '__main__':
    app.run(debug=True)