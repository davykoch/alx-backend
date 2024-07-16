#!/usr/bin/env python3
"""
Basic Flask app with a single route and template.
"""
from flask import Flask, render_template
from typing import Any


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> Any:
    """
    Render the index page with a title and header.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
