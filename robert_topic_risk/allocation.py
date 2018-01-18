from IPython import embed
import pandas as pd
import pickle
import sys
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def Preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    stops = stopwords.words('english')
    tokens = [t for t in tokens if t not in stops]
    pst = PorterStemmer()
    tokens = [pst.stem(t) for t in tokens]
    text = ' '.join(tokens)
    return text


def OffTopic(comment):
	#print(comment)
	f = open('vectorized_ref_comment.pickle','rb')
	vectorizedRefComment = pickle.load(f)
	f.close()
	f = open('off_topic_vectorizer.pickle','rb')
	vectorizer = pickle.load(f)
	f.close()
	vectorizedComment = vectorizer.transform([comment,])
	result = ((vectorizedRefComment * vectorizedComment.T).A)[0][0]
	#print(result)
	if result < 2:
		ans = True
	else:
		ans = False
	return ans


def GetRiskTolerance(comment):
	f = open('v.pickle','rb')
	vectorizer = pickle.load(f)
	f = open('m.pickle','rb')
	model = pickle.load(f)
	X = vectorizer.transform([comment,]).toarray()
	ans = int(model.predict(X))

	if ans == -1:
		riskTolerance = 'conservative'
	if ans == 1:
		riskTolerance = 'aggressive'
	return riskTolerance

def GetAllocation(age,riskTolerance):
	df = pd.read_table('age_risk_glide_path.tsv')
	df2 = df.loc[df['Risk']==riskTolerance]
	df3 = df2.loc[int(age)<=df2['MaxAge']].head(1)
	df3 = df3.reset_index().drop('index',axis=1)
	alloc = df3.iloc[0,:].to_dict()
	return alloc

def GetStatement(age,alloc):
	statement = 'As a ' + str(age) + ' year old investor with a(n) ' + alloc['Risk'] + \
	' risk profile you might consider a portfolio with ' + \
	str(100*round(alloc['Total Stock Market Index'],2)) + ' percent in US stocks, ' + \
	str(100*round(alloc['Total International Stock Index'],2)) + ' percent in international stocks, ' + \
	str(100*round(alloc['Total Bond Market II Index'],2)) + ' percent in US bonds, ' + \
	str(100*round(alloc['Total International Bond Index'],2)) + ' percent in international bonds, and ' + \
	str(100*round(alloc['Short-Term Inflation-Protected Securitie'],2)) + ' percent in short-term inflaction protected securities.'
#	'This is offerd as part of the ' + alloc['Fund name'] + ' target retirement fund.'
	return statement

def PlotChart(alloc):
	labels = ['US Stock','International Stock','US Bond','International Bond','Short-term TIPS']
	fracs = [alloc['Total Stock Market Index'],alloc['Total International Stock Index'],alloc['Total Bond Market II Index'],alloc['Total International Bond Index'],alloc['Short-Term Inflation-Protected Securitie']]
	#colors = ['red','yellow','blue','green','gray']
	colors = ['#96151D','#EBBA00','#005293','#A8B400','#A8A093']


	plt.pie(fracs, colors=colors)
	plt.legend(labels=['%s, %1.1f' % (l, s) for l, s in zip(labels, [i * 100 for i in fracs])],loc='best')
	plt.axis('equal')
	plt.tight_layout()
	filename = 'allocation_' + str(alloc['MaxAge']) + '_' + alloc['Risk'] + '.png'
	print('View your allocation here: ' + filename)
	plt.savefig(filename)
	return True

def Main():
	age = sys.argv[1]
	comment = sys.argv[2]
	processedComment = Preprocess(comment)
	offTopic = OffTopic(processedComment)
	if offTopic:
		print("I'm sorry, can you give me more information?")
	else:
		#print('On topic')
		riskTolerance = GetRiskTolerance(processedComment)
		#print(riskTolerance)
		allocationDict = GetAllocation(age,riskTolerance)
		statement = GetStatement(age,allocationDict)
		print('\n' + statement + '\n')
		PlotChart(allocationDict)

	#embed()
	return


def generateChart():

	risktype = ['conservative', 'moderate', 'aggressive']
	for maxAge in range(23,125,1):
		for r in risktype:
			alloc = GetAllocation(maxAge, r)
			PlotChart(alloc)


#Main()

generateChart()