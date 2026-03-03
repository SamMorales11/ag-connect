from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ganti user, password, dan nama database sesuai settingan PostgreSQL lokal Anda
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:samuel123@localhost:5432/ag_connect_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()