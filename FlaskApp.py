from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://bc07b6a5e8d04bafb2206f26c7177449@sentry.io/1813727",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"