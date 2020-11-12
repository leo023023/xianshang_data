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
    intervalTtrigger = CronTrigger(hour=10, minute=58, second=9)
    asdasda =0
    scheduler.add_job(duoxiancheng, intervalTtrigger, id='my_job_id',args=[asdasda])
    scheduler.start()
    print('执行借宿')




def lanmu_id_1(cishu):
    # shijian = random.randint(1,10)
    shijian = random.randint(1,1000)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0,5):
            if cishu*5+i < 598:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 1).all()[cishu*5+i]
                author_suiji =random.randint(1,300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是',author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间',dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                #下次写入数据库的间隔时间
                time.sleep(random.randint(3600,7200))
                # time.sleep(random.randint(1,10))
            else:
                pass
        print('栏目id——1数据写入成功')


def lanmu_id_2(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间',shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0,20):
            if cishu*20+i<3573:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 2).all()[cishu*20+i]
                author_suiji =random.randint(1,300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是',author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间',dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(900, 2700))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——2数据写入成功')


def lanmu_id_3(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 1):
            if cishu + i < 55:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 3).all()[cishu + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(3600, 36000))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——3数据写入成功')


def lanmu_id_4(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 10):
            if cishu * 10 + i < 1123:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 4).all()[cishu * 10 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(1800, 2700))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——4数据写入成功')





def lanmu_id_5(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 10):
            if cishu * 10 + i < 1312:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 5).all()[cishu * 10 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(1800, 2700))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——5数据写入成功')



def lanmu_id_6(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 2):
            if cishu * 2 + i < 1312:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 6).all()[cishu * 2 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(1800, 27000))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——6数据写入成功')



def lanmu_id_7(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 5):
            if cishu * 5 + i < 2011:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 7).all()[cishu * 5 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(3600, 7200))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——7数据写入成功')



def lanmu_id_8(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 2):
            if cishu * 2 + i < 274:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 8).all()[cishu * 2 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(1800, 27000))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——8数据写入成功')


def lanmu_id_9(cishu):
    shijian = random.randint(1,1000)
    # shijian = random.randint(1,10)
    print('休眠时间', shijian)
    time.sleep(shijian)
    with app.app_context():
        for i in range(0, 5):
            if cishu * 5 + i < 572:
                article_list_1 = Article_zan.query.filter(Article_zan.lanmu_id == 9).all()[cishu * 5 + i]
                author_suiji = random.randint(1, 300)
                yuedu_suiji = random.randint(1500, 4000)
                author_name = Author.query.filter(Author.id == author_suiji).first().author_name
                print('随机生成的作者是', author_name)
                print('随机生成的阅读数是', yuedu_suiji)
                dangqian_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print('获得的当前发布时间', dangqian_time)
                article = Article(
                    title=article_list_1.title,
                    content=article_list_1.content,
                    lanmu_id=article_list_1.lanmu_id,

                    author_name=author_name,
                    zaiyao=article_list_1.zaiyao,
                    description=article_list_1.description,

                    article_yuedu=yuedu_suiji,
                    article_time=dangqian_time,
                )
                db.session.add(article)
                db.session.commit()
                # 下次写入数据库的间隔时间
                time.sleep(random.randint(3600, 72000))
                # time.sleep(random.randint(1,2))

            else:
                pass
            print('栏目id——9数据写入成功')



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