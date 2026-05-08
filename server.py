from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

FILES_DIR = "files"

@app.route("/")
def home():
    return "Assignment Server Running!"

@app.route("/list")
def list_files():
    files = os.listdir(FILES_DIR)
    return jsonify(files)

@app.route("/files/<filename>")
def get_file(filename):
    return send_from_directory(FILES_DIR, filename)

# NEW VIEW ROUTE
@app.route("/view/<filename>")
def view_file(filename):
    filepath = os.path.join(FILES_DIR, filename)

    if not os.path.exists(filepath):
        return "File not found", 404

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    return f"<pre>{content}</pre>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)