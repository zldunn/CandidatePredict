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
#To save classification_report
import cPickle
#Load dataSet
source = 'studentResults.csv'
names = [ 'NumPrevInternships','GPA', 'CalPoly', 'Cornell', 'GT', 'Cal', 'UCLA', 'UCD', 'UCI', 'UCSD', 'USC', 'UCSB', 'UIUC', 'Umich', 'UT',
        'UW', 'Other', 'DataScience', 'FE', 'BE', 'Mobile', 'CA', 'Controls', 'Embedded','C++']
dataSet = pandas.read_csv(source, names = names)

#peek at the dataSet
print(dataSet.head(8))

#summary
print(dataSet.describe())

#class distrubution
print(dataSet.groupby('C++').size())

#plot multivariable

#scatter_matrix(dataSet)

#split out test and training - - - - - - - - - - - - - - - - - -
array = dataSet.values
X = array[:, 0:len(names)-1]

Y = array[:, len(names) -1]
validation_size = .2
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

print "y"
print Y
# Test options and evaluation metric - - - - - - - - - - - - - -
seed = 7
scoring = 'accuracy'

# Spot Check Algorithms - - - - - - - - - - - - - - - - - - - -
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# Compare Algorithms chart - - - - - - - - - - - - - - - - - - -
"""
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

"""
#How to actually create the classification_report
print(X_validation)
cart =  LinearDiscriminantAnalysis()
cart.fit(X_train, Y_train)
print "x"
print X_validation
predictions = cart.predict(X_validation)

print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

predicty = [[0]*24]
predicty[0][0] = 3
predicty[0][1] = 3.75
predicty[0][13] = 1


print  cart.predict(predicty)
with open('my_dumped_classifier.pkl', 'wb') as fid:
    cPickle.dump(cart, fid)
