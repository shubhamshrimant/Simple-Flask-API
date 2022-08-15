# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 10:45:53 2022

@author: shubh
"""

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello():
    return jsonify("Hello World")

if __name__ == '__main__':
    app.run()