from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
SQLALCHEMY_DATABASE_URL_2 = "sqlite:///./aadhar_info.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

engine2 = create_engine(
    SQLALCHEMY_DATABASE_URL_2, connect_args={"check_same_thread":False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind = engine)

SessionLocal2 = sessionmaker(autocommit=False, autoflush=False, bind = engine2)

Base = declarative_base()