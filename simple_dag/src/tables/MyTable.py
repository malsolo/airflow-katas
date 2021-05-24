from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'MyTable'

    Id = Column(String, primary_key=True)
    Value = Column(String)

    def __repr__(self):
        return "<MyTable(Id='%s', Value='%s')>" % (self.Id, self.Value)
