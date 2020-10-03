from flask import Flask, redirect, url_for, request
from hello import Todo

app = Flask(__name__)

html_str = """
<html>
   <body>
      <form action = "http://localhost:5000/login" method = "get">
         <p>Enter Chore:</p>
         <p>description: <input type = "text" name = "desc" /></p>
         <p>severity:  <input type = "text" name = "severity" /></p>
         <p>done?  <input type = "bool" name = "isDone" /></p>
         <p><input type = "submit" value = "submit" /></p>
      </form>
   </body>
</html>
"""

Html_file = open("login.html", "w")
Html_file.write(html_str)
Html_file.close()


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)
