from sqlalchemy import *
from migrate import *
import datetime

from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
entry = Table('entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('content', Text),
    Column('fragment', Text),
    Column('status', Integer, default=ColumnDefault(1)),
    Column('create_time', DateTime, default=ColumnDefault(datetime.datetime(2015, 3, 7, 22, 19, 57, 287949))),
    Column('modified_time', DateTime, default=ColumnDefault(datetime.datetime(2015, 3, 7, 22, 19, 57, 288021))),
    Column('user_id', Integer),
    Column('category_id', Integer),
    Column('view_count', Integer, default=ColumnDefault(0)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['entry'].columns['fragment'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['entry'].columns['fragment'].drop()
