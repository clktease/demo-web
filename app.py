from flask import Flask, request, render_template, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template("index.html", files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    if f.filename.endswith('.mp3'):
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return '', 204

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
