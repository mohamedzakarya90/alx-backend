#!/usr/bin/env python3
''' Task 6 - Using the user locale
'''

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    ''' The Config Class '''

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """ retrieving user based on the user id
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """ performing the routines before each request is resolutted
    """

    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """ retrieving locale for web page

    returns:
        str: best match
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config["LANGUAGES"]:
        return g.user['locale']
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config["LANGUAGES"]:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    ''' The Default Route

    returns:
        html: homepage
    '''
    return render_template("6-index.html")

# Uncommenting that line and commenting @babel.localeselector
# We get this error ->
# The AttributeError - Babel object has no attribute localeselector
# babel.init_app(app, locale_selector=get_locale)


if __name__ == "__main__":
    app.run()
