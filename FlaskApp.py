from flask import Flask
import sentry_sdk
sentry_sdk.init("https://bc07b6a5e8d04bafb2206f26c7177449@sentry.io/1813727")

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# division_by_zero = 1 / 0