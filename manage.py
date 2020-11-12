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



if __name__ =="__main__":
    manager.run()
