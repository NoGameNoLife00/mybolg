#coding:utf-8

import data_model
import datetime
# u = data_model.User(nickname='NoGameNoLife', email='964859557@qq.com', role=data_model.ROLE_ADMIN)
# u2 = data_model.User(nickname='Ct', email='1102443085@qq.com', role=data_model.ROLE_USER)
#
# data_model.db.session.add(u)
# data_model.db.session.add(u2)
# data_model.db.session.commit()
#
# #
# users = data_model.User.query.all()
# for user in users:
#     print(user.id, user.nickname, user.entries)
#     posts = data_model.Entries.query.all()
#     print "------"
#     for post in posts:
#         print "cs:", post.id, post.title, post.content, post.user_id, post.create_time

# u = data_model.User.query.get(1)

# print u
# p = data_model.Entries(title='test', content='my first post',
#                        create_time=datetime.datetime.now(), author=u)
# p2 = data_model.Entries(title='test2', content='my second post',
#                         create_time=datetime.datetime.now(), author=u2)
# data_model.db.session.add(p)
# data_model.db.session.commit()
# posts = data_model.Entries.query.all()
posts = data_model.Entries.query.all()

for post in posts:
    print post.id, post.title, post.author.nickname, post.content, post.user_id, post.create_time
# for post in posts2:
#     print post.id, post.title, post.author.nickname, post.content, post.user_id, post.create_time

# for post in posts:
#     data_model.db.session.delete(post)
#
# for u in users:
#     data_model.db.session.delete(u)
#
data_model.db.session.commit()
