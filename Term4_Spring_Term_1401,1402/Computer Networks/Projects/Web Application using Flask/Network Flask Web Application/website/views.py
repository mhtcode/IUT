import json

from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import current_user, login_required

from . import db
from .models import Note, User

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    """
    Home page view.
    """
    if request.method == 'POST':
        note = request.form.get('note')  # Gets the note from the HTML
        title = request.form.get('title')  # Gets the title from the HTML
        print(note)
        print(title)
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            # Create a new Note object with the provided note data, title, author, and user_id
            new_note = Note(
                data=note, title=title, author=current_user.first_name, user_id=current_user.id)
            db.session.add(new_note)  # Add the note to the database
            db.session.commit()
            flash('Note added!', category='success')

    notes = db.session.query(Note).all()
    return render_template("home.html", notes=notes, user=current_user)


@views.route('/about', methods=['GET', 'POST'])
def about():
    """
    About page view.
    """
    return render_template("about.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    """
    Delete a note from the database.
    """
    # This function expects a JSON object from the INDEX.js file
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            flash('Note deleted!', category='success')

    return jsonify({})


@views.route('/users/count', methods=['GET'])
def get_user_count():
    """
    Get the count of users in the database.
    """
    user_count = User.query.count()
    print(user_count)
    return jsonify({'count': user_count})
