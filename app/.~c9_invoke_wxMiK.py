from app import app
from flask import render_template, url_for, request, jsonify
import json, time

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/list')
def list():
    # total = 
    return render_template("list.html", applicants=total)
    
@app.route('/school')
def school():
    # sch
    return render_template("bySchool.html", applicants=schoolGuys)
    

# ([('school', u'michigan'), ('name', u'Lance'), ('internships', u'1'), ('gpa', u'35')])
@app.route('/decideHire', methods=["GET", "POST"])
def decideHire():
    if request.method == "POST":
        data = request.form
        print data
        
        #return json.dumps({'data': 'true'}, sort_keys=True, indent=4, separators=(',', ': '))
        return jsonify(result={'data': '4'})
        
    if request.method == "GET":
        return "bad response"