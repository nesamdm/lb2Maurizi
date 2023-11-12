from flask import Flask, request, jsonify

app = Flask(__name__)

personen = [
    {'name': 'Alice', 'alter': 28},
    {'name': 'Bob', 'alter': 22},
    {'name': 'Charlie', 'alter': 35}
]

@app.route('/sortiere_personen', methods=['POST'])
def endpoint_sortiere_personen():
    try:
        data = request.json

        if data is not None and 'kriterium' in data:
            kriterium = data['kriterium']

            if kriterium == 'name':
                # Sortiere nach Namen
                sortierte_personen = sorted(personen, key=lambda x: x['name'])
            elif kriterium == 'alter':
                # Sortiere nach Alter
                sortierte_personen = sorted(personen, key=lambda x: x['alter'])
            else:
                return jsonify({'error': 'Ungültiges Sortierkriterium.'}), 400

            return jsonify({'result': sortierte_personen})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte ein Sortierkriterium enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
