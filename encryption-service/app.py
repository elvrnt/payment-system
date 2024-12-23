from flask import Flask, request, jsonify

app = Flask(__name__)

LOGGING_URL = "http://logging-service:5044/log"

def log_event(event, status):
    payload = {"event": event, "status": status}
    try:
        requests.post(LOGGING_URL, json=payload)
    except Exception as e:
        print(f"Failed to log event: {e}")

@app.route('/encrypt', methods=['POST'])
def encrypt():
    log_event("Encryption started", "info")
    data = request.json['card_info']
    encrypted = f"encrypted-{data}"  # Simulated encryption
    log_event("Data encrypted successfully", "success")
    return jsonify({'encrypted': encrypted})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted = request.json['encrypted']
    if encrypted.startswith("encrypted-"):
        decrypted = encrypted.replace("encrypted-", "")
        return jsonify({'card_info': decrypted})
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
