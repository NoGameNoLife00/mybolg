#coding=utf-8

from data_model import *

class DataWrappers(object):

    def get_all_entries(self):
        return Entries.query.all()

    def create_entries(self, title, content):
        ent = Entries(title=title, content=content)
        db.session.add(ent)
        db.comit()
        return ent

    def get_entries_by_page(self, page, par_page):
        pages = Entries.query.order_by(Entries.create_time.desc()).paginate(page, par_page)
        return pages
