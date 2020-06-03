from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from Models.message import Message

@app.route('/api/get_message/<msg_id>', methods=['GET'])
def get_message(msg_id):
    # Read msg id from request
    try:
        if msg_id is None:
            raise ValueError("Don't received any msg id")
        msg = Message.query.filter_by(id=msg_id).first()
        msg.is_read = True
        db.session.commit()
        return jsonify({'msg': msg.serialize()})

    except Exception as e:
        return jsonify({'Exception': True, 'details': str(e)})


# Get all messages for a specific user
@app.route('/api/get_my_messages/<receiver>', methods=['GET'])
def get_my_messages(receiver):
    try:
        if receiver is None:
            raise ValueError("Don't received any receiver info")
        msgs = Message.query.filter_by(receiver=receiver).all()
        return jsonify([e.serialize() for e in msgs])
    except Exception as e:
        return jsonify({'Exception': True, 'details': str(e)})


# Get all unread messages for a specific user
@app.route('/api/get_my_unread_messages/<receiver>', methods=['GET'])
def get_my_unread_messages(receiver):
    try:
        if receiver is None:
            raise ValueError("Don't received any receiver info")
        msgs = Message.query.filter_by(receiver=receiver, is_read=False).all()
        return jsonify([e.serialize() for e in msgs])
    except Exception as e:
        return jsonify({'Exception': True, 'details': str(e)})


@app.route('/api/add_message', methods=['POST'])
def add_message():
    '''
    This api add message
    :return: received property data including extra data
    '''
    # Read request data
    try:
        data = request.get_json()
        if data is None:
            raise ValueError("Don't received any data")
        msg = Message(data['sender'], data['receiver'], data['subject'], data['content'])
        db.session.add(msg)
        db.session.commit()
        return jsonify({'Response': "msg added. msg id={}".format(msg.id)})

    except Exception as e:
        return jsonify({'Exception': True, 'details': str(e)})


@app.route('/api/delete_message/<msg_id>', methods=['GET', 'DELETE'])
def delete_message(msg_id):
    # Read msg id from request
    try:
        if msg_id is None:
            raise ValueError("Don't received any msg id")
        msg = Message.query.filter_by(id=msg_id).first()
        db.session.delete(msg)
        db.session.commit()
        return jsonify({'Response': "msg id={} deleted. ".format(msg.id)})

    except Exception as e:
        return jsonify({'Exception': True, 'details': str(e)})


if __name__ == '__main__':
    app.run(debug=True,  host='0.0.0.0')



