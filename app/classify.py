import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

import cPickle

def testCandidate(GPA, school, skill1, skill2, years_of_experience):

    templateName = {'California Polytechnic State University': 2, 'Cornell University': 3, 'Georgia Institute of Technology': 4, 'UC Berkeley': 5, 'UCLA': 6, 'UC Davis': 7, 'UC Irvine': 8, 'UC San Diego': 9, 'USC': 10, 'UCSB': 11, 'University of Illinois': 12,
                'University of Michigan': 13, 'University of Texas': 14, 'University of Washington': 15, 'Other': 16}
    skills = {'datascience': 17, 'frontend': 18, 'backend': 19, 'mobile':20, 'comparch':21, 'controls':22, 'embedded':23}

    with open('app/my_dumped_classifier.pkl', 'rb') as fid:
        knn_loaded = cPickle.load(fid)



    inputCandidate = [[0] * 24]
    schoolIndex = templateName[school]
    skillIndex = skills[skill1]
    skillIndex2 = skills[skill2]
    #print schoolIndex
    inputCandidate[0][schoolIndex] = 1

    inputCandidate[0][0] = years_of_experience
    inputCandidate[0][1] = GPA
    #print skillIndex
    inputCandidate[0][skillIndex] = 1
    inputCandidate[0][skillIndex2] = 1


    predictions = knn_loaded.predict(inputCandidate)
    #print(accuracy_score(inputCandidate, predictions))
    #print(confusion_matrix(inputCandidate, predictions))
    #print(classification_report(inputCandidate, predictions))
    print predictions
    return predictions[0]

#testCandidate(3.75, 'California Polytechnic State University','controls', 'embedded', 2)

def allCandidates():
    source = 'studentResults.csv'
    names = [ 'NumPrevInternships','GPA', 'CalPoly', 'Cornell', 'GT', 'Cal', 'UCLA', 'UCD', 'UCI', 'UCSD', 'USC', 'UCSB', 'UIUC', 'Umich', 'UT',
        'UW', 'Other', 'DataScience', 'FE', 'BE', 'Mobile', 'CA', 'Controls', 'Embedded','C++']
    
    Simon = {
        'ID': 23342,
        'school': 'California Polytechnic State University',
        'GPA': 2.4,
        'skill1': 'frontend',
        'skill2': 'embedded',
        'experience': 1,
        'score':0
    }
    Neil = {
        'ID': 20213,
        'school': 'California Polytechnic State University',
        'GPA': 3.2,
        'skill1':  'backend',
        'skill2': 'mobile',
        'experience' :0,
        'score':0
    }
    Zane = {
        'ID': 19213,
        'school': 'California Polytechnic State University',
        'GPA': 3.9,
        'skill1': 'controls',
        'skill2': 'frontend',
        'experience': 2,
        'score':0
    }
    Lance  = {
        'ID': 24324,
        'school': 'Georgia Institute of Technology',
        'GPA': 3.75,
        'skill1': 'datascience',
        'skill2': 'frontend',
        'experience': 1,
        'score':0
    }
    Suraj = {
        'ID': 59696,
        'school': 'UC Davis',
        'GPA': 3.5,
        'skill1': 'datascience',
        'skill2': 'mobile',
        'experience': 3,
        'score':0
    }
    
    Cands = [Simon, Neil, Suraj, Zane, Lance]
    Results ={}
    for cand in Cands:
       score =  trainFromDict(cand)
       cand['score'] = score
       Results[cand['ID']] = cand
      
    return Results
   

def trainFromDict(diction):
    return testCandidate(diction['GPA'], diction['school'], diction['skill1'], diction['skill2'], diction['experience'])