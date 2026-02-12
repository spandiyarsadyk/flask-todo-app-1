from flask import Flask
import os

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["DEBUG"] = os.getenv("DEBUG") == "True"

@app.route("/")
def home():
    return f"Environment: {'DEV' if app.config['DEBUG'] else 'PROD'} 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

