from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []

def add_todo(task):
    # Refactoring: Extraktion der Funktion
    todos.append(task)

@app.route('/add_task', methods=['POST'])
def endpoint_add_task():
    try:
        data = request.json

        if data is not None and 'task' in data:
            task = data['task']

            # Refactoring: Verbesserte Variablennamen
            add_todo(task)

            return jsonify({'result': 'Aufgabe hinzugefügt erfolgreich.'})
        else:
            return jsonify({'error': 'Ungültige Anfrage. Die Anfrage sollte ein Aufgabenfeld enthalten.'}), 400
    except Exception as e:
        return jsonify({'error': f'Ein Fehler ist aufgetreten: {str(e)}'}), 500

@app.route('/get_todos', methods=['GET'])
def endpoint_get_todos():
    # Neue Route für das Abrufen der ToDo-Liste
    return jsonify({'todos': todos})

if __name__ == '__main__':
    app.run(debug=True)
