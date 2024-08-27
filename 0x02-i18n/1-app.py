#!/usr/bin/env python3
"""
Task 1: Babel
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)

@app.route("/")
def index():
    """
    defualt route
    """
    return render_template("1-index.html",)

if __name__ == "__main__":
    app.run(debug=True)
