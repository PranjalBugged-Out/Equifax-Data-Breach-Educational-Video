from flask import Flask, request, render_template, jsonify, redirect, url_for
import subprocess
import os
import json
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'demo_only_not_for_production'

# Simulated database
FAKE_DATA = {
    "disputes": [
        {
            "id": "DSP-2017-001",
            "ssn": "123-45-6789",
            "name": "John Doe",
            "dob": "1980-01-01",
            "address": "123 Main St, Anytown, USA",
            "credit_score": 750,
            "dispute_reason": "Incorrect account balance"
        },
        {
            "id": "DSP-2017-002",
            "ssn": "987-65-4321",
            "name": "Jane Smith",
            "dob": "1975-06-15",
            "address": "456 Oak Ave, Somewhere, USA",
            "credit_score": 680,
            "dispute_reason": "Unknown account"
        }
    ]
}

def execute_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dispute-portal')
def dispute_portal():
    return render_template('dispute_portal.html')

@app.route('/attacker')
def attacker():
    return render_template('attacker.html')

@app.route('/api/submit-dispute', methods=['POST'])
def submit_dispute():
    # Vulnerable endpoint simulating Apache Struts
    content_type = request.headers.get('Content-Type', '')
    
    # Simulating the Apache Struts vulnerability
    if '%{' in content_type and '}' in content_type:
        try:
            # Extract command from OGNL expression (simplified for demo)
            cmd_match = re.search(r"#cmd='([^']+)'", content_type)
            if cmd_match:
                cmd = cmd_match.group(1)
                if cmd in ['whoami', 'hostname', 'dir', 'ls', 'ls -la', 'pwd', 'echo "Hello"', 'ver', 'systeminfo']:  # Safe commands for local testing
                    output = '\n'.join(execute_command(cmd).splitlines()[:2])
                    return jsonify({"status": "exploited", "output": output})
                else:
                    return jsonify({"status": "error", "output": "Command not allowed"})
        except Exception as e:
            return jsonify({"error": str(e)})
    
    # Normal dispute submission
    try:
        dispute_data = request.get_json()
        if dispute_data:
            new_id = f"DSP-2017-{str(len(FAKE_DATA['disputes']) + 1).zfill(3)}"
            FAKE_DATA['disputes'].append({
                "id": new_id,
                **dispute_data
            })
            return jsonify({"status": "submitted", "dispute_id": new_id})
    except Exception as e:
        return jsonify({"error": "Invalid request"})

@app.route('/api/disputes', methods=['GET'])
def get_disputes():
    return jsonify(FAKE_DATA)

if __name__ == '__main__':
    import socket
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"\nServer is running on:")
    print(f"- Local URL: http://localhost:5000")
    print(f"- Network URL: http://{local_ip}:5000")
    print("\nUse these URLs to access from your Linux VM")
    app.run(debug=True, port=5000, host='0.0.0.0')
