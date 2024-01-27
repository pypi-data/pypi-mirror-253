from flask import Flask, session, g

# local imports
from dash_flask_keycloak import FlaskKeycloak

# Setup server.
server = Flask(__name__)
KEYCLOAK_HOST = 'http://127.0.0.1:5555'
APP_HOST = "http://127.0.0.1"
APP_PORT = 5007
CLIENT_ID = 'keycloak_clients'
REALM_NAME = 'dev'
CLIENT_SECRET_KEY = '2oh5SxbEnMVLeF7c95xfzkGw3wYYMGvJ'
KEYCLOAK_PYTHON_CERT = False

conf = dict(server_url=KEYCLOAK_HOST,
            client_id=CLIENT_ID,
            realm_name=REALM_NAME,
            client_secret_key=CLIENT_SECRET_KEY,
            verify=KEYCLOAK_PYTHON_CERT)

FlaskKeycloak.build(
    server,
    config_data=conf,
    redirect_uri=f"http://127.0.0.1:{APP_PORT}",
)


@server.route("/")
def root_route():
    # Add "logout" button with "redirect_uri/logout" url to the page
    user = session["user"]
    data = session["data"]
    return "Hello {} - calling from {} \n{}".format(user, g.external_url, data)


if __name__ == '__main__':
    server.run(port=APP_PORT)
