#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# A very simple Flask Hello World app for you to get started with...

import flask
from flask import Flask, request

app = Flask(__name__, static_folder="static", static_url_path="", template_folder="templates")

@app.route('/')
def root():
    return flask.render_template(
        'index.html'
    )

def egcd (a: 'int', b: 'int') -> 'tuple' :
    if b == 0:
        return 1,0,a
    else:
        x, y, z = egcd(b, a % b)
        return y, x - a // b * y, z
    
@app.route('/egcd', methods = ['GET'])
def index_egcd():
    if request.method == 'GET':
        a_param=request.args.get('a')
        b_param=request.args.get('b')
    check_param=''
    if a_param==None or b_param==None:
        a_param=0
        b_param=0
        check_param='Не хватает входных данных :('
    if check_param=='':
        result=str(egcd(int(a_param),int(b_param)))
    else:
        result=check_param

    return flask.render_template(
        'egcd.html',
        egcd=result
    )

if __name__ == '__main__':
   app.run(debug = True)
