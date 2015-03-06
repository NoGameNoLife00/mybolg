from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
entries = Table('entries', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=100)),
    Column('content', TEXT),
    Column('status', INTEGER),
    Column('create_time', DATETIME),
    Column('modified_time', DATETIME),
    Column('user_id', INTEGER),
)

category = Table('category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
)

entry = Table('entry', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('content', Text),
    Column('status', Integer, default=ColumnDefault(1)),
    Column('create_time', DateTime),
    Column('modified_time', DateTime),
    Column('user_id', Integer),
    Column('category_id', Integer),
    Column('view_count', Integer, default=ColumnDefault(0)),
)

tag = Table('tag', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=80)),
)

tags = Table('tags', post_meta,
    Column('tag_id', Integer),
    Column('entry_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['entries'].drop()
    post_meta.tables['category'].create()
    post_meta.tables['entry'].create()
    post_meta.tables['tag'].create()
    post_meta.tables['tags'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['entries'].create()
    post_meta.tables['category'].drop()
    post_meta.tables['entry'].drop()
    post_meta.tables['tag'].drop()
    post_meta.tables['tags'].drop()
