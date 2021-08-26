#!/usr/bin/env python3
"""
FLask module
"""
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)


@app.route('/')
def root() -> str:
    """
    root route

    Returns:

    a Welcome message
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
