from flask import Flask

app= Flask(__name__)

@app.route('/')
def testme():
    return "Welcome to the flask application"    

if __name__ == '__main__':
     app.run(port=10001)