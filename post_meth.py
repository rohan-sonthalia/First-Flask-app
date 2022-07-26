from flask import Flask, request, url_for, redirect

app = Flask("__name__")

@app.route('/')
def fault():
    return "Welcome to my API"

@app.route('/success/<name>')
def success(name):
    return "Welcome %s" % name

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST' :
        username = request.form['username']
        return redirect(url_for('success', name = username))
    else :
        username = request.args.get('username')
        return redirect(url_for('success', name = username))

app.run(host='0.0.0.0', port=81, debug=True)