"""
Flask web interface for Agent WellCare.
Provides a simple web UI to interact with the ADK agent.
"""

import os
from flask import Flask, render_template, request, jsonify
from google.genai import Client
from agent import interactive_wellcare_agent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Initialize ADK client
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

client = Client(api_key=api_key)

# Store active sessions (in production, use a proper database)
sessions = {}

@app.route('/')
def index():
    """Serve the main chat interface."""
    return render_template('index.html')

@app.route('/start_session', methods=['POST'])
def start_session():
    """Start a new agent session."""
    try:
        # Create a new agent session
        session = client.agents.create(interactive_wellcare_agent)
        session_id = session.id if hasattr(session, 'id') else str(id(session))
        sessions[session_id] = session
        
        # Get initial greeting
        greeting = "Hello! I'm Agent WellCare, your compassionate mental health support assistant. How can I help you today?"
        
        return jsonify({
            'session_id': session_id,
            'response': greeting
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/send_message', methods=['POST'])
def send_message():
    """Send a message to the agent and get response."""
    try:
        data = request.json
        session_id = data.get('session_id')
        message = data.get('message')
        
        if not session_id or not message:
            return jsonify({'error': 'Missing session_id or message'}), 400
            
        if session_id not in sessions:
            return jsonify({'error': 'Invalid session_id'}), 400
            
        # Send message to agent
        session = sessions[session_id]
        response = session.send_message(message)
        
        return jsonify({
            'response': response.text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/end_session', methods=['POST'])
def end_session():
    """End an agent session."""
    try:
        data = request.json
        session_id = data.get('session_id')
        
        if session_id in sessions:
            del sessions[session_id]
            
        return jsonify({'status': 'success'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Agent WellCare Web Interface...")
    print("Open your browser to http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)