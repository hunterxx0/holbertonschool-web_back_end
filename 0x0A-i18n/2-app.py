#!/usr/bin/env python3
"""
FLask module
"""
from flask import Flask, jsonify, request, render_template
from flask_babel import Babel
from os import getenv

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    return request.accept_languages.best_match(Config.LANGUAGES)


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
