from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
entries = Table('entries', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('author', String(length=40)),
    Column('content', Text),
    Column('status', Integer),
    Column('create_time', DateTime),
    Column('modified_time', DateTime),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=80)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(2)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['entries'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['entries'].drop()
    post_meta.tables['user'].drop()
