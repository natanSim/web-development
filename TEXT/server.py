from flask import Flask, request

app = Flask(__name__)


@app.route('/writeText', methods=['GET'])
def get_user_by_information():
    print(request.args)
    return "Ok"


if __name__ == '__main__':
    app.run()