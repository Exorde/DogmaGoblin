from mediagoblin.db.base import Base
from sqlalchemy import Column, Integer, Unicode, ForeignKey

class DogmaExtraDataDB(Base):
    __tablename__ = "dogma__extra_data"

    media_entry = Column(Integer, ForeignKey('core__media_entries.id'),primary_key=True)
    composers = Column(Unicode)
    authors = Column(Unicode)
    performers = Column(Unicode)

MODELS = [DogmaExtraDataDB]
