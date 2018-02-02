from app import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(20), unique = True)
    user_password = db.Column(db.String(20))
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30))
    content = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id


