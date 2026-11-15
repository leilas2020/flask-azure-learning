from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello from Azure!</h1>
    <p>My first Flask app is running in the cloud.</p>
    """
