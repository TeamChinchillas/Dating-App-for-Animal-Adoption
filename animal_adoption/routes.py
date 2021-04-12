from animal_adoption import app


@app.route('/', endpoint='', methods=['GET'])
def login():
    """
    Route for user to login with username and password and receive a JWT token
    in response if credentials are valid
    :return:
    """
    hello = "Hello World"
    return hello
