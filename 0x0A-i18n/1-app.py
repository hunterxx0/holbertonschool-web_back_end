#!/usr/bin/env python3
"""
FLask module
"""
from flask import Flask, jsonify, request, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['LANGUAGES'] = ["en", "fr"]
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'


@app.route('/')
def root() -> str:
    """
    root route

    Returns:

    a Welcome message
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
