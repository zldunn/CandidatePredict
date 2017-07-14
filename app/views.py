'''
WRITTEN BY LANCE HASSON AND SIMON WU
'''


from app import app
from flask import render_template, url_for, request, jsonify
import json, time, classify

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/list')
def list():
    total = classify.allCandidates()
    print total
    return render_template("list.html", applicants=total)
    
@app.route('/school')
def school():
    schoolGuys = {}
    return render_template("bySchool.html", applicants=schoolGuys)
    

# ([('school', u'University of Michigan'), ('name', u'lance'), ('skill2', u'frontend'), ('skill1', u'datascience'), ('gpa', u'3.75'), ('internships', u'1')])
@app.route('/decideHire', methods=["GET", "POST"])
def decideHire():
    if request.method == "POST":
        data = request.form
        name = data.get('name')
        school = data.get('school')
        internships = data.get('internships')
        gpa = data.get('gpa')
        skill1 = data.get('skill1')
        skill2 = data.get('skill2')
        print data
        print str(school)
        print float(gpa)
        print int(internships)
        print str(skill1)
        print str(skill2)
        
        
        res = classify.testCandidate(float(gpa), str(school), str(skill1), str(skill2), int(internships))
        time.sleep(3)
        print res
        #return json.dumps({'data': 'true'}, sort_keys=True, indent=4, separators=(',', ': '))
        return jsonify(result={'data': res})
        
    if request.method == "GET":
        return "bad response"