from config.database import Base
from sqlalchemy import Column, Integer, String

class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(String)
    category = Column(String)