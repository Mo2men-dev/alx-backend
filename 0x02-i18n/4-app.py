#!/usr/bin/env python3
'''Task 3: Force locale with URL parameter
'''

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    '''Config class'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page.

    Returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''default route'''
    return render_template("2-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
