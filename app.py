import atexit
import os
import json
from flask import Flask, render_template, flash, redirect, url_for, request, jsonify, session
from pymongo import MongoClient

app = Flask(__name__, static_url_path='')
dbConnectionString = 'mongodb+srv://hesham:accessME@cluster0.1e6ml.mongodb.net/BDAT1004?retryWrites=true&w=majority'
client = MongoClient(dbConnectionString)
db = client.BDAT1004DB
student =  db.student

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route("/data", methods=['GET', 'POST'])
def data():
    #In the below code we read the student details from the form and save it to DB.
    fname = request.form['first_name']
    lname = request.form['last_name']
    student_id = request.form['student_id']
    gender = request.form['gender']
    data = {'First Name' : fname, 'Last Name' : lname, 'Student ID' : student_id, 'Gender' : gender}
    student.insert_one(data)
    
    return render_template('register.html')

@app.route('/pie')
def pie():
    #In the below code we read the regitered student from the DB and count number of Male and Female
    countM = 0
    countF = 0
    studentData = student.find()
    for dat in studentData:
        if dat['Gender'] == 'M':
            countM += 1
        else:
            countF += 1
    
    data = {'Rigistered Students' : 'Male vs Female', 'Male' : countM, 'Female' : countF}
    return render_template('pie.html', data=data)

@app.route('/about')
def about():
	return render_template('about.html')


if __name__ == "__main__":
	app.debug = True
	app.run()
