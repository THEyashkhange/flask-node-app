from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/api/submit', list=['POST'])
def handle_submit():
    data = request.json
    name = data.get('name')
    email = data.get('email')

    return jsonify({
        "status": "success",
        "message": f"Data received for {name} ({email}) successfully!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
