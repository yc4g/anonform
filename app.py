#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template, request, session, \
abort

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # Change the host and port name if you want. The default config is port 
    # 5000 on localhost, which you can access by pointing your browser to
    # `localhost:5000`, `127.0.0.1:5000`, or `0.0.0.0:5000`.
    app.run(host='0.0.0.0', port=5000)
