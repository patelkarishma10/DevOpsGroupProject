#!flask/bin/python
from flask import Flask, jsonify, make_response
import sys
import requests
from random import randint
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "test"

@app.route('/prizegen', methods=['GET'])
def prize_gen_big():
    chance = randint(0,100)
    prize = 0
    resp = "You didn't win a prize"
    
    if chance >= 70:
        prize = randint(50,100)
        resp = requests.get('http://localhost:9000/notify').content    

    return jsonify({"Prize":prize})

@app.route('/anEndpoint')
def make_request():
    return requests.get('http://example.com').content

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=9017)




