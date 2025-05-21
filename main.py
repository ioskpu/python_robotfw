from flask import Flask, jsonify, request

app=Flask(__name__)

@app.route('/status')
def status():
    return jsonify({"Status":"ok"})

if __name__=='__main__':
    app.run(host='0.0.0.0')