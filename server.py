import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'



@app.route("/", methods=['GET'])
def success():
    return render_template('index.html')


@app.route('/result', methods=["GET", "POST"])
def process_submission():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return render_template('result.html')

    
@app.route('/destroy_session')
def reset_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=5000)