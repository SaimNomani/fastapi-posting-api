from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings
from urllib.parse import quote_plus



SQLALCHEMY_DATABASE_URL=f'postgresql+psycopg2://{settings.DB_USER}:{quote_plus(settings.DB_PASSWORD)}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}_test'

engine=create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal=sessionmaker(autoflush=False, autocommit=False, bind=engine)







