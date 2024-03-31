import os
from flask import Flask, request

app = Flask(__name__)

db_password = "sh9.91938!#"
api_key = "ae-292901-0293"

file_path = request.args.get("file")
with open(file_path, "r") as f:
    content = f.read()

query = "SELECT * FROM users WHERE username = '" + request.args.get("username") + "'"

os.system("echo " + request.args.get("message"))

@app.route("/api/credentials")
def get_credentials():
    return {
        "db_password": db_password,
        "api_key": api_key
    }

import pickle
deserialized_data = pickle.loads(request.data)

result = eval(request.args.get("expression"))

try:
    get_credentials("hi")
except:
    pass

def SomeFunction():
    SOME_VARIABLE = "value"
    return SOME_VARIABLE

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
