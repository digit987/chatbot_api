from flask import Flask, request, Response
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import random

app = Flask(__name__)

@app.route('/question', methods=['POST'])
def read_question_and_respond():
	body = request.get_json()
	return {'response': read_question_predict_return_response(body['question'])}, 200
	
def read_question_predict_return_response(question):
	loaded_model = pickle.load(open('intent_and_answer.csv', 'rb'))
	vectorizer = CountVectorizer()
	vectorized_question = vectorizer.fit_transform([question])
	vectorized_question = vectorized_question.toarray()
	prediction = clf.predict(vectorized_question)
	intent_and_answer = pd.read_csv('intent_and_answer')
	answers = intent_and_answer[prediction]
	return random.choice(answers)