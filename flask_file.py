from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        with open('./forms/messages.txt', 'a') as file:
            file.write(f"Name: {name}\n")
            file.write(f"Email: {email}\n")
            file.write(f"Subject: {subject}\n")
            file.write(f"Message: {message}\n")
            file.write(f"Date: {datetime.now()}\n")
            file.write("--------------------\n")
        
        return render_template('index.html')


    
if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8080)