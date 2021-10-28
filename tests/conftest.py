import pytest
import sqlite3

conn = sqlite3.connect('todo.db')

@pytest.fixture(autouse=True)
def client():
    from project.app import app
    app.config['TESTING'] = True
    yield app.test_client()

@pytest.fixture(autouse=True)
def __init__():
    conn = sqlite3.connect('todo.db')
   
    # Why are we calling user table before to_do table
    # what happens if we swap them?



@pytest.fixture(autouse=True)
def delete_to_do_table():

    query = "DROP TABLE IF EXISTS Todo"

    conn.execute(query)

@pytest.fixture(autouse=True)
def delete_user_table():

    query = """
    DROP TABLE IF EXISTS User
    """
    
    conn.execute(query)

@pytest.fixture(autouse=True)
def create_to_do_table(delete_to_do_table):

    query = """
    CREATE TABLE IF NOT EXISTS "Todo" (
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done boolean DEFAULT 0,
        _is_deleted boolean DEFAULT 0,
        CreatedOn Date DEFAULT CURRENT_DATE,
        DueDate Date,
        UserId INTEGER FOREIGNKEY REFERENCES User(_id)
    );
    """

    conn.execute(query)

@pytest.fixture(autouse=True)
def create_user_table(delete_user_table):
    query = """
    CREATE TABLE IF NOT EXISTS "User" (
    _id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Email TEXT,
    CreatedOn Date default CURRENT_DATE
    );
    """
    conn.execute(query)
