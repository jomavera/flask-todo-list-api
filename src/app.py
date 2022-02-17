from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]


@app.route('/blabla', methods=['GET'])
def bla():
    return 'Hello, World!'

# @app.route('/todos', methods=['GET'])
# def todos():
#      return "<h1>Hello!</h1>"
    
@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def handle_todos():
    json_t = jsonify(todos)

    return json_t

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)