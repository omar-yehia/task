import flask

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    try:
        jsonInput=flask.request.json
    except:
        return errorNotJson()

    try:
        a=int(jsonInput['a'])
        b=int(jsonInput['b'])
    except:
        return errorNotNumber()

    data = {
        "code":1,
        "message":'success',
        "data":{
            "a*b": a*b,
            "a/b": a/b,
            "a-b": a-b,
            "a+b": a+b,
        }
    }
    return flask.jsonify(data) 

def errorNotJson():
    data = {
        "code":0,
        "message":'parameters must be in json format',
        "data":{}
    }
    return flask.jsonify(data)

def errorNotNumber():
    data = {
        "code":0,
        "message":'incorrect input format',
        "data":{}
    }
    return flask.jsonify(data)

if __name__ == '__main__':
    app.run()
