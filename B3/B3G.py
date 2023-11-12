from flask import Flask, jsonify

app = Flask(__name__)

# Beispiel-Endpunkt, der eine generische Operation auf zwei Zahlen anwendet
def generischer_endpoint(operation):
    return lambda x, y: jsonify({'result': operation(x, y)})

# Lambda-Funktionen für verschiedene Operationen
quadrat = lambda x, y: x ** y
multiplikation = lambda x, y: x * y
addition = lambda x, y: x + y

# Dynamische Erstellung von Endpunkten
app.add_url_rule('/quadrat', 'quadrat', generischer_endpoint(quadrat), methods=['POST'])
app.add_url_rule('/multiplikation', 'multiplikation', generischer_endpoint(multiplikation), methods=['POST'])
app.add_url_rule('/addition', 'addition', generischer_endpoint(addition), methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
