import pytest

from sqlalchemy import insert, select, text
from models import User

# test db connection
def test_db_connection(db_session):
    # Use db_session to interact with the database
    result = db_session.execute(text("SELECT 1"))
    assert result.scalar() == 1

# test to insert a user
# you can count this as one of your 5 test cases :)
def test_insert_user(db_session, sample_signup_owen):
    insert_stmt = insert(User).values(sample_signup_owen)

    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    # not part of the app.py code, just being used to get the inserted data
    selected_user = db_session.query(User).filter_by(FirstName="Owen").first()

    assert selected_user is not None
    assert selected_user.LastName == "Thomas"

#tests how it handles duplicate email submissions
def test_duplicate_email(db_session, sample_signup_alex):
    #insert first user
    insert_stmt = insert(User).values(sample_signup_alex)
    # execute insert query
    db_session.execute(insert_stmt)
    # commit the changes to the db
    db_session.commit()

    #insert second user by copying the "alex fixture"
    duplicate_user_email = sample_signup_alex.copy()
    duplicate_user_email["FirstName"] = "Duplicate"
    db_session.execute(insert(User).values(duplicate_user_email))
    db_session.commit()

    #checks to see if there are two users with same email
    users_with_duplicate_email = db_session.query(User).filter_by(Email = sample_signup_alex["Email"]).all()

    assert len(users_with_duplicate_email) == 2
    assert users_with_duplicate_email[0].FirstName == "Alex"
    assert users_with_duplicate_email[1].FirstName == "Duplicate"

#this is my expected to fail test, it attempts to find a user that does not exist.
@pytest.mark.xfail
def test_user_DNE(db_session):

    selected_user = db_session.query(User).filter_by(FirstName = "Nobody").first()

    assert selected_user is not None, "Expected fail because user 'Nobody' DNE. "

#Tests finding a user by first name/last name
def test_find_user_by_last_name(db_session, sample_signup_alex):

    insert_stmt = insert(User).values(sample_signup_alex)
    db_session.execute(insert_stmt)
    db_session.commit()

    #find user by full name and email I added email because I had multiple "Alex Thomas in my db and it was failing. This is better practice anyway, large dbs probably have multiple people with the same name, an email is a good way to distinguish them"
    selected_user = db_session.query(User).filter_by(LastName="Thomas", FirstName="Alex", Email=sample_signup_alex["Email"]).first()
   
    assert selected_user is not None, "User with first name 'Alex and last name 'Thomas' should exist."
    assert selected_user.Email == sample_signup_alex["Email"]

#this test determines whether a required '@' symbol was used when entering email
def test_for_at_symbol(db_session, sample_signup_georgia):

    insert_stmt = insert(User).values(sample_signup_georgia)
    db_session.execute(insert_stmt)
    db_session.commit()

    # verifies email format is correct.
    selected_user = db_session.query(User).filter_by(FirstName = "Georgia").first()
    assert selected_user is not None
    assert "@" in selected_user.Email

@pytest.mark.xfail(reason = "Expected failure due to missing table")
def test_critical_error_table_DNE(db_session):

    #query for a table that doesnt exist in the db
    non_exist_table_query = text("SELECT * FROM non_exist_table")

    #execute the query, expected to fail cause table dne.
    db_session.execute(non_exist_table_query)

    assert False, "Critical Error due to querying a table that is non-existent"
