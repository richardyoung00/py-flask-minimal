from flask import Flask
app = Flask(__name__)

# two decorators, same function
@app.route('/')
def index():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)