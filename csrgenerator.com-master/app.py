#!/usr/bin/env python

import os

from flask import Flask, request, Response, render_template, send_file

from csr import CsrGenerator

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/security')
def security():
    return render_template('security.html')


@app.route('/generate', methods=['POST'])
def generate_csr():
    csr = CsrGenerator(request.form)
    response = b'\n'.join([csr.csr, csr.private_key])
    fp = open('/home/sysadmin/Downloads/pueba1.csr', 'w')
    csr_CA = str(csr.csr)
    nremove = csr_CA.replace('\\n', '')
    fp.write(nremove[1:])
    fp.close()

    pk = open('/home/sysadmin/Downloads/pueba1.csr.keyID', 'w')
    csr_CA_key = str(csr.private_key)
    nremove_key = csr_CA_key.replace('\\n', '')
    pk.write(nremove_key[1:])
    pk.close()
    return Response(response, mimetype='text/plain')


if __name__ == '__main__':
    port = int(os.environ.get('FLASK_PORT', 5555))
    app.run(host='0.0.0.0', port=port)
