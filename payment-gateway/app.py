from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

encryption_service_url = os.getenv("ENCRYPTION_SERVICE_URL")

LOGGING_URL = "http://logging-service:5044/log"

def log_event(event, status):
    payload = {"event": event, "status": status}
    try:
        requests.post(LOGGING_URL, json=payload)
    except Exception as e:
        print(f"Failed to log event: {e}")

@app.route('/pay', methods=['POST'])
def process_payment():
    log_event("Payment processing started", "info")
    data = request.json
    encrypted_data = data['encrypted_data']
    
    # Simulate payment processing
    decrypted_data = requests.post(f"{encryption_service_url}/decrypt", json={'encrypted': encrypted_data}).json()
    if decrypted_data['card_info']:
        log_event("Payment processed successfully", "success")
        return jsonify({'status': 'success'})
    else:
        log_event(f"Payment processing error: {e}", "error")
        return jsonify({'status': 'failed'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
