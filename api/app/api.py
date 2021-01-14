from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"


@app.route('/current-storms', methods=['POST'])
def current_storms():
    data = request.get_json()
    storm_resources = data['storms']
    for storm_resource in storm_resources:
        print(storm_resource)
    return "OK"
    

if __name__ == "__main__":
    app.run(host='0.0.0.0')