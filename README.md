# mybolg
本blog系统后端使用python编写，基于flask框架+mysql数据库，前端html5+bootstrap。目前这个blog部署在SAE（新浪云）上面。

基本功能：
---------
支持后台管理与登录，管理文章，分类，标签，用户，文件，友链等

演示地址：[NoGameNoLife's Blog](http://bugcoding.com)


使用SAE：
----------------
1.申请 SAE 开发账号, 创建Python Web应用

2.进入SAE应用管理控制台

3.在服务管理中创建SAE云存储 domain, 记下 domain名字

4.阅读SAE相关文档进行部署 [SAE python](http://sae.sina.com.cn/doc/python/index.html)文档

配置运行：
----------
配置MYSQL等（在部署在SAE上的话，直接从sae.const导入配置即可）

邮箱配置：输入使用的服务器地址，端口和账号，密码

开启调试模式：DEBUG = Ture

配置注册码（注册账号时需要使用）：REGISTRATION_CODE

创建数据表： $ python data_model.py

运行blog ： $ python blogapp.py
 
进入blog后台：
进入 http://localhost:5005/admin

点击register进行注册（需要输入配置的注册码）

退出之后即可用注册的账号登录

评论使用的多说评论系统：
-------------------
使用方法：注册多说，在首页里面选择我要安装，填写好资料。进入你的多说后台。获得你的多说的JS代码

并且把templates/blog（项目代码）里面的的模板（.html）中使用多说JS的代码替换成自己的就ok了

更多操作可以查看文档：[多说](http://dev.duoshuo.com/docs)


运行环境和第三方依赖库:
------------
python = 2.7

flask = 0.10.1

flask-SQLAlchemy = 2.0

flask-Admin = 1.0.3

flask-Login = 0.2.11

flask-Mail = 0.1

flask-Login = 0.2.11

flask-WTF = 0.11

sqlalchemy = 0.9.8

sqlalchemy-migrate = 0.10.1

wtforms = 2.0.2
