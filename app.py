from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def respond():
    return 'hello you'

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json);
    return Response(status=200)

if __name__ == '__main__':
    app.run()
