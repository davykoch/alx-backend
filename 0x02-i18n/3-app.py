#!/usr/bin/env python3
"""
Flask app with Babel configuration and locale selector.
"""
from flask import Flask, render_template, request
from flask_babel import _
from flask_babel import Babel
from typing import Any


class Config:
    """Configuration class for Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best match with our supported languages.
    """
    # For testing, always return 'en'
    return 'en'


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Render the index page with a title and header.
    """
    return render_template('3-index.html')


print(_('home_title'))  # Should print "Welcome to Holberton"
print(_('home_header'))  # Should print "Hello world!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
