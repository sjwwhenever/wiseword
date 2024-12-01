from flask import Flask, request, jsonify
from flask_cors import CORS

from uagents.query import query
from uagents import Model
import json

class AIRequest(Model):
    prompt: str


app = Flask(__name__)
# Set CORS to allow your specific frontend origin
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

#openai ask agent address
openai_ask_agent_address = "agent1qdhe4d3ucjusk6s2aw8av3fsj6ulz3ghyp7dsuhux23cq3vkljepxd8ujfl"

@app.route('/')
def home():
    return "Moya, Spirit and Soul!"

@app.route('/api/ask/<topic>', methods=['GET'])
async def ask(topic):
    # Create a response based on the asked topic
    response_message = await query(destination=openai_ask_agent_address, message=AIRequest(prompt=topic), timeout=15.0)
    # Return a JSON response
    data = json.loads(response_message.decode_payload())
    return data

if __name__ == '__main__':
    app.run(debug=True)
