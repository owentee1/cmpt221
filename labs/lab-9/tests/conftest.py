import os
import pytest

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# contains table objects
Base = declarative_base()

# import environment variables from .env
load_dotenv()

db_name: str = os.getenv('db_name')
db_owner: str = os.getenv('db_owner')
db_pass: str = os.getenv('db_pass')
db_uri: str = f"postgresql://{db_owner}:{db_pass}@localhost/{db_name}"

# create db connection w/o Flask
# NOTE: creates new session for each test function
@pytest.fixture(scope="function")
def db_session():
    engine = create_engine(db_uri) 
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # create tables
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    yield session
    session.close()
    # drop tables
    Base.metadata.drop_all(bind=engine)

# example fixture - user sign in input
# hint... can you do something similar for login?
@pytest.fixture
def sample_signup_owen():
    return {'FirstName': 'Owen', 
            'LastName': 'Thomas', 
            'Email': 'owen.thomas1@marist.edu', 
            'PhoneNumber': '8888888888', 
            'Password': 'strongestPasswordEver'
            }

@pytest.fixture
def sample_signup_alex():
    return {'FirstName': 'Alex', 
            'LastName': 'Thomas', 
            'Email': 'alex.downey1@marist.edu', 
            'PhoneNumber': '7777777777', 
            'Password': 'strongestPasswordEver1'
            }

@pytest.fixture
def sample_signup_austin():
    return {'FirstName': 'Austin', 
            'LastName': 'James', 
            'Email': 'Austin.james1@marist.edu', 
            'PhoneNumber': '6666666666', 
            'Password': 'strongestPasswordEver2'
            }

@pytest.fixture
def sample_signup_georgia():
    return {'FirstName': 'Georgia', 
            'LastName': 'Angelina', 
            'Email': 'georgia.angelina1@marist.edu', 
            'PhoneNumber': '5555555555', 
            'Password': 'strongestPasswordEver3'
            }

@pytest.fixture
def sample_signup_mike():
    return {'FirstName': 'Mike', 
            'LastName': 'Corbi', 
            'Email': 'mike.corbi1@marist.edu', 
            'PhoneNumber': '4444444444', 
            'Password': 'strongestPasswordEver9'
            }