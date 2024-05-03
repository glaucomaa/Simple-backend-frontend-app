from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/api/random', methods=['GET'])
def get_random_number():
    return jsonify({'random_number': random.randint(0, 100)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
