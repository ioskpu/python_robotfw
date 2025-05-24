from flask import Flask, jsonify, request
from h11 import Data

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
    
@app.route('/api/people', methods=['POST'])
def add_person():
    """Agrega una persona"""
    data = request.get_json()
    global idEntity
    new_person = {
        "id": idEntity,
        "name": data.get("name"),
        "lastname": data.get("lastname"),
        "age": data.get("age")
    }
    people.append(new_person)
    idEntity += 1
    return jsonify(new_person), 201

@app.route('/api/people/<int:id>', methods=['PUT'])
def update_person(id):
    """Actualiza una persona por id"""
    data = request.get_json()
    person = next((p for p in people if p['id'] == id), None)
    if person:
        person['name'] = data.get("name", person['name'])
        person['lastname'] = data.get("lastname", person['lastname'])
        person['age'] = data.get("age", person['age'])
        return jsonify(person)
    else:
        return jsonify({"error": "Person not found"}), 404


@app.route('/api/people/<int:id>', methods=['DELETE'])
def delete_person(id):
    """Elimina una persona por id"""
    global people
    people = [p for p in people if p['id'] != id]
    return jsonify({"message": "Person deleted"}), 200

if __name__=='__main__':
    app.run(host='0.0.0.0')