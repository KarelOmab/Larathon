from flask import render_template, request, redirect, url_for
from app.Models.user import User
from bootstrap.database import db  # Import the singleton db instance

class UserController:
    def index(self):
        users = User.query.all()  # No need for manual app context management
        return render_template('users/index.html', users=users)

    def show(self, id):
        user = User.query.get_or_404(id)
        return render_template('users/show.html', user=user)

    def create(self):
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']
            new_user = User(name=name, email=email)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('users/create.html')

    def edit(self, id):
        user = User.query.get_or_404(id)
        if request.method == 'POST':
            user.name = request.form['name']
            user.email = request.form['email']
            if request.form['password']:
                user.set_password(request.form['password'])
            db.session.commit()
            return redirect(url_for('show', user_id=user.id))
        return render_template('users/edit.html', user=user)

    def delete(self, id):
        user = User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
