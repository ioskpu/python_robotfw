from flask import Flask, jsonify

app=Flask(__name__)

idEntity = 2
people = [
    {
        "id": 1,
        "name": "Juan",
        "lastname": "Pérez",
        "age": 30
    },
    {
        "id": 2,
        "name": "Pedro",
        "lastname": "Gómez",
        "age": 25
    }
]

@app.route('/api/status')
def status():
    """Retorna un status 200"""
    return jsonify({"Status":"ok"})

@app.route('/api/people', methods=['GET'])
def get_people():
    """Retorna la lista de personas"""
    return jsonify(people)

@app.route('/api/people/<int:id>', methods=['GET'])
def get_person(id):
    """Retorna una persona por id"""
    person = next((p for p in people if p['id'] == id), None)
    if person:
        return jsonify(person)
    else:
        return jsonify({"error": "Person not found"}), 404

if __name__=='__main__':
    app.run(host='0.0.0.0')