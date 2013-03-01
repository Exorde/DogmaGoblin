from mediagoblin.db.base import Base
from sqlalchemy import (MetaData, Table, Column, Integer, Unicode, ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from mediagoblin.db.migration_tools import RegisterMigration, inspect_table

MIGRATIONS = {}

class DogmaExtraDataDB_V0(declarative_base()):
    extend_existing=True
    __tablename__ = "dogma__extra_data"

    media_entry = Column(Integer, ForeignKey('core__media_entries.id'),primary_key=True)
    composers = Column(Unicode)
    authors = Column(Unicode)
    performers = Column(Unicode)

@RegisterMigration(1, MIGRATIONS)
def remove_and_replace_token_and_code(db):
    metadata = MetaData(bind=db.bind)

    token_table = inspect_table(metadata, 'dogma__extra_data')
    DogmaExtraDataDB_V0.__table__.create(db.bind)

    db.commit()
