
from flask import render_template, session, url_for, flash
from werkzeug.utils import redirect

from app.main.forms import EditForm
from app.models import Element, Type
from . import main
from .. import db


@main.route('/', methods=['GET', 'POST'])
def index():
    elements = Element.query.order_by(Element.type_id).all()
    return render_template('index.html', elements=elements)


@main.route('/add-element', methods=['GET', 'POST'])
def add_element():
    form = EditForm()
    if form.validate_on_submit():
        element = Element(ip=form.ip.data, username=form.username.data,
                          password=form.password.data, type=Type.query.get(form.type.data))
        db.session.add(element)
        db.session.commit()
        flash('Add element successfully')
        return redirect(url_for('.index'))
    return render_template('add_element.html', form=form)


@main.route('/edit-element/<int:id>', methods=['GET', 'POST'])
def edit_element(id):
    element = Element.query.get_or_404(id)
    form =EditForm()
    if form.validate_on_submit():
        element.ip = form.ip.data
        element.username = form.username.data
        element.password = form.password.data
        element.type = Type.query.get(form.type.data)
        db.session.add(element)
        db.session.commit()
        flash('The element has been updated')
        return redirect(url_for('.index'))
    form.ip.data = element.ip
    form.username.data = element.username
    form.password.data = element.password
    form.type.data = element.type_id
    return render_template('add_element.html', form=form)


@main.route('/delete-element/<int:id>', methods=['GET', 'POST'])
def delete_element(id):
    element = Element.query.get_or_404(id)
    db.session.delete(element)
    db.session.commit()
    return redirect(url_for('.index'))
