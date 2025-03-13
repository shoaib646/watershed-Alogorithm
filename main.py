import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a sample Python project with Flask!"

if __name__ == "__main__":
    app.run(debug=True)
