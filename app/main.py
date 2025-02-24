from flask import Flask

app = Flask(__name__)

@app.route('/text', methods=['GET'])
def get_text():
    return "Hello from Flask!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
