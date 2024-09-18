from flask import Flask, render_template, request, redirect, url_for, flash
import csv

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<string:page_name>")
def hello_world23(page_name):
    return render_template(page_name)

def writeto_server(data):
    with open("database.txt", mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open("database.csv", 'a',newline="") as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        


@app.route('/submit_Form', methods=['POST', 'GET'])
def submit_Form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        return "something went wrong try agian"

