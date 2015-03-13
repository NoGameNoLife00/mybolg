 #encoding=utf-8

from data_model import User, Tag, Entry, Category, Friend_link, tag_entry
from blogapp import db


class DataWrappers(object):

    def get_all_entries(self):
        return Entry.query.all()

    def create_entry(self, title, content, tag, category):
        ent = Entry(title=title, content=content, category_id=category, create_time=datetime.now())
        #查找tag是否存在,并加入tags，如果不存在则创建tag
        tag_list = tag_entry.split()
        for tag_name in tag_list:
            t = db.session.query(Tag).filter(Tag.name == tag_name).first()
            if not t:
                t = Tag(tag_name)
            ent.tag.append(t)

        db.session.add(ent)
        db.comit()
        return ent

    def get_prev_entry(self, id):
        ent = db.engine.execute('SELECT * FROM  `entry`  where id<%s  order by create_time desc' % id).first()
        return ent

    def get_next_entry(self, id):
        ent = db.engine.execute('SELECT * FROM  `entry`  where id>%s  order by create_time asc ' % id).first()
        return ent

    def get_entry_by_category(self, categories):
        counts = []
        for category in categories:
            counts.append(Entry.query.filter_by(category=category).count())

        return counts


    def increase_view_count(self, entry, num):
        entry.view_count += num
        db.session.commit()
        return None

    def get_entries_by_page(self, page, par_page):
        pages = Entry.query.order_by(Entry.create_time.desc()).paginate(page, par_page)
        return pages

    def get_entry_by_id(self, id):
        ent = Entry.query.get(id)
        return ent

    def get_all_tags(self):
        ts = Tag.query.all()
        return ts

    def get_all_categories(self):
        categories = Category.query.all()
        return categories

    def get_category_by_id(self, id):
        cate = Category.query.get(id)
        return cate

    def get_tag_by_id(self, id):
        tag = Tag.query.get(id)
        return tag

    def get_all_links(self):
        links = Friend_link.query.all()
        return links

    def get_first_user(self):
        user = User.query.all()
        return user
