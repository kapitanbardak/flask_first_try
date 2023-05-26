from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Quiz(db.Model):
    __tablename__ = "quiz"

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        unique=True
    )
    question = db.Column(db.String(), nullable=False)
    answer = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Quiz {self.id}, {self.question}, {self.answer}, {self.created_at}>"
