from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload logic here
    return "File uploaded successfully"

@app.route('/download/<filename>')
def download_file(filename):
    # Add logic to retrieve the file from the database and serve it for download
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(host = '0.0.0.0',debug=True)