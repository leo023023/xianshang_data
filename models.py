# coding=utf-8
from exts import db

class User(db.Model):
    __tablename__ = 'user_vippp'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    telephone = db.Column(db.String(11), nullable=False)

class Lanmu(db.Model):
    __tablename__ = 'lanmu'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lanmuname = db.Column(db.String(100),nullable=False)
    lanmu_desc = db.Column(db.Text, nullable=False)
    lanmu_lujin = db.Column(db.String(100),nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    lanmu_id = db.Column(db.INTEGER,db.ForeignKey('lanmu.id'))
    authorkkk = db.relationship('Lanmu', backref=db.backref('xxxx'))
    author_name = db.Column(db.String(100), nullable=False)
    article_yuedu = db.Column(db.String(100), nullable=False)
    article_time = db.Column(db.String(100), nullable=False)

class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_name = db.Column(db.String(100), nullable=False)
    
class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(100), nullable=False)

class Pingjia(db.Model):
    __tablename__ = 'pingjia'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)