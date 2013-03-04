from mediagoblin.db.base import Base
from sqlalchemy import Column, Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship, backref

class DogmaExtraDataDB(Base):
    __tablename__ = "dogma__extra_data"

    media_entry = Column(Integer, ForeignKey('core__media_entries.id'),primary_key=True)
    composers = Column(Unicode)
    authors = Column(Unicode)
    performers = Column(Unicode)
    get_media_entry = relationship("MediaEntry",
                                   backref=backref("get_dogma_data", uselist=False,
                                                    cascade="all, delete-orphan"))

MODELS = [DogmaExtraDataDB]
