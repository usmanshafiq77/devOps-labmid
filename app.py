from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <body>
            <h1>DevOps Lab - CI/CD Pipeline Working!</h1>
            <p>This is running inside a Docker container.</p>
            <p>Auto-deployed by GitHub Actions!</p>
        </body>
    </html>
    """

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)