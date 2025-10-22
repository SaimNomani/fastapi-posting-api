from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from urllib.parse import quote_plus # to handle special characters in DB password

# SQLALCHEMY_DATABASE_URL='postgresql+<driver>://<username>:<password>@<ip-address/hostname>:<port no>/<database_name>'

SQLALCHEMY_DATABASE_URL=f'postgresql+psycopg2://{settings.DB_USER}:{quote_plus(settings.DB_PASSWORD)}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

# *****The engine is the bridge between your Python code and the database.***
# --It handles the connection to your database (like SQLite, PostgreSQL, etc.)
# --It uses a database URL to connect
# --It powers all the communication with the database under the hood
engine=create_engine(SQLALCHEMY_DATABASE_URL)



# *****A session is how you talk to the database to run commands.*****
# --- You use it to add, update, delete, and query data
# --- It's like a temporary conversation with the database
# --- You typically open a session, do your work, then commit or close it
# autoflush=False: Changes are not auto-pushed to the DB until you commit or flush explicitly.
# autocommit=False: Manual control over commits; changes won’t persist unless committed.
# bind=engine: Connects the session to the engine so it knows what DB to interact with.
SessionLocal=sessionmaker(autoflush=False, autocommit=False, bind=engine)


# Every ORM class (representing a table) will inherit from Base.
# This enables SQLAlchemy to map the classes to actual tables and manage their metadata.
# It’s the starting point for creating ORM models in SQLAlchemy.
# It acts like a blueprint maker — you use it to define your database tables as Python classes.
Base=declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()