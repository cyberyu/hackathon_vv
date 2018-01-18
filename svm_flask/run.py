__author__ = 'shiyu'


from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import pickle
import sys
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

def Preprocess(text):
    tokens = word_tokenize(text)
    tokens = [t.lower() for t in tokens]
    stops = stopwords.words('english')
    tokens = [t for t in tokens if t  not in stops]
    pst = PorterStemmer()
    tokens = [pst.stem(t) for t in tokens]
    text = ' '.join(tokens)
    return text

def Predict(comment):
    f = open('v.pickle','rb')
    vectorizer = pickle.load(f)
    f = open('m.pickle','rb')
    model = pickle.load(f)

    processedComment = Preprocess(comment)
    X = vectorizer.transform([processedComment,]).toarray()
    ans = int(model.predict(X))

    return ans


class HelloWorld(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Email address to create user')
        parser.add_argument('password', type=str, help='Password to create user')
        args = parser.parse_args()
        #json_data = request.get_json(force=True)

        un = str(args['name'])
        pw = str(args['password'])
        #args = parser.parse_args()
        #un = str(args['username'])
        #pw = str(args['password'])
        return jsonify(u=un, p=pw)

class classify(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('textinput', type=str)
        args = parser.parse_args()
        txtinput = str(args['textinput'])
    	info = Predict(txtinput)
        print txtinput
        return jsonify(y=info)

api.add_resource(classify, '/clsfy')
api.add_resource(HelloWorld, '/testing')

if __name__ == '__main__':

    # print Predict("I like to play it safe")
    # #
    # print Predict("I like to take risk")
    # #
    # print Predict("I want high risk ")
    # #
    # print Predict("I want low risk ")
    app.run(debug=True)