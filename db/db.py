from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="password", 
    host="localhost",     
    port=3306,
    database="tasks"
)

engine = create_engine(url)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()