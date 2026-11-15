from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1>Welcome to My Cloud App!</h1>
<h2>My name is Leila.</h2>
<p>This website is hosted on Microsoft Azure.</p>
<p>Deployed automatically from GitHub!</p>
"""
