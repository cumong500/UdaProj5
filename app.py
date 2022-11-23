from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    html = f"<h3>Welcome to my page! My name is Khanh</h3><h6>App version 2.0.0</h6>"
    return html.format(format)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80
