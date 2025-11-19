import os
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "service": "Legal OCR API",
        "version": "1.0",
        "status": "operational",
        "endpoints": ["/health", "/api/auto/external-trigger"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    })

@app.route('/api/auto/external-trigger', methods=['POST'])
def webhook():
    try:
        data = request.get_json() or {}
        return jsonify({
            "status": "success",
            "message": "Endpoint working",
            "received_files": len(data.get('files', [])),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
