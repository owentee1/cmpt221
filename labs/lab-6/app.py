"""app.py: render and route to webpages"""

from flask import request, render_template, redirect, url_for
from sqlalchemy import insert, text, select

from db.server import app
from db.server import db

from db.schema.user import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method =='POST':
        # query = f"""INSERT INTO "Users" ("FirstName", "LastName", "Email", "PhoneNumber", "Password")
        # VALUES ('{request.form["FirstName"]}',
        #         '{request.form["LastName"]}',
        #         '{request.form["Email"]}',
        #         '{request.form["PhoneNumber"]}',
        #         '{request.form["Password"]}'
        #         );"""

        query = insert(User).values(request.form)

        with app.app_context():
            db.session.execute(query)
            db.session.commit()

        return redirect(url_for('index'))
    
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if "Email" in request.form and "Password" in request.form:

            stmt = select(User).where(User.Email == request.form["Email"])
            user = db.session.execute(stmt).scalars().first()

            if user and user.Password == request.form["Password"]:
                return redirect(url_for('success'))
            else:
                return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/users')
def users():
    
    with app.app_context():
        # select users where the first name is Calista
        # stmt = select(User).where(User.FirstName == "Calista")

        # select all users
        stmt = select(User)
        all_users = db.session.execute(stmt)

        return render_template('users.html', users=all_users)
    
    return render_template('users.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    # debug refreshes your application with your new changes every time you save
    app.run(debug=True)

