from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from website.forms import NoteForm
from .models import Note
from . import db
import json

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    form = NoteForm()
    if form.validate_on_submit():
        flash("Note added", category="success")
        note = Note(data=form.note.data, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()
    return render_template("home.html", form=form, user=current_user)


@views.route("/delete-note", methods=["GET", "POST"])
def delete_note():
    note = json.loads(request.data)
    note_id = note["noteId"]
    note = Note.query.get(note_id)
    db.session.delete(note)
    db.session.commit()
    print("here")
    return jsonify({})
