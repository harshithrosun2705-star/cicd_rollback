from flask import Flask

app = Flask(__name__)

APP_VERSION = "v1"

@app.route("/")
def home():
    return f"CloudMart Mini App - Version {APP_VERSION}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
