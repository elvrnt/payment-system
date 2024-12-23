from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    print(f"LOG: {data}")
    return jsonify({'status': 'logged'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5044)
