#!/usr/bin/env python3
"""
FLask module
"""
from datetime import datetime
from flask import Flask, g, request, render_template
from flask_babel import Babel, format_datetime
from os import getenv
from pytz import timezone, exceptions, all_timezones

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config object
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.before_request
def before_request():
    """
    find a user
    """
    g.user = get_user()
    tmz = get_timezone()
    loc = get_locale()
    if loc == 'fr':
        g.timezone = format_datetime(
            datetime.now(timezone(tmz)),
            'dd MMM yyy à hh:mm:ss')
    else:
        g.timezone = format_datetime(
            datetime.now(timezone(tmz)),
            'MMM dd, yyy, hh:mm:ss a')


@babel.localeselector
def get_locale():
    """
    determine the best match with our supported languages.
    """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.user
    if user:
        loc = user.get('locale')
        if loc and loc in app.config['LANGUAGES']:
            return loc
    locHead = request.headers.get('locale')
    if locHead and locHead in app.config['LANGUAGES']:
        return locHead
    return request.accept_languages.best_match(Config.LANGUAGES)


@babel.timezoneselector
def get_timezone():
    """
    validate that it is a valid time zone.
    """
    try:
        tmz = request.args.get("timezone")
        if tmz:
            try:
                timezone(tmz)
                return tmz
            except:
                raise exceptions.UnknownTimeZoneError
        user = g.user
        if user:
            tmz = user.get('timezone')
            if tmz:
                try:
                    timezone(tmz)
                    return tmz
                except:
                    raise exceptions.UnknownTimeZoneError
    except exceptions.UnknownTimeZoneError:
        return Config.BABEL_DEFAULT_TIMEZONE


@app.route('/')
def root() -> str:
    """
    root route

    Returns:

    a Welcome message
    """
    return render_template('index.html')


def get_user():
    """
    returns a user dictionary
    """
    try:
        uID = int(request.args.get("login_as"))
        return users.get(uID)
    except Exception:
        return None


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
