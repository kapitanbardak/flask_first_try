from flask import jsonify, request
from models import db, Quiz
import requests
from datetime import datetime as dt

def init_routes(app):
    @app.route('/')
    def hello_world():
        return 'Hello World!'

    @app.route('/api/questions', methods=['POST'])
    def create_user():
        questions_num = request.json.get('questions_num')
        saved_questions = db.session.query(Quiz).count()
        last_question = db.session.query(Quiz).order_by(Quiz.id.desc()).first()
        if last_question:
            result = jsonify(last_question.question)
        else:
            result = jsonify()
        while db.session.query(Quiz).count() < saved_questions + questions_num:
            response = requests.get('https://jservice.io/api/random?count=1')
            if response.status_code == 200:
                question = response.json()[0]['question']
                question_exists = db.session.query(Quiz).filter_by(question=question).first() is not None
                if not question_exists:
                    answer = response.json()[0]['answer']
                    created_at = dt.now()
                    new_question = Quiz(question=question, answer=answer, created_at=created_at)
                    db.session.add(new_question)
                    db.session.commit()

        return result
