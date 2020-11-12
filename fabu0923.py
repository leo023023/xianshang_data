# coding=utf-8
from flask_script import Manager
from app import app
from models import *
import time
import threading
import random
from datetime import datetime

from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


manager = Manager(app)


@manager.command
def fabu():
    print('<<<<<'*40)
    scheduler = BlockingScheduler()
    # intervalTtrigger = CronTrigger(second=30)
    intervalTtrigger = CronTrigger(hour=10, minute=11, second=9)
    asdasda =0
    scheduler.add_job(duoxiancheng, intervalTtrigger, id='my_job_id',args=[asdasda])
    scheduler.start()
    print('执行借宿')

def lanmu_id_1(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 1).all())
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



def lanmu_id_2(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 2).all())
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

def lanmu_id_3(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 3).all())
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
	            time.sleep(random.randint(3600, 30000))
	            changdu = changdu + 1

def lanmu_id_4(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 4).all())
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


def lanmu_id_5(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 5).all())
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


def lanmu_id_6(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 6).all())
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


def lanmu_id_7(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 7).all())
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


def lanmu_id_8(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 8).all())
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


def lanmu_id_9(cishu):
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
	    changdu = len(Article.query.filter(Article.lanmu_id == 9).all())
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
	            time.sleep(random.randint(3600, 7200))
	            changdu = changdu + 1






def duoxiancheng(asdasda):
    with app.app_context():
        cishu = len(Cishu.query.all())
        print('程序运行的次数',cishu+1)
        lanmu_id_1_def = threading.Thread(target=lanmu_id_1, name='lanmu_id_1', args=(cishu,))
        lanmu_id_2_def = threading.Thread(target=lanmu_id_2, name='lanmu_id_2', args=(cishu,))
        lanmu_id_3_def = threading.Thread(target=lanmu_id_3, name='lanmu_id_3', args=(cishu,))
        lanmu_id_4_def = threading.Thread(target=lanmu_id_4, name='lanmu_id_4', args=(cishu,))
        lanmu_id_5_def = threading.Thread(target=lanmu_id_5, name='lanmu_id_5', args=(cishu,))
        lanmu_id_6_def = threading.Thread(target=lanmu_id_6, name='lanmu_id_6', args=(cishu,))
        lanmu_id_7_def = threading.Thread(target=lanmu_id_7, name='lanmu_id_7', args=(cishu,))
        lanmu_id_8_def = threading.Thread(target=lanmu_id_8, name='lanmu_id_8', args=(cishu,))
        lanmu_id_9_def = threading.Thread(target=lanmu_id_9, name='lanmu_id_9', args=(cishu,))

        lanmu_id_1_def.start()
        lanmu_id_2_def.start()
        lanmu_id_3_def.start()
        lanmu_id_4_def.start()
        lanmu_id_5_def.start()
        lanmu_id_6_def.start()
        lanmu_id_7_def.start()
        lanmu_id_8_def.start()
        lanmu_id_9_def.start()

        lanmu_id_1_def.join()
        lanmu_id_2_def.join()
        lanmu_id_3_def.join()
        lanmu_id_4_def.join()
        lanmu_id_5_def.join()
        lanmu_id_6_def.join()
        lanmu_id_7_def.join()
        lanmu_id_8_def.join()
        lanmu_id_9_def.join()

        print('主线程结束')
        cishu_xieru = Cishu(cishu=cishu)
        db.session.add(cishu_xieru)
        db.session.commit()
        print('全部跑结束了')




if __name__=='__main__':
    manager.run()