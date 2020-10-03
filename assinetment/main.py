import json

from flask import Flask, redirect, url_for, request, jsonify, render_template
from hello import Todo

app = Flask(__name__)

html_str = """
<html>
   <body>
      <form action = "http://localhost:5000/login" method = "post">
         <p>Enter Chore:</p>
         <p>description: <input type = "text" name = "desc" /></p>
         <p>severity:  <input type = "text" name = "severity" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
"""

Html_file = open("login.html", "w")
Html_file.write(html_str)
Html_file.close()


@app.route('/login', methods=['POST'])
def create_file():
    user_input = request.form
    chore = Todo(user_input["desc"], user_input["severity"])
    with open(fr"C:\Users\Amir\PycharmProjects\assinetment\{chore.get_uuid()}.json", "w") as f:
        json.dump(chore.to_json(), f)
    return "True"


if __name__ == '__main__':
    app.run(debug=True)
