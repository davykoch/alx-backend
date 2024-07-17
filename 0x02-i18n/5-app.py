#!/usr/bin/env python3
"""
Flask app with Babel configuration, locale selector, and mock user login.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union, Dict

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

def get_user() -> Union[Dict, None]:
    """
    Returns a user dictionary or None if ID can't be found or
    if login_as was not passed.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request():
    """
    Use get_user to find a user if any, and set it as a global on flask.g.user.
    """
    g.user = get_user()

@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with a title and header.
    """
    return render_template('5-index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
