# coding=utf-8
from flask_script import Manager
import config
from app import app
from exts import db
from models import *
from datetime import datetime
from flask_migrate import Migrate,MigrateCommand

#生成一个迁移文件会报错的引用
# '''
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from xlrd import open_workbook


from xlutils.copy import copy
import sched
import time
import random
# '''

manager = Manager(app)
db.init_app(app)

#绑定app和db
migrate = Migrate(app,db)

#添加迁移脚本的命令到manager中

manager.add_command('db',MigrateCommand)








@manager.command
def runjiaoben():
    print('脚本跑起来了')
    kk = Lanmu.query.all()
    print('获取到的栏目长度', kk)
    scheduler = BlockingScheduler()
    intervalTtrigger = CronTrigger(hour=14,minute=33,second=25)

    scheduler.add_job(faubu,intervalTtrigger,id='my_job_id')
    scheduler.start()
    print('执行借宿')


def faubu():
    i = 0
    print('-----'*30)
    # while i< 100:
    '''
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    r_xls = open_workbook('/Users/leo/Desktop/smzl/git_location/test/zy_fl_ms.xlsx')
    table_miaosu = r_xls.sheets()[0]
    content_html = table_miaosu.cell(2, 4).value
    print('这个是提取到的文本内容', content_html)
    '''
    kk = Lanmu.query.all()
    print('获取到的栏目长度',kk)
    # time.sleep(300)



if __name__ =="__main__":
    manager.run()
