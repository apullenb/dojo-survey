import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'




@app.route("/", methods=['GET'])
def success():
    return '<h1>Welcome!</h1>'
    
@app.route('/destroy_session')
def reset_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)