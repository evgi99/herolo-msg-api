from app import db
from datetime import datetime


class Message(db.Model):
    """Model for the messages table"""
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key = True)
    sender = db.Column(db.String(80))
    receiver = db.Column(db.String)
    subject = db.Column(db.String)
    msg_content = db.Column(db.String)
    creation_date = db.Column(db.String)
    is_read = db.Column(db.Boolean)

    def __init__(self, sender, receiver, subject, msg_content):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.msg_content = msg_content
        self.creation_date = '{:%d/%m/%Y %H:%M:%S}'.format(datetime.now())
        self.is_read = False

    def serialize(self):
        return {
            'id': self.id,
            'sender': self.sender,
            'receiver': self.receiver,
            'subject': self.subject,
            'msg_content': self.msg_content,
            'creation_date': self.creation_date
        }