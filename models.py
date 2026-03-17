from sqlalchemy import Column,Integer,String,Text,DateTime,func
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Blog(Base):

    __tablename__ = "blog"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100),nullable=False)
    content = Column(Text,nullable=False)
    author = Column(String(100),nullable=False)
    created_at = Column(DateTime,server_default=func.now())