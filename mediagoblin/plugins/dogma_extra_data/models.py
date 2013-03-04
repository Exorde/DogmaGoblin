from mediagoblin.db.base import Base
from sqlalchemy import Column, Float,  Integer, Unicode, ForeignKey
from sqlalchemy.orm import relationship, backref
from mediagoblin.db.models import MediaEntry

class DogmaExtraDataDB(Base):
    __tablename__ = "dogma__extra_data"

    media_entry = Column(Integer, ForeignKey('core__media_entries.id'),primary_key=True)
    composers = Column(Unicode)
    authors = Column(Unicode)
    performers = Column(Unicode)
    get_media_entry = relationship("MediaEntry",
                                   backref=backref("get_dogma_data", uselist=False,
                                                    cascade="all, delete-orphan"))

class DogmaBandsDataDB(Base):
    __tablename__ = "dogma__bands_data"

    band_id = Column(Integer, primary_key=True)
    allowed_users_id = Column(Unicode)
    name = Column(Unicode)
    description = Column(Unicode)
    album_list = Column(Unicode)
    latitude = Column(Float)
    longitude = Column(Float)
    location = Column(Unicode)

MODELS = [DogmaExtraDataDB, DogmaBandsDataDB]
