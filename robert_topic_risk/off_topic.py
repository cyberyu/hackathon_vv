import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

#import pickle
#from nltk.sentiment.vader import negated
#import pandas as pd

global refComment

def Preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    stops = stopwords.words('english')
    tokens = [t for t in tokens if t  not in stops]
    pst = PorterStemmer()
    tokens = [pst.stem(t) for t in tokens]
    text = ' '.join(tokens)
    return text


def initialize():

    global refComment, vectorizedFit, vectorizedRefComment

    refComment = "2008 ETF accept account advice age aggressive allocation amount asset averse balance bank bear bitcoin black bond brokerage bubble budget bull buy cash cautious collapse \
    comfortable commission concern conservative contribute coin cost credit currency debt decline dip distribute diversify dividend dollar down downturn dow \
    earn economy equity euro expense exposure fall fear fluctuation frugal fund gain grow high hold hundred income increase index inflation invest loan long lose loss \
    low market maximum medium middle million minimum moderate money mutual nasdaq net old owe portfolio position price principal profit \
    rally ratio reinvest recession red retirement return revenue rise risk safe save securities sell share spend stable stock s&p tax term thousand thrifty tolerance trade \
    unbalanced up value volatile vanguard wallet worry worth yen yield young"

    refComment = Preprocess(refComment)

    vectorizer = CountVectorizer(min_df=1,ngram_range=(1,1))

    vectorizedFit = vectorizer.fit([refComment,])

    vectorizedRefComment = vectorizedFit.transform([refComment,])


def Detect_topic(comment):
    global vectorizedFit,  vectorizedRefComment
    processedComment = Preprocess(comment)
    vectorizedTestComment = vectorizedFit.transform([processedComment,])
    result = ((vectorizedRefComment * vectorizedTestComment.T).A)[0][0]

    if result < 2:
        print('off topic')
    else:
        print('on topic')


def main():
    initialize()
    comment = sys.argv[1]
    Detect_topic(comment)

if __name__ == "__main__":
    main()




# print('score: ' + str(result))
# print()


# f = open('vectorized_ref_comment.pickle','wb')
# pickle.dump(vectorizedRefComment,f)
# f.close()
#
# f = open('off_topic_vectorizer.pickle','wb')
# pickle.dump(vectorizedFit,f)
# f.close()