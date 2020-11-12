# coding=utf-8
from flask_script import Manager
from models import *
import time
import threading
import random
from datetime import datetime







def lanmu_id_1():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 1).all())
    xianzhi_changdu = changdu+5
    print('这个是栏目id为1 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 1).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(3600, 7200))
            changdu = changdu + 1



def lanmu_id_2():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 2).all())
    xianzhi_changdu = changdu+20
    print('这个是栏目id为2 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 2).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(900, 2700))
            changdu = changdu + 1

def lanmu_id_3():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 3).all())
    xianzhi_changdu = changdu+1
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 3).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(3600, 36000))
            changdu = changdu + 1

def lanmu_id_4():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 4).all())
    xianzhi_changdu = changdu+10
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 4).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(1800, 2700))
            changdu = changdu + 1


def lanmu_id_5():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 5).all())
    xianzhi_changdu = changdu+10
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 5).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(1800, 2700))
            changdu = changdu + 1


def lanmu_id_6():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 6).all())
    xianzhi_changdu = changdu+2
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 6).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(1800, 2700))
            changdu = changdu + 1


def lanmu_id_7():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 7).all())
    xianzhi_changdu = changdu+5
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 7).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(3600, 7200))
            changdu = changdu + 1


def lanmu_id_8():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 8).all())
    xianzhi_changdu = changdu+2
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 8).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(1800, 27000))
            changdu = changdu + 1


def lanmu_id_9():
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    changdu = len(Article.query.filter(Article_zan.lanmu_id == 9).all())
    xianzhi_changdu = changdu+5
    print('这个是栏目id为3 的文章长度',changdu)
    i=0
    while changdu < xianzhi_changdu:
        i=i+1
        print('运行次数统计',i)
        xieru_zong = Article_zan.query.filter(Article_zan.lanmu_id == 9).all()[changdu]
        xieru_title = xieru_zong.title
        print('获取到的文章标题',xieru_title)

        title_yesno = Article.query.filter(Article.title == xieru_title).first()
        if title_yesno:
            print('存在')
            changdu=changdu+1
            xianzhi_changdu=xianzhi_changdu+1
        else:
            print('不存在')
            author_suiji = random.randint(1, 300)
            yuedu_suiji = random.randint(1000, 4000)
            author_name = Author.query.filter(Author.id == author_suiji).first().author_name
            print('随机生成的作者是', author_name)
            print('随机生成的阅读数是', yuedu_suiji)
            dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print('获得的当前发布时间', dangqian_time)

            article = Article(
                title=xieru_zong.title,
                content=xieru_zong.content,
                lanmu_id=xieru_zong.lanmu_id,

                author_name=author_name,
                zaiyao=xieru_zong.zaiyao,
                description=xieru_zong.description,

                article_yuedu=yuedu_suiji,
                article_time=dangqian_time,
            )
            db.session.add(article)
            db.session.commit()
            time.sleep(random.randint(3600, 72000))
            changdu = changdu + 1

