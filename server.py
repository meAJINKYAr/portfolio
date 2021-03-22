from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)

#print(__name__)
@app.route('/')
def my_home():
    return render_template('index.html')

""" @app.route('/<username>/<int:post_id>')
def display_user(username=None,post_id=None):
    return render_template('user.html',name=username,id=post_id)
 """
@app.route('/<string:page_name>')
def show_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    database = open('database.txt','a')
    email = data['email']
    subject = data['subject']
    message = data['message']
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    csvdb = open('database.csv','a',newline='')
    email = data['email']
    subject = data['subject']
    message = data['message']
    csv_writer =csv.writer(csvdb,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_csv(data)
            return redirect('/thanks.html')
        except:
            return "Did not save to Database."
    else:
        return "Something went wrong. Try again!"
    