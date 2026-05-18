from flask import Flask, render_template
from firebase_functions import https_fn

# Initialize Flask
# We point template_folder to the root if your templates are outside, 
# but for Cloud Functions, it's easiest to keep them handy.
app = Flask(__name__)

@app.route("/")
def home():
    # Your backend Python logic goes here!
    return "This is actually running from app.py backend!"

@app.route("/<path:path>")
def catch_all(path):
    return f"Flask backend caught this route: /{path}"

# This exposes your Flask app to Firebase
@https_fn.on_request()
def kumpix_backend(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()