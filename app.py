from flask import Flask, render_template, request
from recognizer.detector import detect_faces
from recognizer.encoding import encode_known_faces
import os

app = Flask(__name__)

known_faces = encode_known_faces()

@app.route("/", methods=["GET", "POST"])
def index():
    names = []
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file:
            filepath = os.path.join("uploads", uploaded_file.filename)
            uploaded_file.save(filepath)
            names = detect_faces(filepath, known_faces)
    return render_template("index.html", names=names)

if __name__ == "__main__":
    app.run(debug=True)
