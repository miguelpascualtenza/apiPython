from flask import Flask, request, jsonify
from flask_cors import CORS
import tracker

app= Flask(__name__)
CORS(app)

@app.route('/')
def root():
     return "Hello, World!"
    

@app.route('/track')
def track():
    url = request.args.get("url")
    #url = "https://amzn.eu/d/j64pPdb"
    if url:
        data = tracker.obtener_datos(url)
        if 'error' in data:
            return jsonify(data), 500
        else:
            return jsonify(data), 200
    else:
        return jsonify({'error': 'URL parameter is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
