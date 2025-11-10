from flask import Flask, jsonify, render_template, request
from app.data import get_top_dividends

app = Flask(__name__, template_folder="../templates")

@app.route("/api/top")
def api_top():
    limit = int(request.args.get("limit", 10))
    return jsonify(get_top_dividends(limit=limit))

@app.route("/")
def index():
    limit = int(request.args.get("limit", 10))
    rows = get_top_dividends(limit=limit)
    return render_template("index.html", rows=rows, limit=limit)

@app.route("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
