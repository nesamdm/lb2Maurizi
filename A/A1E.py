from flask import Flask, jsonify

app = Flask(__name__)

# Objektorientierte Programmierung
class Mitarbeiter:
    def __init__(self, name, rolle):
        self.name = name
        self.rolle = rolle

@app.route('/mitarbeiter/oop', methods=['GET'])
def endpoint_mitarbeiter_oop():
    mitarbeiter = Mitarbeiter(name='Max Mustermann', rolle='Entwickler')
    return jsonify({'name': mitarbeiter.name, 'rolle': mitarbeiter.rolle})


# Prozedurale Programmierung
def erstelle_mitarbeiter_prozedural(name, rolle):
    return {'name': name, 'rolle': rolle}

@app.route('/mitarbeiter/prozedural', methods=['GET'])
def endpoint_mitarbeiter_prozedural():
    mitarbeiter = erstelle_mitarbeiter_prozedural(name='Max Mustermann', rolle='Entwickler')
    return jsonify(mitarbeiter)


# Funktionale Programmierung
def erstelle_mitarbeiter_funktional(name, rolle):
    return {'name': name, 'rolle': rolle}

@app.route('/mitarbeiter/funktional', methods=['GET'])
def endpoint_mitarbeiter_funktional():
    mitarbeiter = erstelle_mitarbeiter_funktional(name='Max Mustermann', rolle='Entwickler')
    return jsonify(mitarbeiter)


if __name__ == '__main__':
    app.run(debug=True)
