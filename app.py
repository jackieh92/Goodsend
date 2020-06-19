import os
from firebase_admin import credentials, firestore, initialize_app
from flask import Flask
app = Flask(__name__)
# Initialize Firestore DB
cred = credentials.Certificate('./goodsend/key.json')
default_app = initialize_app(cred)
db = firestore.client()
ben_ref = db.collection('beneficiary')
field_create = {
    "name": "test",
    "email": "testmail@test.com",
}
ben_ref.document().create(field_create)
@app.route('/add', methods=['POST'])
def create():
    """
        create() : Add document to Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post'}
    """
    try:
        id = request.json['id']
        ben_ref.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/list', methods=['GET'])
def read():
    """
        read() : Fetches documents from Firestore collection as JSON
        todo : Return document that matches query ID
        all_todos : Return all documents
    """
    try:
        # Check if ID was passed to URL query
        ben_id = request.args.get('id')    
        if ben_id:
            ben = ben_ref.document(ben_id).get()
            return jsonify(ben.to_dict()), 200
        else:
            all_bens = [doc.to_dict() for doc in ben_ref.stream()]
            return jsonify(all_bens), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/update', methods=['POST', 'PUT'])
def update():
    """
        update() : Update document in Firestore collection with request body
        Ensure you pass a custom ID as part of json body in post request
        e.g. json={'id': '1', 'title': 'Write a blog post today'}
    """
    try:
        id = request.json['id']
        ben_ref.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
@app.route('/delete', methods=['GET', 'DELETE'])
def delete():
    """
        delete() : Delete a document from Firestore collection
    """
    try:
        # Check for ID in URL query
        ben_id = request.args.get('id')
        ben_ref.document(ben_id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
if __name__ == "__main__":
    app.run(debug = True)
    