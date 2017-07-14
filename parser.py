import pandas as pd
import numpy as np

df = pd.read_csv('example.csv')
del df['Timestamp']
df.drop(df.columns[11],axis=1,inplace=True)
df.drop(1)
df.drop(df.index[[1]])
new_header = ['schoolName', 'previousInternships', 'gpa', 'cpp', 'java', 'xo', 'python', 'javascript', 'ruby', 'skill1', 'skill2'] #10



gpaDict = {'0.00 - 0.49': 0.25, '0.50 - 0.99': 0.75, '1.00 - 1.49': 1.25, '1.50 - 1.99': 1.75, '2.00 - 2.49': 2.25, '2.50 - 2.99': 2.75, '3.00 - 3.49': 3.25, '3.50 - 4.00': 3.75}
scaleDict = {'No experience': 0, 'Familiar': 1, 'Comfortable': 2, 'Fluent': 3, 'Master': 4}
df.to_csv('out.csv', header=new_header)
df = pd.read_csv('out.csv', index_col=0)

df.replace(['0.00 - 0.49', '0.50 - 0.99', '1.00 - 1.49', '1.50 - 1.99', '2.00 - 2.49', '2.50 - 2.99', '3.00 - 3.49', '3.50 - 4.00'], [0.25, 0.75, 1.25, 1.75, 2.25, 2.75, 3.25, 3.75], inplace = True)
df.replace(['No experience', 'Familiar', 'Comfortable', 'Fluent', 'Master'], [0,1,2,3,4], inplace = True)
templateName = {'California Polytechnic State University': 1, 'Cornell University': 2, 'Georgia Institute of Technology': 3, 'UC Berkeley': 4, 'UCLA': 5, 'UC Davis': 6, 'UC Irvine': 7, 'UC San Diego': 8, 'USC': 9, 'UCSB': 10, 'University of Illinois': 11, 'University of Michigan': 12, 'University of Texas': 13, 'University of Washington': 14, 'Other': 15}
schools = ['cpsu', 'cornell', 'gt', 'ucb', 'ucla', 'ucd', 'uci', 'ucsd', 'usc', 'ucsb', 'uiuc', 'um', 'ut', 'uw', 'other']
skills = ['datascience', 'frontend', 'backend', 'mobile', 'comparch', 'controls', 'embedded']
skillsTemplate = ['Data Science', 'Front-End', 'Backend', 'Mobile', 'Computer Architecture', 'Controls', 'Embedded Systems']

cpsu = []
cornell = []
gt = []
ucb = []
ucla = []
ucd = []
uci = []
ucsd = []
usc = []
ucsb = []
uiuc = []
um = []
ut = []
uw = []
ot = []
datascience = []
frontend = []
backend = []
mobile = []
comparch = []
controls = []
embedded = []

count = 0

for row in df.iterrows():
	if row[1][0] == 'California Polytechnic State University':
		cpsu.append(1)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'Cornell University':
		cpsu.append(0)
		cornell.append(1)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'Georgia Institute of Technology':
		cpsu.append(0)
		cornell.append(0)
		gt.append(1)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UC Berkeley':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(1)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UCLA':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(1)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UC Davis':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(1)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UC Irvine':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(1)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UC San Diego':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(1)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'USC':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(1)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'UCSB':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(1)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'University of Illinois':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(1)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'University of Michigan':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(1)
		ut.append(0)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'University of Texas':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(1)
		uw.append(0)
		ot.append(0)
	if row[1][0] == 'University of Washington':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(1)
		ot.append(0)
	if row[1][0] == 'Other':
		cpsu.append(0)
		cornell.append(0)
		gt.append(0)
		ucb.append(0)
		ucla.append(0)
		ucd.append(0)
		uci.append(0)
		ucsd.append(0)
		usc.append(0)
		ucsb.append(0)
		uiuc.append(0)
		um.append(0)
		ut.append(0)
		uw.append(0)
		ot.append(1)
	if (row[1][9] == 'Data Science'):
		datascience.append(1)
		frontend.append(0)
		backend.append(0)
		mobile.append(0)
		comparch.append(0)
		controls.append(0)
		embedded.append(0)
	if (row[1][9] == 'Front-End'):
		datascience.append(0)
		frontend.append(1)
		backend.append(0)
		mobile.append(0)
		comparch.append(0)
		controls.append(0)
		embedded.append(0)
	if (row[1][9] == 'Backend'):
		datascience.append(0)
		frontend.append(0)
		backend.append(1)
		mobile.append(0)
		comparch.append(0)
		controls.append(0)
		embedded.append(0)
	if (row[1][9] == 'Mobile'):
		datascience.append(0)
		frontend.append(0)
		backend.append(0)
		mobile.append(1)
		comparch.append(0)
		controls.append(0)
		embedded.append(0)
	if (row[1][9] == 'Computer Architecture'):
		datascience.append(0)
		frontend.append(0)
		backend.append(0)
		mobile.append(0)
		comparch.append(1)
		controls.append(0)
		embedded.append(0)
	if (row[1][9] == 'Controls'):
		datascience.append(0)
		frontend.append(0)
		backend.append(0)
		mobile.append(0)
		comparch.append(0)
		controls.append(1)
		embedded.append(0)
	if (row[1][9] == 'Embedded Systems'):
		datascience.append(0)
		frontend.append(0)
		backend.append(0)
		mobile.append(0)
		comparch.append(0)
		controls.append(0)
		embedded.append(1)
	if (row[1][10] == 'Data Science'):
		datascience[count] +=1
	if (row[1][10] == 'Front-End'):
		frontend[count] +=1
	if (row[1][10] == 'Backend'):
		backend[count] +=1
	if (row[1][10] == 'Mobile'):
		mobile[count] +=1
	if (row[1][10] == 'Computer Architecture'):
		comparch[count] +=1
	if (row[1][10] == 'Controls'):
		controls[count] +=1
	if (row[1][10] == 'Embedded Systems'):
		embedded[count] +=1
	count += 1
df['cpsu'] = cpsu
df['cornell'] = cornell
df['gt'] = gt
df['ucb'] = ucb
df['ucla'] = ucla
df['ucd'] = ucd
df['uci'] = uci
df['ucsd'] = ucsd
df['usc'] = usc
df['ucsb'] = ucsb
df['uiuc'] = uiuc
df['um'] = um
df['ut'] = ut
df['uw'] = uw
df['ot'] = ot
df['datascience'] = datascience
df['frontend'] = frontend
df['backend'] = backend
df['mobile'] = mobile
df['comparch'] = comparch
df['controls'] = controls
df['embedded'] = embedded
df = df.drop('skill1', 1)
df = df.drop('skill2', 1)
df = df.drop('schoolName', 1)


df.to_csv('parsed.csv')











