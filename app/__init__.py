from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/resources', methods=['POST'])
def create_resource():
    data = request.json
    resource = Resource(name=data['name'], quantity=data['quantity'])
    db.session.add(resource)
    db.session.commit()
    return jsonify({"id": resource.id}), 201

@app.route('/resources', methods=['GET'])
def get_resources():
    resources = Resource.query.all()
    return jsonify([{"id": r.id, "name": r.name, "quantity": r.quantity} for r in resources])

@app.route('/resources/<int:id>', methods=['PUT'])
def update_resource(id):
    resource = Resource.query.get(id)
    if not resource:
        return jsonify({"error": "Not found"}), 404
    data = request.json
    resource.name = data['name']
    resource.quantity = data['quantity']
    db.session.commit()
    return jsonify({"message": "Updated"})

@app.route('/resources/<int:id>', methods=['DELETE'])
def delete_resource(id):
    resource = Resource.query.get(id)
    if not resource:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(resource)
    db.session.commit()
    return jsonify({"message": "Deleted"})
