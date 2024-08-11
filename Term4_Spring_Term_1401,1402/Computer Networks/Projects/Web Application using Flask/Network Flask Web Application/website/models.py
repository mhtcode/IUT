from datetime import datetime, timedelta
import pytz
from flask_login import UserMixin
from sqlalchemy import func, text

from . import db


class User(db.Model, UserMixin):
    """
    Model representing a user in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note', backref='user', lazy=True)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.id}, {self.first_name})'


class Note(db.Model):
    """
    Model representing a note in the database.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30))
    data = db.Column(db.String(10000))

    # Get the current time in Iran using func.text and the appropriate time zone offset
    # iran_timezone_offset = '+03:30'
    # current_time = func.text(
    #     f"(NOW() AT TIME ZONE 'GMT' + INTERVAL '{iran_timezone_offset}')")
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    author = db.Column(db.String(30))

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'{self.__class__.__name__},(self.id, {self.title[:30]}, {self.date})'
