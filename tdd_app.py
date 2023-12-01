from flask import Flask, jsonify, request, Response

app = Flask(__name__)
users = {}
next_user_id = 1

@app.route("/users", methods=['GET'])
def get_users():
    return jsonify(list(users.values())), 200

@app.route("/users/<int:user_id>", methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    return (jsonify(user), 200) if user else (jsonify({"error": "User not found"}), 400)

@app.route("/users", methods=['POST'])
def create_user():
    global next_user_id
    data = request.json
    data['id'] = next_user_id
    users[next_user_id] = data
    next_user_id += 1
    return jsonify(data), 201

@app.route("/users/<int:user_id>", methods=['PATCH'])
def update_user(user_id):
    user = users.get(user_id)
    if not user:
        return Response(status=400)
    data = request.json
    user.update(data)
    return Response(status=204)

@app.route("/users/<int:user_id>", methods=['PUT'])
def replace_user(user_id):
    if user_id not in users:
        return Response(status=400)
    data = request.json
    data['id'] = user_id
    users[user_id] = data
    return Response(status=204)

@app.route("/users/<int:user_id>", methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return Response(status=400)
    del users[user_id]
    return Response(status=204)

if __name__ == "__main__":
    app.run(debug=True)
