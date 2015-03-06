from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=80)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(2)),
    Column('about_me', String(length=250)),
)

entries = Table('entries', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=100)),
    Column('author', VARCHAR(length=40)),
    Column('content', TEXT),
    Column('status', INTEGER),
    Column('create_time', DATETIME),
    Column('modified_time', DATETIME),
    Column('user_id', INTEGER),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['about_me'].create()
    pre_meta.tables['entries'].columns['author'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['about_me'].drop()
    pre_meta.tables['entries'].columns['author'].create()
