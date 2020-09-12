# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for, session, make_response
import config
from models import *
from exts import db
import urllib.parse
import urllib.request
import re
import os
import ssl
import http.cookiejar
import ast
import json
import time
import hashlib
import webbrowser
import random
import datetime

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
ssl._create_default_https_context = ssl._create_unverified_context


@app.route("/", methods=["GET", "POST"])
def helloWorld():
    kk = Lanmu.query[0:8]
    article_title = []
    article_content = []
    article_id_old = []

    houtzhui = '.html'
    for i in range(0, 8):
        zzz = Lanmu.query.filter(Lanmu.lanmuname == kk[i].lanmuname).first()
        kkkasd = zzz.xxxx
        for i in range(len(kkkasd) - 1, 0, -1):
            article_title.append(kkkasd[i].title)
            tqnr_tqnr = re.sub(r'<.*?>', '', kkkasd[i].content)[:100]
            article_content.append(tqnr_tqnr)
            article_id_old.append(kkkasd[i].id)

    for i in range(len(article_id_old)):
        article_id_old[i] = str(article_id_old[i]) + houtzhui
    article_id = article_id_old

    seo_article = {
        'lanmu': kk,
        'article_title': article_title,
        'article_content': article_content,
        'article_id': article_id,
    }

    reg_b = re.compile(
        r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
        re.I | re.M)
    use_agent = request.headers.get('User-Agent')
    # print(type(use_agent))
    # print("这个是UA %s" % use_agent)
    basda = reg_b.search(use_agent)
    # jieguo = Article.query.filter(Article.title == "aaa").all()

    if basda:
        return render_template('m_index.html', **seo_article)
    else:
        return render_template('index.html', **seo_article)
    # return render_template('m_index.html')


@app.route('/qmgl/')
def qmgl():
    kk = Lanmu.query.all()
    len_kk = len(kk)
    article_title = []
    article_content = []
    article_id_old = []
    article_author = []
    article_yuedu = []
    article_time = []
    geishi = '.html'
    for i in range(0, len(kk)):
        zzz = Lanmu.query.filter(Lanmu.lanmuname == kk[i].lanmuname).first()
        kkkasd = zzz.xxxx
        for i in range(len(kkkasd) - 1, len(kkkasd) - 6, -1):
            article_title.append(kkkasd[i].title)
            tqnr_tqnr = re.sub(r'<.*?>', '', kkkasd[i].content)[:100]
            # print(tqnr_tqnr)
            article_content.append(tqnr_tqnr)
            article_id_old.append(kkkasd[i].id)
            article_author.append(kkkasd[i].author_name)
            article_yuedu.append(kkkasd[i].article_yuedu)
            article_time.append(kkkasd[i].article_time)
    for i in range(len(article_id_old)):
        article_id_old[i] = str(article_id_old[i]) + geishi
    article_id = article_id_old

    seo_article = {
        'len_kk': len_kk,
        'lanmu': kk,
        'article_title': article_title,
        'article_content': article_content,
        'article_id': article_id,
        'article_author':article_author,
        'article_yuedu':article_yuedu,
        'article_time':article_time,
    }

    reg_b = re.compile(
        r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
        re.I | re.M)
    use_agent = request.headers.get('User-Agent')
    # print(type(use_agent))
    # print("这个是UA %s" % use_agent)
    basda = reg_b.search(use_agent)
    # jieguo = Article.query.filter(Article.title == "aaa").all()

    if basda:
        return render_template('m_qiminggonglue.html', **seo_article)
    else:
        return render_template('pc_qiminggonglue.html', **seo_article)


#
# @app.route('/cscscs/',methods=["GET", "POST"])
# def cscscs():
#     return render_template('cesecscscs.html')
#

@app.route('/qmgl/<article_idid>')
def wzxq(article_idid):
    quanbuwenzhang = Article.query.all()
    new_article_idid = article_idid.replace('.html', '')
    # 找到了对应id的文章详情
    article = Article.query.filter(Article.id == new_article_idid).first()
    lanmu = article.authorkkk.lanmuname
    zzz = Lanmu.query.filter(Lanmu.lanmuname == lanmu).first()
    # 找到同一个栏目下的全部文章
    article_wzxq = zzz.xxxx

    article_title_ls = []
    # 相关的5篇文章id不带后缀的
    article_id_ls = []
    houzhui = '.html'

    # 这里是生成的相关文章
    for i in range(5, -1, -1):
        article_id_ls.append(article_wzxq[i].id)
        article_title_ls.append(article_wzxq[i].title)


    # 剔除这篇文章，不让在相关文章中调用
    if int(new_article_idid) in article_id_ls:

        kk = article_id_ls.index(int(new_article_idid))
        # print('kkkk % s' % kk)
        article_title_ls.remove(article_title_ls[kk])
        article_id_ls.remove(article_id_ls[kk])
    else:
        pass
    # article_id_ls.remove()

    # print('这个是剔除后的ID %s' % article_id_ls)
    # 给相关文章的id加上后缀
    for m in range(len(article_id_ls)):
        article_id_ls[m] = str(article_id_ls[m]) + houzhui
    new_article_id_ls = article_id_ls

    more_qmgl_title = []
    more_qmgl_id = []

    for i in range(len(quanbuwenzhang) - 1, -10, -1):
        if len(more_qmgl_id) < 11:
            more_qmgl_id.append(quanbuwenzhang[i].id)
            more_qmgl_title.append(quanbuwenzhang[i].title)
        else:
            pass
    # print('全部i的列表 %s' % more_qmgl_id)
    # print('传输的id % s' % int(new_article_idid))
    # print('这个是全部标题的长度 % s' % len(more_qmgl_title))
    if int(new_article_idid) in more_qmgl_id:
        kk = more_qmgl_id.index(int(new_article_idid))
        # print('gengduobiaoti % s' % kk)
        more_qmgl_id.remove(int(new_article_idid))
        more_qmgl_title.remove(more_qmgl_title[kk])
    else:
        pass

    for i in range(len(more_qmgl_id)):
        more_qmgl_id[i] = str(more_qmgl_id[i]) + houzhui
    new_more_qmgl_id = more_qmgl_id
    article_content = {
        'article_content': article.content,
        'article_title': article.title,
        'article_desc':article.description,
        'article_title_ls': article_title_ls,
        'more_qmgl_title': more_qmgl_title,
        'more_qmgl_id': new_more_qmgl_id,
        'article': article.author_name,
        'new_article_id_ls': new_article_id_ls,  # 这个是带有后缀的相关文章id
    }
    reg_b = re.compile(
        r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
        re.I | re.M)
    use_agent = request.headers.get('User-Agent')
    # print(type(use_agent))
    # print("这个是UA %s" % use_agent)
    basda = reg_b.search(use_agent)
    # jieguo = Article.query.filter(Article.title == "aaa").all()

    if basda:
        return render_template('m_wzxq.html', **article_content)
    else:
        return render_template('pc_wzxq.html', **article_content)


@app.route('/<lm_lujin>/')
def zhuanshu_lanmu(lm_lujin):
    lanmu_canshu = 'robots.txt'
    if lm_lujin == lanmu_canshu:
        base_dir = os.path.dirname(__file__)
        resp = make_response(open(os.path.join(base_dir, 'robots.txt')).read())
        resp.headers["Content-type"] = "text/plan;charset=UTF-8"
        return resp

    else:
        lanmu = Lanmu.query.filter(Lanmu.lanmu_lujin == lm_lujin).first()
        # print('zhdge shi lanmu name  % s' % lanmu.lanmuname)
        # lanmu_name = lanmu.lanmuname
        lanmu_qbwz = lanmu.xxxx

        qbwz_jieduan = []
        title = []
        artilce_id = []
        article_author = []
        article_yuedu = []
        article_time = []
        for i in range(len(lanmu_qbwz) - 1, 0, -1):
            tqnr_tqnr = re.sub(r'<.*?>', '', lanmu_qbwz[i].content)[:200]
            qbwz_jieduan.append(tqnr_tqnr)
            title.append(lanmu_qbwz[i].title)
            artilce_id.append(lanmu_qbwz[i].id)
            article_author.append(lanmu_qbwz[i].author_name)
            article_yuedu.append(lanmu_qbwz[i].article_yuedu)
            article_time.append(lanmu_qbwz[i].article_time)
        houzhui = '.html'
        for i in range(len(artilce_id)):
            artilce_id[i] = str(artilce_id[i]) + houzhui
        article_new_id = artilce_id
        len_id = len(artilce_id)

        zidian = {
            'lanmu_name': lanmu.lanmuname,
            'lanmu_desc': lanmu.lanmu_desc,
            'lanmu_qbwz_jieduan': qbwz_jieduan,
            'lanmu_title': title,
            'artilce_id': article_new_id,
            'len_id': len_id,
            'article_author':article_author,
            'article_yuedu':article_yuedu,
            'article_time':article_time,
        }
        reg_b = re.compile(
            r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
            re.I | re.M)
        use_agent = request.headers.get('User-Agent')
        # print(type(use_agent))
        # print("这个是UA %s" % use_agent)
        basda = reg_b.search(use_agent)

    if basda:
        return render_template('m_lmzt.html', **zidian)
    else:
        return render_template('pc_lmzt.html', **zidian)


@app.route("/csjg/", methods=["GET", "POST"])
def csjg():
    if request.method == 'POST':

        global qiwang_dongtai, qiwang_dt_lb, qiwang_dt_lb_1, qiwang_dt_nb_new, qiwang_zhuanhua, qiwang_quanbu, qiwang_dt_nb
        qiwang_quanbu = ['占位', '优雅', '爱国', '吉祥', '美好', '明理', 'zhan', '美德', '幸福', 'zhan', 'zhan', 'zhan', 'zhan',
                         '浩大',
                         '英俊', '健壮', '美丽', '安康', '年轻', '快乐', '灵巧', '勇敢', '坚强', '稳重', '文静', '贤淑', '才华', '智慧', '谦虚',
                         '正直',
                         '纯洁', '志向', 'zhan', '杰出', '上进心', '富裕', '优秀', '温顺', '担当', 'zhan', '传承', '善良', ]
        qiwang_dongtai = request.values.getlist("qiwang")

        qiwang_dongtai_re = re.sub(r'[(\')(\[)(\])]', '', str(qiwang_dongtai))
        qiwang_dongtai_list = list(qiwang_dongtai_re.split(','))
        qiwang_dt_nb_str = []
        if qiwang_dongtai_list[0]:
            qiwang_dt_nb = list(map(int, qiwang_dongtai_list))
            for i in qiwang_dt_nb:
                qiwang_dt_nb_str.append(qiwang_quanbu[int(i)])
            if len(qiwang_dt_nb) == 3:
                qiwang_dt_nb_new = str(qiwang_dt_nb[0]) + "," + str(qiwang_dt_nb[1]) + "," + str(qiwang_dt_nb[2])
                qiwang_zhuanhuan = type(qiwang_quanbu)(map(lambda i: qiwang_quanbu[i], qiwang_dt_nb))
            elif len(qiwang_dt_nb) == 2:
                qiwang_dt_nb_new = str(qiwang_dt_nb[0]) + "," + str(qiwang_dt_nb[1])
                qiwang_zhuanhuan = type(qiwang_quanbu)(map(lambda i: qiwang_quanbu[i], qiwang_dt_nb))
            else:
                qiwang_dt_nb_new = str(qiwang_dt_nb[0])
                qiwang_zhuanhuan = type(qiwang_quanbu)(map(lambda i: qiwang_quanbu[i], qiwang_dt_nb))
        else:
            qiwang_dt_nb = None
            qiwang_dt_nb_new = ""
            qiwang_zhuanhuan = "未选择"

        # print("这个是qiwang_dt_nb %s" % qiwang_dt_nb)

        xing = request.form.get("xing")

        dingzhi = request.form.get("dingzhi")
        if dingzhi:
            dingzhi_2 = dingzhi
        else:
            dingzhi_2 = ''

        biaodan_xz = request.form.get("biaodan_xz")
        mizi_ku_nm = request.form.get("mizi_ku_nm")
        # print("这个是提交的名字： %s" % mizi_ku_nm)
        # print(type(mizi_ku_nm))
        birthtime = request.form.get("birthtime")
        # birthtime = '2020-04-04 13:32'
        # 将提交的性别进行重现赋值
        ba_mp_sex = request.form.get("xingbie")
        # print("这个是提交的性别： %s" % ba_mp_sex)

        if ba_mp_sex == "1":
            ba_mp_sex_zhon = "男"
            q_m_url = "s"
            q_m_ze_cl = "py"
        elif ba_mp_sex == "0":
            ba_mp_sex_zhon = "女"
            q_m_url = "s"
            q_m_ze_cl = "py"
        else:
            ba_mp_sex_zhon = "未出生"
            q_m_url = "s2"
            q_m_ze_cl = "py2"

        # 将输入的日期内容按需切片
        ymd_ymd = str(birthtime.split(' ')[0])
        h_h = str((birthtime.split(' ')[1]).split(':')[0])
        i_i = str((birthtime.split(' ')[1]).split(':')[1])
        ba_mp_year = str((birthtime.split(' ')[0]).split("-")[0])
        ba_mp_month = str((birthtime.split(' ')[0]).split("-")[1])
        ba_mp_day = str((birthtime.split(' ')[0]).split("-")[2])

        # 公历转农历
        gl_nl_url = "https://gonglinongli.51240.com/"

        # 构建农历转换请求头
        gl_nl_haders = {
            'authority': 'gonglinongli.51240.com',
            'method': 'POST',
            'path': '/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed-exchange;v = b3;q = 0.9',
            # 'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN, zh;q=0.9',
            'cache-control': 'no-cache',
            'content-length': '43',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'BAIDU_SSP_lcr= https://www.baidu.com/link?url=ZFeSXmVcZyF09greJ6og4cKT-kLPfPH54GsjbpA-e0oD_xydA2aHYIQ9v5KGQlR1&wd=&eqid=9a1fd0a900295a3a000000065e36f4ee;__gads=ID=803bb3b14c69f57f: T = 1580659957:S=ALNI_MZYauQaE4D5qH6sRGH_tg56wwz8Ng;Hm_lvt_fbe0e02a7ffde424814bef2f6c9d36eb = 1580659957, 1581685473;Hm_lpvt_fbe0e02a7ffde424814bef2f6c9d36eb=1581685494',
            'origin': 'https://gonglinongli.51240.com',
            'pragma': 'no-cache',
            'referer': 'https://gonglinongli.51240.com/',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure - requests': '1',
            'user-agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, likeGecko) Chrome/79.0.3945.130Safari/537.36',
        }

        # 构建农历转换字典
        gl_nl_form = {
            'gongli_nian': ba_mp_year,
            'gongli_yue': ba_mp_month,
            'gongli_ri': ba_mp_day,
        }
        # 将表单数据encode编码一下
        gl_nl_form_ed = urllib.parse.urlencode(gl_nl_form).encode()

        # 创建请求对象
        gl_nl_requeset = urllib.request.Request(url=gl_nl_url, headers=gl_nl_haders)

        # 发送请求，获取响应内容
        gl_nl_response = urllib.request.urlopen(gl_nl_requeset, data=gl_nl_form_ed).read().decode()

        # 正则匹配提取农历
        # gl_nl_y_m_d_h = re.compile(r"<td bgcolor='#FFFFFF' align='center' style='font-size:16px;'>(.*?)<div class='pmk_sj_show'></div>.*?</td>").findall(str(gl_nl_response))
        # print(str(gl_nl_response))
        matches = re.search(r'16px;">(.*)<div class="pmk_sj_show">', str(gl_nl_response)).group(1)
        # print(matches)
        # 这里是八字命盘
        ba_mp = "https://www.buyiju.com/bazi/"
        # 八字命盘表单数据
        ba_mp_form = {
            'year': ba_mp_year,
            'month': ba_mp_month,
            'day': ba_mp_day,
            'hour': h_h,
            'sex': "男",
            'action': 'test',
        }
        # 将表单数据encode编码一下
        ba_mp_form_ed = urllib.parse.urlencode(ba_mp_form).encode()

        # 创建八字命盘请求头
        ba_mp_request = {
            'authority': 'www.buyiju.com',
            'method': 'POST',
            'path': '/bazi/',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'Hm_lvt_0282956784a69e8d921f9a8ae09c09ad=1580542815; ASPSESSIONIDQUASBRCA=LOGBPHGCAFIPNPEAEDKPGNPC; sex=%E7%94%B7; hour=0; month=2; day=15; year=1985; ASPSESSIONIDSWBTAQDB=PADMNDDDFHGOAKGDCEGCLNMO; ASPSESSIONIDSWDSDTBB=BDCAAOMCEKOGCBJJNHCOBAEI; ASPSESSIONIDAWTATTTR=GHIHGNLCOAPAJIKDFOJNHNCN; ASPSESSIONIDCUQATSTR=IDEJGNLCMHHONOEBHIPKMMAB; Hm_lpvt_0282956784a69e8d921f9a8ae09c09ad=1581642236',
            'origin': 'https://www.buyiju.com',
            'pragma': 'no-cache',
            'referer': 'https://www.buyiju.com/bazi/',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }

        # 构建请求对象
        ba_mp_dx = urllib.request.Request(url=ba_mp, headers=ba_mp_request)

        # 发送请求，获取响应内容
        ba_mp_nr = urllib.request.urlopen(ba_mp_dx, data=ba_mp_form_ed).read().decode()

        # 正则表达式提取八字年月
        ba_mp_y_m_d_h = re.compile(r'<p><strong>八字：</strong>(.*?)</p>', re.S).findall(str(ba_mp_nr))[0]

        # 正则表达式提取八字命盘相关内容&过滤所需内容
        ba_mp_ze_1 = re.compile(r'<td .*?>(.*?)</td>', re.S).findall(str(ba_mp_nr))
        ba_mp_ze_2 = re.compile(r'<td .*?><b>(.*?)</b></td>', re.S).findall(str(ba_mp_nr))
        ba_mp_ze_1[10:14] = ba_mp_ze_2
        ba_mp_ze_1.remove(ba_mp_ze_1[15])
        ba_mp_zd = [
            {"key_0": ba_mp_ze_1[0],
             "key_1": ba_mp_ze_1[1],
             "key_2": ba_mp_ze_1[2],
             "key_3": ba_mp_ze_1[3],
             "key_4": ba_mp_ze_1[4],
             },
            {"key_0": ba_mp_ze_1[5],
             "key_1": ba_mp_ze_1[6],
             "key_2": ba_mp_ze_1[7],
             "key_3": ba_mp_ze_1[8],
             "key_4": ba_mp_ze_1[9],
             },
            {"key_0": ba_mp_ze_1[10],
             "key_1": ba_mp_ze_1[11],
             "key_2": ba_mp_ze_1[12],
             "key_3": ba_mp_ze_1[13],
             "key_4": ba_mp_ze_1[14],
             },
            {"key_0": ba_mp_ze_1[15],
             "key_1": ba_mp_ze_1[16],
             "key_2": ba_mp_ze_1[17],
             "key_3": ba_mp_ze_1[18],
             "key_4": ba_mp_ze_1[19],
             },
            {"key_0": ba_mp_ze_1[20],
             "key_1": ba_mp_ze_1[21],
             "key_2": ba_mp_ze_1[22],
             "key_3": ba_mp_ze_1[23],
             "key_4": ba_mp_ze_1[24],
             },
            {"key_0": ba_mp_ze_1[25],
             "key_1": ba_mp_ze_1[26],
             "key_2": ba_mp_ze_1[27],
             "key_3": ba_mp_ze_1[28],
             "key_4": ba_mp_ze_1[29],
             },
        ]

        # 正则表达式提取八字命盘五行个数
        ba_mp_wuxing = re.search(r'<p>五行个数：(.*)。</p>', ba_mp_nr).group(1)
        ba_mp_gs = re.compile((r'([\d]+)个')).findall(ba_mp_wuxing)
        ba_mp_gs = list(map(int, ba_mp_gs))
        # 生产大写对照列表
        ba_mp_dx = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
        # 将生成的数字列表转化成大写
        ba_mp_dx_new = type(ba_mp_dx)(map(lambda i: ba_mp_dx[i], ba_mp_gs))
        # 将八字个数生成列表
        ba_mp_ge_yz = [
            {
                "wuxing": "金",
                "wx_ge": ba_mp_dx_new[0]
            },
            {
                "wuxing": "木",
                "wx_ge": ba_mp_dx_new[1]
            },
            {
                "wuxing": "水",
                "wx_ge": ba_mp_dx_new[2]
            },
            {
                "wuxing": "火",
                "wx_ge": ba_mp_dx_new[3]
            },
            {
                "wuxing": "土",
                "wx_ge": ba_mp_dx_new[4]
            },
        ]

        # 正则表达式提取"帮扶日主的五行"
        ba_mp_bfrz = re.search(r'帮扶日主的五行：(.*)</p>', str(ba_mp_nr), re.M).group(1)
        # 正则表达式提取"帮扶日主的五行"
        ba_mp_wxsq = re.search(r'五行是否所缺：(.*)</p>', str(ba_mp_nr)).group(1)
        # 正则匹配日柱命理内容
        # ba_mp_day = str((request.form.get("birthtime").split(' ')[0]).split("-")[2])
        ba_mp_rzml_2 = re.search(r'命理</h3>\s(.*?)<h3>年命', str(ba_mp_nr), re.S).group(1)
        # 将里面多余的字段进行替换
        ba_mp_rzml_3 = re.sub(r'<p>', '', ba_mp_rzml_2)
        # 按照</p>进行切片
        ba_mp_rzml_4 = ba_mp_rzml_3.split('</p>')[0]
        ba_mp_rzml_5 = ba_mp_rzml_3.split('</p>')[1]
        ba_mp_rzml_6 = ba_mp_rzml_3.split('</p>')[2]
        ba_mp_rzml_7 = ba_mp_rzml_3.split('</p>')[3]
        ba_mp_rzml_8 = ba_mp_rzml_3.split('</p>')[4]

        # 八字测算
        ba_mp_bzcs = re.search(r'<p>●(.*\s.*)<br><br>', str(ba_mp_nr), re.S).group(1)
        ba_mp_bzcs_qx = re.sub(r'\r\n', '', str(ba_mp_bzcs))
        #         # print(ba_mp_bzcs_qx)
        ba_mp_bzcs_qp = ba_mp_bzcs_qx.split('<br>●  ')
        #         # print(type(ba_mp_bzcs_qp))
        #         # print(ba_mp_bzcs_qp)

        # 三命会通
        ba_mp_smth = re.compile(r'三命通会</h3>((\s.*){3})</p>', re.M)
        ba_mp_smth = ba_mp_smth.findall(str(ba_mp_nr))[0]
        #         # print(ba_mp_smth)
        ba_mp_smth_qx_1 = re.sub(r"[('\\r)(\\n)(<p>)]", '', str(ba_mp_smth))
        ba_mp_smth_qx_2 = re.sub(r", ", '/', str(ba_mp_smth_qx_1))
        #         # print(ba_mp_smth_qx_2)
        ba_mp_smth_qp = ba_mp_smth_qx_2.split('/')

        #         # print("三命通会最终结果 %s" % ba_mp_smth_qp)

        def zhengze(response):
            # 编写正则规则
            global lt_lt_mz
            m_z_ku_gz = "<div class='" + q_m_ze_cl + "'>.*?<b .*?>(.*?)</b>.*?</div>"
            # print("这个是正则规则 %s" % m_z_ku_gz)
            # 生成名字库

            pattern = re.compile(m_z_ku_gz, re.S)
            lt_lt_mz = pattern.findall(response)[0:10]
            # print("名字库为空的情况 %s" % lt_lt_mz_pd)
            # print("名字库为空的情况列表 %s" % lt_lt_mz_pd[0])

            print("这个是名字库名字库名字库名字库0729 %s" % lt_lt_mz)
            session['name_ku'] = lt_lt_mz
            session.permanent = True
            if lt_lt_mz:
                # print('名字列表7月27日lt_lt_mz名字列表 %s' % lt_lt_mz)
                vip_regex = request.form.get("xing") + "(.)"
                # print('vip_regex %s' % vip_regex)

                vip_mzku_noxing = re.sub(vip_regex, '*', str(lt_lt_mz))
                # print("将名字中间一个字替换成*: %s" % vip_mzku_noxing)
                # print(type(vip_mzku_noxing))

                vip1_mzku_noxing = ast.literal_eval(vip_mzku_noxing)
                # print("将带*的名转化为列表: %s" % vip1_mzku_noxing)

                # print(type(mi_ku_sy))

                # 将生成的名字库去掉前面的姓
                li_lt_mz_noxing = re.sub(request.form.get("xing"), "", str(lt_lt_mz))

                # 正则提取名印象
                mz_yx = re.compile(r"class='item'><span class='yy'>.*?<div class='item am-margin-top-xs", re.S)
                mz_yx_lt = mz_yx.findall(response)[0:10]

                # 清洗正则提取名字印象
                mz_yx_lt_qx = re.sub(r"[(\[a-z\])(\-)(=)(')( )(<span>)]", '', str(mz_yx_lt))
                # print(mz_yx_lt_qx)
                # print(type(mz_yx_lt_qx))
                session['mz_yx_lt_qx'] = mz_yx_lt_qx
                session.permanent = True
                # 如果直接由html提交表单过来，才是的名字印象取第一个，否则取对应的名字的索引
                mz_yx_lt_qx = ast.literal_eval(mz_yx_lt_qx)[0]

                # print('这是个啥 %s' % mz_yx_lt_qx)

                mz_yx_lt_qx_qp = mz_yx_lt_qx.split('/')[0:-3]
                # print("对应名字的名字印象 %s" % mz_yx_lt_qx_qp)
                # print(type(mz_yx_lt_qx_qp))

                global li_lt_mz_noxing_1, q_m_pingying, neirog

                # 将测算结果页面提交的名字库转化为列表，并
                li_lt_mz_noxing_1 = ast.literal_eval(li_lt_mz_noxing)[0]
                # print(li_lt_mz_noxing_1)
                # print("这个是尝试转换的数据 %s" % type(li_lt_mz_noxing_1))

                # 起名网链接
                qi_ming_url = "https://qm.qumingdashi.com/newqiming/index/index"

                # 创建一个cookie对象
                q_m_cook_jar = http.cookiejar.CookieJar()
                q_m_handler = urllib.request.HTTPCookieProcessor(q_m_cook_jar)
                q_M_opener = urllib.request.build_opener(q_m_handler)

                q_m_formdata = {
                    'ad_code_id': '',
                    'order_forms': '',
                    'ad_source': '',
                    'zty': '1',
                    'sex': '1',
                    'token': 'token_1175932555',
                    'qim': 'zhqm',
                    's_bday': '',
                    'from_source': 'newqiming',
                    'surname': xing,
                    'birth_date': birthtime,
                    'date_type': '1',
                    'is_leap': '0',
                    'birth_address': '上海-上海市-黄浦区',
                    'harea': '310101',
                    'name_character': '',
                    'name_expect': '',
                }
                # 处理表单数据
                q_m_formdata_ed = urllib.parse.urlencode(q_m_formdata).encode()
                # 构建起名请求头

                q_m_headers = {
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    # 'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    # 'Content-Length': '309',
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Host': 'qm.qumingdashi.com',
                    'Origin': 'https://qm.qumingdashi.com',
                    'Pragma': 'no-cache',
                    'Referer': 'https://qm.qumingdashi.com/newqiming',
                    'Sec-Fetch-Mode': 'navigate',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-User': '?1',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                }

                # 构建起名网请求对象
                q_m_request = urllib.request.Request(url=qi_ming_url, headers=q_m_headers)
                # print("这个是请求的链接 %s" % q_m_request)
                # 获取响应，必须要用open进行操作，因为这里面带着cookie
                q_m_response = q_M_opener.open(q_m_request, data=q_m_formdata_ed)
                # 下面是提交信息成功后的，进入名字详情页的操作
                # 起名网名字详情链接
                q_m_mingzi = "https://qm.qumingdashi.com/newqiming/index/detail?"

                q_m_mz_formdata = {
                    'surname': xing,
                    'name': li_lt_mz_noxing_1,
                }
                # 将变量进行拼接
                q_m_mz_pj = urllib.parse.urlencode(q_m_mz_formdata)
                q_m_mingzi += q_m_mz_pj
                # print(q_m_mingzi)
                # 构建请求头
                q_m_headers = {
                    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
                }
                # 构建请求对象
                q_m_xq_request = urllib.request.Request(url=q_m_mingzi, headers=q_m_headers)

                # 发送请求，获取响应
                q_m_mz_xq_response = q_M_opener.open(q_m_xq_request).read().decode()

                # 开始正则，对响应的内容进行数据的提取
                # 首先提取的是拼音
                q_m_pingying_b = re.search(r'的读音是(.*?)，声调为', str(q_m_mz_xq_response), re.M).group(1)
                q_m_pingying = re.sub('、', ' ', q_m_pingying_b)
                # print(q_m_pingying)
                # 接着是字义内涵
                q_m_hanyi_quanbu = re.search(r'class="co_s">(.：.*)</p>', str(q_m_mz_xq_response)).group(1)
                # print(q_m_hanyi_quanbu)
                q_m_hanyi_1 = re.search(r'(.*?)<span class="co_s">', str(q_m_hanyi_quanbu), re.S).group(1)
                # print(type(q_m_hanyi_1))
                # print("第一个名未清洗: %s" % q_m_hanyi_1)
                q_m_hanyi_1_1 = re.sub('</span>', '', str(q_m_hanyi_1))
                # print("第一个名已清洗: %s" % q_m_hanyi_1_1)

                q_m_hanyi_2 = re.search(r'<span class="co_s">(.*)', str(q_m_hanyi_quanbu), re.S).group(1)
                q_m_hanyi_2_2 = re.sub('[(<span>)(\[a-z\])(<>_")(\/)( )]', '', str(q_m_hanyi_2))
                # print("第二个名已清洗: %s" % q_m_hanyi_2_2)

                # 开始正则打分项
                q_m_zh_df = re.search(r'综合评分</p><span>(.*?)</span>', str(q_m_mz_xq_response), re.S).group(1)
                # print("综合打分 %s" % q_m_zh_df)
                # 其他打分项
                q_m_qt_df = re.compile(r'\d+分</b></div>').findall(q_m_mz_xq_response)
                q_m_qt_df_qx = re.sub("</b></div>", "", str(q_m_qt_df))
                q_m_qt_df_qx_lt = ast.literal_eval(q_m_qt_df_qx)

                # 引经据典
                q_m_yjjd = re.compile(r'<p>来自(.*?)</p>').findall(q_m_mz_xq_response)
                q_m_yjjd_qx_1 = re.sub('<span class="co_red">', '', str(q_m_yjjd))
                q_m_yjjd_qx_2 = re.sub('</span>', '', str(q_m_yjjd_qx_1))
                q_m_yjjd_qx_3 = ast.literal_eval(q_m_yjjd_qx_2)
                # print("引经据典: %s" % q_m_yjjd_qx_3)

                # 八字开运
                q_m_bzky = re.search(r'(八字偏.*\s.*)，', str(q_m_mz_xq_response), re.M).group(1)
                # print("八字开运: %s" % q_m_bzky)
                q_m_bzky_qx = re.sub(r'[(<>)(\/)( )(\[a-z\])(_\"=)]', '', q_m_bzky)
                # print("八字开运清洗后数据: %s" % q_m_bzky_qx)

                # 大师点评
                q_m_dsdp = re.search(r'大师点评：.*\s.*\s.*<p>(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                # print("大师点评: %s" % q_m_dsdp)

                # 生肖性格优势标签
                q_m_sxxg = re.search(r'性格优点：</dt>\s.*\.*(\s.*\s.*\s.*\s*\s.*\s.*?)</span>', str(q_m_mz_xq_response),
                                     re.M).group(1)
                # print(q_m_sxxg)
                q_m_sxxg_qx = re.sub(r'[(<span>)( )(<dd class="p_b30 youdisn clearfix">)]', '', str(q_m_sxxg))
                q_m_sxxg_qp_1 = q_m_sxxg_qx.split('</span>')
                q_m_sxxg_qp_2 = re.sub(r'[(n)(r)(\\\)(\')(\[)(\])]', '', str(q_m_sxxg_qp_1))
                # print(q_m_sxxg_qp_2)
                q_m_sxxg_qp = q_m_sxxg_qp_2.split("/")
                # print("生肖性格优点 %s" % q_m_sxxg_qp)
                # print(type(q_m_sxxg_qp))

                # 生肖性格缺点标签啊
                q_m_sxxg_qd = re.search(r'性格缺点：</dt>\s.*\.*(\s.*\s.*\s.*\s*\s.*\s.*?)</span>', str(q_m_mz_xq_response),
                                        re.M).group(1)
                # print(q_m_sxxg_qd)
                q_m_sxxg_qd_qx = re.sub(r'[(<span>)( )(<dd class="clearfix">)]', '', str(q_m_sxxg_qd))
                q_m_sxxg_qd_qp = q_m_sxxg_qd_qx.split('</span>')
                q_m_sxxg_qd_qp_1 = re.sub(r"[(n)(r)(\\\)(\')(\[)(\])]", '', str(q_m_sxxg_qd_qp))
                q_m_sxxg_qd_qp_2 = q_m_sxxg_qd_qp_1.split('/')
                # print("生肖性格缺点 %s" % q_m_sxxg_qd_qp_2)
                # print(type(q_m_sxxg_qd_qp_2))
                # 生肖评分解释
                q_m_sxxg_jies1 = re.search(r'生肖评分解释：(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                q_m_sxxg_jies = re.sub(r'[(\[a-z\])(\d)(")(_)(\/)(<>)( )]', '', str(q_m_sxxg_jies1))
                # print("生肖评分解释 %s" % q_m_sxxg_jies)
                # 什么星座
                q_m_sm_xz = re.search(r'class="f_s16 f_w700 p_b15">星座：(.*)<span class="co_999 f_s14 f_w400">',
                                      str(q_m_mz_xq_response), re.M).group(1)
                # print("什么星座 %s" % q_m_sm_xz)
                #  星座性格优势
                q_m_sm_xz_yd = re.search(r'dd class="p_b30 youdisn clearfix">.*((\s.*){7})</span>',
                                         str(q_m_mz_xq_response),
                                         re.M).group(1)
                # print(q_m_sm_xz_yd)
                q_m_sm_xz_yd_qx = re.sub(r'[(<span>)(\\)( )(\n)(\r)(\')(\[)(\])]', '', str(q_m_sm_xz_yd))
                # print(q_m_sm_xz_yd_qx)
                q_m_sm_xz_yd_qx_qp = q_m_sm_xz_yd_qx.split('/')
                # print("星座性格优势 %s" % q_m_sm_xz_yd_qx_qp)
                # print(type(q_m_sm_xz_yd_qx_qp))

                # 星座缺点
                q_m_sm_xz_qd = re.search(r'座缺点：</dt>((\s.*){6})', str(q_m_mz_xq_response), re.M).group(1)
                # print(q_m_sm_xz_qd)
                # print(type(q_m_sm_xz_qd))
                q_m_sm_xz_qd_qx = re.sub(r'[(<span>)( )(<dd class="clearfix">)(\r)(\n)]', '', str(q_m_sm_xz_qd))
                # print("星座缺点清洗后的数据: %s" % q_m_sm_xz_qd_qx)
                q_m_sm_xz_qd_qp = q_m_sm_xz_qd_qx.split("/")
                q_m_sm_xz_qd_qp = q_m_sm_xz_qd_qp[0:-1]
                # print("星座缺点切片: %s" % q_m_sm_xz_qd_qp)

                # 星座评分解释
                q_m_xz_pfjs = re.search(r'星座评分解释(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                q_m_xz_pfjs_pf = re.sub(r'：', '', str(q_m_xz_pfjs))
                # print("星座评分解释 %s" % q_m_xz_pfjs_pf)

                # 三才五格正则
                # 名字的前两个格
                q_m_scwg_qb = re.compile(r'<p>(. \d+)</p>').findall(q_m_mz_xq_response)
                # print("全部三才五格 %s" % q_m_scwg_qb)
                # 第二个名
                q_m_scwg_ming_2 = re.search(r'<p>(.&nbsp;\d+) </p>', str(q_m_mz_xq_response), re.M).group(1)
                q_m_scwg_ming_2_qx = re.sub(r'&nbsp;', ' ', str(q_m_scwg_ming_2))
                # print(q_m_scwg_ming_2_qx)

                # 天格
                q_m_scwg_tiange = re.search(r'<p>天格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                # print("天格 %s" % q_m_scwg_tiange)
                # 地格
                q_m_scwg_dige = re.search(r'<p>地格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                # print("地格 %s" % q_m_scwg_dige)
                # 人格
                q_m_scwg_renge = re.search(r'<p>人格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
                # print("人格 %s" % q_m_scwg_renge)
                # 外格
                q_m_scwg_waige = re.search(r'<em>外格(.*)</em>', str(q_m_mz_xq_response), re.M).group(1)
                # print("外格 %s" % q_m_scwg_waige)
                # 总格
                q_m_scwg_zongge = re.search(r'总格.(\d+)', str(q_m_mz_xq_response), re.M).group(1)
                # print("总格 %s" % q_m_scwg_zongge)
                # 天格解释
                q_m_scwg_tiange_jx = re.search(r'天格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("天格解释 %s" % q_m_scwg_tiange_jx)
                # 地格解释
                q_m_scwg_dige_jx = re.search(r'地格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("地格解释 %s" % q_m_scwg_dige_jx)
                # 人格解释
                q_m_scwg_renge_jx = re.search(r'人格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("人格解释 %s" % q_m_scwg_renge_jx)
                # 外格解释
                q_m_scwg_waige_jx = re.search(r'外格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("外格解释 %s" % q_m_scwg_waige_jx)
                # 总格解释

                q_m_scwg_zongge_jx = re.search(r'总格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("总格解释 %s" % q_m_scwg_zongge_jx)
                # 三才解析
                q_m_scwg_scwg_jx = re.search(r'三才解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("三才解析 %s" % q_m_scwg_scwg_jx)
                # 基础运解析
                q_m_scwg_jcy_jx = re.search(r'基础运解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("基础运解析 %s" % q_m_scwg_jcy_jx)
                # 成功运解析
                q_m_scwg_cgy_jx = re.search(r'成功运解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("成功运解析 %s" % q_m_scwg_cgy_jx)
                # 人际关系解析
                q_m_scwg_rjgx_jx = re.search(r'人际关系解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("人际关系解析 %s" % q_m_scwg_rjgx_jx)
                # 性格影响解析
                q_m_scwg_xg_jx = re.search(r'性格影响解析.*_h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
                # print("性格影响解析 %s" % q_m_scwg_xg_jx)

                # 周易八卦正则

                # 名字卦象解析
                q_m_gx_jx = re.search(r'名字卦象解析</div>(\s.*)专家解卦</div>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gx_jx_qx = re.sub(
                    r'[(<div class="f_s16 line_h170">)(<div style="border-top: 1px dashed #efefef;height: 0;" class="m_t20"><div>)(\r)(\n)(<p>)(<p class="pb5">)( <div class="f_s16 f_w700 p_t20 p_b10">)(-)( )]',
                    '', str(q_m_gx_jx))
                q_m_gx_jx_qp = q_m_gx_jx_qx.split("/")
                q_m_gx_jx_qp_2 = q_m_gx_jx_qp[0:-3]
                # print("名字卦象解析: %s" % q_m_gx_jx_qp_2)
                # #解卦
                q_m_zybg_jg = re.search(r'专家解卦</div>(\s.*)<div class="f_s16 f_w700">卦象运势解析', str(q_m_mz_xq_response),
                                        re.S).group(1)
                # print("专家解卦：%s" % q_m_zybg_jg)
                q_m_zybg_jg_qx = re.sub(r'[(\[a-z\])(<)(>)( )(=)(")(;)(\d)(_)(:)(-)(#)(\n)(\r)]', '', str(q_m_zybg_jg))
                # print("专家解卦2：%s" % q_m_zybg_jg_qx)
                q_m_zybg_jg_qx2 = q_m_zybg_jg_qx.split("/")[0:-2]
                del q_m_zybg_jg_qx2[1]
                # print("专家解卦3：%s" % q_m_zybg_jg_qx2)

                # 卦象运势解析
                q_m_gxys_jx_dx = re.search(r'大象：</dt>\s.*p_b10">(.*)总论：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_dx_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_dx))
                # print("大象 %s" % q_m_gxys_dx_qx)
                q_m_gxys_jx_zl = re.search(r'总论：</dt>\s.*p_b10">(.*)建议：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_zl_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_zl))
                # print("总论 %s" % q_m_gxys_zl_qx)
                q_m_gxys_jx_jy = re.search(r'建议：</dt>\s.*p_b10">(.*)事业：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_jy_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_jy))
                # print("建议 %s" % q_m_gxys_jy_qx)
                q_m_gxys_jx_sy = re.search(r'事业：</dt>\s.*p_b10">(.*)经商：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_sy_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_sy))
                # print("事业 %s" % q_m_gxys_sy_qx)
                q_m_gxys_jx_js = re.search(r'经商：</dt>\s.*p_b10">(.*)求名：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_js_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_js))
                # print("经商 %s" % q_m_gxys_js_qx)
                q_m_gxys_jx_qm = re.search(r'求名：</dt>\s.*p_b10">(.*)婚恋：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_qm_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_qm))
                # print("求名 %s" % q_m_gxys_qm_qx)
                q_m_gxys_jx_hl = re.search(r'婚恋：</dt>\s.*p_b10">(.*)没有下一条', str(q_m_mz_xq_response), re.S).group(1)
                q_m_gxys_hl_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)(:C;)]', '', str(q_m_gxys_jx_hl))
                # print("婚恋 %s" % q_m_gxys_hl_qx)

                # 音形义详解
                # 名字拆分
                q_m_yxy_ming = re.compile(r'<em class="zis">(.)</em>').findall(q_m_mz_xq_response)
                # print("名字拆分 %s" % q_m_yxy_ming)

                # 字义解释
                q_m_yxy_zyjs = re.search(r'字义解释：</dt>(\s.*?\s.*)用字解释：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                # 字义解释一
                q_m_yxy_zyjs1 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_zyjs)[0]
                # print("字义解释1则： %s" % q_m_yxy_zyjs1)
                # 字义解释二
                q_m_yxy_zyjs2 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_zyjs)[-1]
                # print("字义解释2则： %s" % q_m_yxy_zyjs2)

                # 用字解释
                q_m_yxy_yzjs = re.search(r'用字解释：</dt>(.*)来源解释：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_yxy_yzjs1 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_yzjs)[0]
                q_m_yxy_yzjs1_qx = re.sub(r'[(<> =_"\/)(\[a-z\])()()()]', '', str(q_m_yxy_yzjs1))
                # print("用字解释1最终版： %s" % q_m_yxy_yzjs1_qx)
                q_m_yxy_yzjs2_qx = re.search(r'用字解释：</dt>(\s.*\s.*)', str(q_m_yxy_yzjs), re.S).group(1)
                q_m_yxy_yzjs22_qx = re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)]', '', str(q_m_yxy_yzjs2_qx))
                # print("用字解释2最终版： %s" % q_m_yxy_yzjs22_qx)

                # 来源解释已经有了，不需要在单独提取

                # 字义分析
                q_m_yxy_zyfx = re.search(r'字义分析：</dt>(.*)音律分析：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_yxy_zyfx_qx1 = re.compile(r'<p>(.*)</p>').findall(q_m_yxy_zyfx)
                # print("字义分析列表： %s" % q_m_yxy_zyfx_qx1)

                # 音律分析
                q_m_yxy_ylfx = re.search(r'音律分析：</dt>(.*)字型分析：</dt>', str(q_m_mz_xq_response), re.S).group(1)
                # print("音律分析： %s" % q_m_yxy_ylfx)
                q_m_yxy_ylfx_qx = re.search(r'p_b10">(.*)</dd>', str(q_m_yxy_ylfx), re.S).group(1)
                # print("音律分析最终版： %s" % q_m_yxy_ylfx_qx)

                # 字型分析
                q_m_yxy_zxfx = re.search(r'字型分析：</dt>(.*)大师点评</div>', str(q_m_mz_xq_response), re.S).group(1)
                q_m_yxy_zxfx_lt = re.compile(r'<p>(.*)</p>', re.S).findall(q_m_yxy_zxfx)
                q_m_yxy_zxfx_lt2 = re.sub(r'[(\r\n<>p  \\)(\[\])(\')(rn)( )(\[a-z\])(\d+)(;)(")(_=)]', '',
                                          str(q_m_yxy_zxfx_lt)).split("/")
                # print("字型分析列表2： %s" % q_m_yxy_zxfx_lt2)

                # 大师点评
                q_m_yxy_dsdp = re.search(r'大师点评</div>(.*)下一条，八字五行分析', str(q_m_mz_xq_response), re.S).group(1)
                # print("大师点评： %s" % q_m_yxy_dsdp)
                q_m_yxy_dsdp_qx = re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)(:I;)]', '', str(q_m_yxy_dsdp))
                # print("大师点评数据清洗： %s" % q_m_yxy_dsdp_qx)
                qiwang_dt_nb_str = []
                if qiwang_dongtai_list[0]:
                    for i in qiwang_dt_nb:
                        qiwang_dt_nb_str.append(qiwang_quanbu[int(i)])
                else:
                    qiwang_dt_nb_str = ['未选择']
                pingjia = Pingjia.query.all()
                pingjia_content_ls = []
                for i in pingjia:
                    pingjia_content_ls.append(i.content)

                # 这里随机生成评价内容长度一样的城市列表
                city = City.query.all()
                city_list = []
                for i in range(0, len(pingjia_content_ls)):
                    suijishu = random.randint(0, len(city) - 1)
                    city_list.append(city[suijishu].city_name)

                city_fenzu = []
                pingjia_fenzhu = []
                n = 4
                h = 0
                for i in range(0, n):
                    m = int(len(pingjia_content_ls) / n)
                    if i == n - 1:
                        obj = pingjia_content_ls[h:]
                        obj_city = city_list[h:]
                    else:
                        obj = pingjia_content_ls[h:h + m]
                        obj_city = city_list[h:h + m]
                    pingjia_fenzhu.append(obj)
                    city_fenzu.append(obj_city)
                    h = h + m

                # print('这个是评价分组的长度 % s' % len(pingjia_fenzhu))
                # print('这个是评价分组的长度 % s' % type(pingjia_fenzhu[0]))

                # beforeOfDay=random.randint(1, 3)
                today = datetime.datetime.now()
                pingjian_shijian = []
                for i in range(0, 4):
                    offset = datetime.timedelta(days=-i)
                    re_date = (today + offset).strftime('%Y-%m-%d')
                    pingjian_shijian.append(re_date)
                pingjia_fenzhu_one_len = len(pingjia_fenzhu[0])
                pingjia_fenzhu_two_len = len(pingjia_fenzhu[1])
                pingjia_fenzhu_three_len = len(pingjia_fenzhu[2])
                pingjia_fenzhu_four_len = len(pingjia_fenzhu[3])

                neirog = {
                    'mizi_ku_nm': mizi_ku_nm,
                    'xing': xing,
                    'xingbie': ba_mp_sex,
                    "xingbie_zhon": ba_mp_sex_zhon,
                    'dingzhi': dingzhi,
                    'biaodan_xz': biaodan_xz,
                    'qiwang': qiwang_zhuanhuan,
                    'birthtime': birthtime,
                    'birthplace': request.form.get("birthplace"),
                    "mz_ku": lt_lt_mz,
                    "vip1_mzku_noxing": vip1_mzku_noxing,
                    "ba_mp": ba_mp_zd,
                    "ba_mp_y_m_d_h": ba_mp_y_m_d_h,
                    "ba_gl_nl": matches,
                    "ba_mp_gs": ba_mp_ge_yz,
                    "ba_mp_bfrz": ba_mp_bfrz,
                    "ba_mp_wxsq": ba_mp_wxsq,
                    "ba_mp_rzml_4": ba_mp_rzml_4,
                    "ba_mp_rzml_5": ba_mp_rzml_5,
                    "ba_mp_rzml_6": ba_mp_rzml_6,
                    "ba_mp_rzml_7": ba_mp_rzml_7,
                    "ba_mp_rzml_8": ba_mp_rzml_8,
                    "li_lt_mz_noxing_1": li_lt_mz_noxing_1,
                    "q_m_pingying": q_m_pingying,
                    "q_m_hanyi_1_1": q_m_hanyi_1_1,
                    "q_m_hanyi_2_2": q_m_hanyi_2_2,
                    "q_m_zh_df": q_m_zh_df,
                    "q_m_qt_df_qx_lt": q_m_qt_df_qx_lt,
                    "q_m_yjjd_qx_3": q_m_yjjd_qx_3,
                    "q_m_bzky_qx": q_m_bzky_qx,
                    "q_m_dsdp": q_m_dsdp,
                    "mz_yx_lt_qx_qp": mz_yx_lt_qx_qp,
                    "ba_mp_bzcs_qp": ba_mp_bzcs_qp,  # 八字五行详解中的八字测算
                    "ba_mp_smth_qp": ba_mp_smth_qp,  # 三命通会
                    "q_m_sxxg_qp": q_m_sxxg_qp,  # 生肖性格优点
                    "q_m_sxxg_qd_qp": q_m_sxxg_qd_qp_2,  # 生肖性格缺点
                    "q_m_sxxg_jies": q_m_sxxg_jies,  # 生肖性格解释
                    "q_m_sm_xz": q_m_sm_xz,  # 什么星座
                    "q_m_sm_xz_yd_qx_qp": q_m_sm_xz_yd_qx_qp,  # 星座优点
                    "q_m_sm_xz_qd_qp": q_m_sm_xz_qd_qp,  # 星座缺点
                    "q_m_xz_pfjs_pf": q_m_xz_pfjs_pf,  # 星座评分解释
                    "q_m_scwg_qb": q_m_scwg_qb,  # 前两个字的三才五格
                    "q_m_scwg_ming_2_qx": q_m_scwg_ming_2_qx,  # 最后一个字的五格
                    "q_m_scwg_tiange": q_m_scwg_tiange,  # 天格
                    "q_m_scwg_dige": q_m_scwg_dige,  # 地格
                    "q_m_scwg_renge": q_m_scwg_renge,  # 人格
                    "q_m_scwg_waige": q_m_scwg_waige,  # 外格
                    "q_m_scwg_zongge": q_m_scwg_zongge,  # 总格
                    "q_m_scwg_tiange_jx": q_m_scwg_tiange_jx,  # 五格解析
                    "q_m_scwg_dige_jx": q_m_scwg_dige_jx,  # 五格解析
                    "q_m_scwg_renge_jx": q_m_scwg_renge_jx,  # 五格解析
                    "q_m_scwg_waige_jx": q_m_scwg_waige_jx,  # 五格解析
                    "q_m_scwg_zongge_jx": q_m_scwg_zongge_jx,  # 五格解析
                    "q_m_scwg_scwg_jx": q_m_scwg_scwg_jx,  # 五格解析
                    "q_m_scwg_jcy_jx": q_m_scwg_jcy_jx,  # 五格解析
                    "q_m_scwg_cgy_jx": q_m_scwg_cgy_jx,  # 五格解析
                    "q_m_scwg_rjgx_jx": q_m_scwg_rjgx_jx,  # 五格解析
                    "q_m_scwg_xg_jx": q_m_scwg_xg_jx,  # 五格解析
                    "q_m_gx_jx_qp_2": q_m_gx_jx_qp_2,  # 名字卦象解析
                    "q_m_zybg_jg_qx2": q_m_zybg_jg_qx2,  # 专业解卦
                    "q_m_gxys_jx_dx": q_m_gxys_dx_qx,  # 卦象运势解析
                    "q_m_gxys_jx_zl": q_m_gxys_zl_qx,  # 卦象运势解析
                    "q_m_gxys_jx_jy": q_m_gxys_jy_qx,  # 卦象运势解析
                    "q_m_gxys_jx_sy": q_m_gxys_sy_qx,  # 卦象运势解析
                    "q_m_gxys_jx_js": q_m_gxys_js_qx,  # 卦象运势解析
                    "q_m_gxys_jx_qm": q_m_gxys_qm_qx,  # 卦象运势解析
                    "q_m_gxys_jx_hl": q_m_gxys_hl_qx,  # 卦象运势解析
                    "q_m_yxy_ming": q_m_yxy_ming,  # 名字拆分
                    "q_m_yxy_zyjs1": q_m_yxy_zyjs1,  # 字义解释1
                    "q_m_yxy_zyjs2": q_m_yxy_zyjs2,  # 字义解释2
                    "q_m_yxy_yzjs1_qx": q_m_yxy_yzjs1_qx,  # 用字解释1最终版
                    "q_m_yxy_yzjs22_qx": q_m_yxy_yzjs22_qx,  # 用字解释2最终版
                    "q_m_yxy_zyfx_qx1": q_m_yxy_zyfx_qx1,  # 字义分析列表
                    "q_m_yxy_ylfx_qx": q_m_yxy_ylfx_qx,  # 音律分析最终版
                    "q_m_yxy_zxfx_lt2": q_m_yxy_zxfx_lt2,  # 字型分析列表2
                    "q_m_yxy_dsdp_qx": q_m_yxy_dsdp_qx,  # 大师点评数据清洗
                    "ymd_ymd": ymd_ymd,
                    "h_h": h_h,
                    "i_i": i_i,
                    "qiwang_dt_nb_new": qiwang_dt_nb_new,
                    "qiwang_dt_lb_1": qiwang_dt_nb_str,
                    "qiwang_dt_lb_int": qiwang_dt_nb,
                    'pingjian_shijian': pingjian_shijian,  # 这个是生成的评价时间
                    'pingjia_content_ls': pingjia_fenzhu,  # 评价内容分组
                    'pingjia_fenzhu_one_len': pingjia_fenzhu_one_len,
                    'pingjia_fenzhu_two_len': pingjia_fenzhu_two_len,
                    'pingjia_fenzhu_three_len': pingjia_fenzhu_three_len,
                    'pingjia_fenzhu_four_len': pingjia_fenzhu_four_len,
                    'city_fenzu': city_fenzu,
                }
            else:
                kong_tishi = '未生成'
                return redirect(url_for('helloWorld', goodname=kong_tishi))

        huoqu_data_mizi = {
            'sign': 'fy',
            'xing': xing,
            'xb': ba_mp_sex,
            'mzi': dingzhi_2,
            'wz': biaodan_xz,
            'ymd': ymd_ymd,
            'h': h_h,
            'i': i_i,
            'lx': 1,
            'gs': 0,
            'yy': qiwang_dt_nb_new,
            'page': 1,
        }

        data_mizi = urllib.parse.urlencode(huoqu_data_mizi)

        path_new = "/qiming/" + q_m_url + ".php?" + data_mizi
        # print("这个是请求路径： %s " % path_new)
        # 构建请求头——名字吧
        headers = {
            'authority': 'www.mzi8.com',
            'method': 'GET',
            'path': path_new,
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'accept - encoding': 'gzip, deflate, br',
            'accept - language': 'zh-CN,zh;q = 0.9',
            'cache - control': 'no - cache',
            'cookie': 'Hm_lvt_03af629b9001bca5b8986251b864e9ba = 1578922456;mzi8_mz_cookies = %E5%88%98%7C%7C1%7C2019-08-21%7C0%7C0%7C3%7C%7C9;Hm_lpvt_03af629b9001bca5b8986251b864e9ba = 1581263255',
            'pragma': 'no - cache',
            'referer': 'https://www.mzi8.com/qiming/',
            'sec-fetch-mode': 'same - origin',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }

        # 创建起名吧的名字库链接
        get_url = "https://www.mzi8.com/qiming/" + q_m_url + ".php?"

        # 生成新的url
        get_url += data_mizi
        # 构建请求对象
        # print(get_url)
        qu_dx = urllib.request.Request(url=get_url, headers=headers)

        # 发送请求对象,获取响应内容
        response = urllib.request.urlopen(qu_dx).read().decode()
        # print('名字库的响应内容% s' % response)

        zhengze(response)

        # 执行以下函数

        # with open("mxxxp.html" ,"wb") as fp:
        #    fp.write(ba_mp_nr.read())

        # 执行这个函数
        # return json.dumps(pay_url)

        reg_b = re.compile(
            r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
            re.I | re.M)
        use_agent = request.headers.get('User-Agent')
        basda = reg_b.search(use_agent)
        if basda:
            if lt_lt_mz:
                return render_template('mobile_csjg.html', **neirog)
            else:
                kong_tishi = '未生成'
                return redirect(url_for('helloWorld', goodname=kong_tishi))

        else:
            if lt_lt_mz:
                return render_template("csjg.html", **neirog)
            else:
                kong_tishi = '未生成'
                return redirect(url_for('helloWorld', goodname=kong_tishi))
        # return render_template("/csjg.html/", **neirog)

    else:
        # reg_b = re.compile(
        #     r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
        #     re.I | re.M)
        # use_agent = request.headers.get('User-Agent')
        # basda = reg_b.search(use_agent)
        # if basda:
        #     return redirect(url_for('helloWorld'))
        # else:
        #     return redirect(url_for('helloWorld'))

        return redirect(url_for('helloWorld'))


@app.route('/m_ajax/', methods=['GET', 'POST'])
def m_ajax():
    if request.method == 'POST':
        mizi_ku_nm = request.form.get("mizi_ku_nm")
        birthtime = request.form.get("birthtime")
        qi_ming_url = "https://qm.qumingdashi.com/newqiming/index/index"
        xing = mizi_ku_nm[0]
        # print(xing)
        li_lt_mz_noxing_1 = mizi_ku_nm[1:]
        # print(li_lt_mz_noxing_1)

        name = session.get('name_ku')
        mingzi_sy = name.index(mizi_ku_nm)

        ttt = session.get('mz_yx_lt_qx')
        mz_yx_lt_qx = ast.literal_eval(ttt)[mingzi_sy]
        mz_yx_lt_qx_qp = mz_yx_lt_qx.split('/')[0:-3]

        # 创建一个cookie对象
        q_m_cook_jar = http.cookiejar.CookieJar()
        q_m_handler = urllib.request.HTTPCookieProcessor(q_m_cook_jar)
        q_M_opener = urllib.request.build_opener(q_m_handler)

        q_m_formdata = {
            'ad_code_id': '',
            'order_forms': '',
            'ad_source': '',
            'zty': '1',
            'sex': '1',
            'token': 'token_1175932555',
            'qim': 'zhqm',
            's_bday': '',
            'from_source': 'newqiming',
            'surname': xing,
            'birth_date': birthtime,
            'date_type': '1',
            'is_leap': '0',
            'birth_address': '上海-上海市-黄浦区',
            'harea': '310101',
            'name_character': '',
            'name_expect': '',
        }
        # 处理表单数据
        q_m_formdata_ed = urllib.parse.urlencode(q_m_formdata).encode()
        # 构建起名请求头

        q_m_headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive',
            # 'Content-Length': '309',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'qm.qumingdashi.com',
            'Origin': 'https://qm.qumingdashi.com',
            'Pragma': 'no-cache',
            'Referer': 'https://qm.qumingdashi.com/newqiming',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(Macintosh;Intel Mac OS X 10_12_3) AppleWebKit/537.36(KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }

        # 构建起名网请求对象
        q_m_request = urllib.request.Request(url=qi_ming_url, headers=q_m_headers)
        # print("这个是请求的链接 %s" % q_m_request)
        # 获取响应，必须要用open进行操作，因为这里面带着cookie
        q_m_response = q_M_opener.open(q_m_request, data=q_m_formdata_ed)
        # 下面是提交信息成功后的，进入名字详情页的操作
        # 起名网名字详情链接
        q_m_mingzi = "https://qm.qumingdashi.com/newqiming/index/detail?"

        q_m_mz_formdata = {
            'surname': xing,
            'name': li_lt_mz_noxing_1,
        }
        # 将变量进行拼接
        q_m_mz_pj = urllib.parse.urlencode(q_m_mz_formdata)
        q_m_mingzi += q_m_mz_pj
        # print(q_m_mingzi)
        # 构建请求头
        q_m_headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        }
        # 构建请求对象
        q_m_xq_request = urllib.request.Request(url=q_m_mingzi, headers=q_m_headers)

        # 发送请求，获取响应
        q_m_mz_xq_response = q_M_opener.open(q_m_xq_request).read().decode()

        # print('这个是获取的响应对象q_m_mz_xq_response % s' % q_m_mz_xq_response)
        # 开始正则，对响应的内容进行数据的提取
        # 首先提取的是拼音
        q_m_pingying_b = re.search(r'的读音是(.*?)，声调为', str(q_m_mz_xq_response), re.M).group(1)
        q_m_pingying = re.sub('、', ' ', q_m_pingying_b)
        # print('首先提取的是拼音 %s' % q_m_pingying)

        # 接着是字义内涵
        q_m_hanyi_quanbu = re.search(r'class="co_s">(.：.*)</p>', str(q_m_mz_xq_response)).group(1)
        # print(q_m_hanyi_quanbu)
        q_m_hanyi_1 = re.search(r'(.*?)<span class="co_s">', str(q_m_hanyi_quanbu), re.S).group(1)
        # print(type(q_m_hanyi_1))
        # print("第一个名未清洗: %s" % q_m_hanyi_1)
        q_m_hanyi_1_1 = re.sub('</span>', '', str(q_m_hanyi_1))
        # print("第一个名已清洗: %s" % q_m_hanyi_1_1)

        q_m_hanyi_2 = re.search(r'<span class="co_s">(.*)', str(q_m_hanyi_quanbu), re.S).group(1)
        q_m_hanyi_2_2 = re.sub('[(<span>)(\[a-z\])(<>_")(\/)( )]', '', str(q_m_hanyi_2))
        # print("第二个名已清洗: %s" % q_m_hanyi_2_2)

        # 开始正则打分项
        q_m_zh_df = re.search(r'综合评分</p><span>(.*?)</span>', str(q_m_mz_xq_response), re.S).group(1)
        # print("综合打分 %s" % q_m_zh_df)
        # 其他打分项
        q_m_qt_df = re.compile(r'\d+分</b></div>').findall(q_m_mz_xq_response)
        q_m_qt_df_qx = re.sub("</b></div>", "", str(q_m_qt_df))
        q_m_qt_df_qx_lt = ast.literal_eval(q_m_qt_df_qx)

        # print('其他打分项 % s' % q_m_qt_df_qx_lt)
        # 引经据典
        q_m_yjjd = re.compile(r'<p>来自(.*?)</p>').findall(q_m_mz_xq_response)
        q_m_yjjd_qx_1 = re.sub('<span class="co_red">', '', str(q_m_yjjd))
        q_m_yjjd_qx_2 = re.sub('</span>', '', str(q_m_yjjd_qx_1))
        q_m_yjjd_qx_3 = ast.literal_eval(q_m_yjjd_qx_2)
        # print("引经据典: %s" % q_m_yjjd_qx_3)

        # 八字开运
        q_m_bzky = re.search(r'(八字偏.*\s.*)，', str(q_m_mz_xq_response), re.M).group(1)
        # print("八字开运: %s" % q_m_bzky)
        q_m_bzky_qx = re.sub(r'[(<>)(\/)( )(\[a-z\])(_\"=)]', '', q_m_bzky)
        # print("八字开运清洗后数据: %s" % q_m_bzky_qx)

        # 大师点评
        q_m_dsdp = re.search(r'大师点评：.*\s.*\s.*<p>(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        print("大师点评: %s" % q_m_dsdp)

        print('对应的名字印象mz_yx_lt_qx_qp %s ' % mz_yx_lt_qx_qp)

        # 生肖性格优势标签
        q_m_sxxg = re.search(r'性格优点：</dt>\s.*\.*(\s.*\s.*\s.*\s*\s.*\s.*?)</span>', str(q_m_mz_xq_response),
                             re.M).group(1)
        # print('生肖性格优势标签 %s' % q_m_sxxg)

        q_m_sxxg_qx = re.sub(r'[(<span>)( )(<dd class="p_b30 youdisn clearfix">)]', '', str(q_m_sxxg))
        q_m_sxxg_qp_1 = q_m_sxxg_qx.split('</span>')
        q_m_sxxg_qp_2 = re.sub(r'[(n)(r)(\\\)(\')(\[)(\])]', '', str(q_m_sxxg_qp_1))
        # print('生肖性格优势标签q_m_sxxg_qp_2 切片 %s' % q_m_sxxg_qp_2)
        q_m_sxxg_qp = q_m_sxxg_qp_2.split("/")
        # print("生肖性格优点q_m_sxxg_qp %s" % q_m_sxxg_qp)
        # print(type(q_m_sxxg_qp))

        # 生肖性格缺点标签啊
        q_m_sxxg_qd = re.search(r'性格缺点：</dt>\s.*\.*(\s.*\s.*\s.*\s*\s.*\s.*?)</span>', str(q_m_mz_xq_response),
                                re.M).group(1)
        # print(q_m_sxxg_qd)
        q_m_sxxg_qd_qx = re.sub(r'[(<span>)( )(<dd class="clearfix">)]', '', str(q_m_sxxg_qd))
        q_m_sxxg_qd_qp = q_m_sxxg_qd_qx.split('</span>')
        q_m_sxxg_qd_qp_1 = re.sub(r"[(n)(r)(\\\)(\')(\[)(\])]", '', str(q_m_sxxg_qd_qp))
        q_m_sxxg_qd_qp_2 = q_m_sxxg_qd_qp_1.split('/')
        # print("生肖性格缺点 %s" % q_m_sxxg_qd_qp_2)
        # print(type(q_m_sxxg_qd_qp_2))
        # 生肖评分解释
        q_m_sxxg_jies1 = re.search(r'生肖评分解释：(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        q_m_sxxg_jies = re.sub(r'[(\[a-z\])(\d)(")(_)(\/)(<>)( )]', '', str(q_m_sxxg_jies1))
        # print("生肖评分解释 %s" % q_m_sxxg_jies)
        # 什么星座
        q_m_sm_xz = re.search(r'class="f_s16 f_w700 p_b15">星座：(.*)<span class="co_999 f_s14 f_w400">',
                              str(q_m_mz_xq_response), re.M).group(1)
        # print("什么星座 %s" % q_m_sm_xz)
        #  星座性格优势
        q_m_sm_xz_yd = re.search(r'dd class="p_b30 youdisn clearfix">.*((\s.*){7})</span>', str(q_m_mz_xq_response),
                                 re.M).group(1)
        # print(q_m_sm_xz_yd)
        q_m_sm_xz_yd_qx = re.sub(r'[(<span>)(\\)( )(\n)(\r)(\')(\[)(\])]', '', str(q_m_sm_xz_yd))
        # print(q_m_sm_xz_yd_qx)
        q_m_sm_xz_yd_qx_qp = q_m_sm_xz_yd_qx.split('/')
        # print("星座性格优势 %s" % q_m_sm_xz_yd_qx_qp)
        # print(type(q_m_sm_xz_yd_qx_qp))

        # 星座缺点
        q_m_sm_xz_qd = re.search(r'座缺点：</dt>((\s.*){6})', str(q_m_mz_xq_response), re.M).group(1)
        # print(q_m_sm_xz_qd)
        # print(type(q_m_sm_xz_qd))
        q_m_sm_xz_qd_qx = re.sub(r'[(<span>)( )(<dd class="clearfix">)(\r)(\n)]', '', str(q_m_sm_xz_qd))
        # print("星座缺点清洗后的数据: %s" % q_m_sm_xz_qd_qx)
        q_m_sm_xz_qd_qp = q_m_sm_xz_qd_qx.split("/")
        q_m_sm_xz_qd_qp = q_m_sm_xz_qd_qp[0:-1]
        # print("星座缺点切片: %s" % q_m_sm_xz_qd_qp)

        # 星座评分解释
        q_m_xz_pfjs = re.search(r'星座评分解释(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        q_m_xz_pfjs_pf = re.sub(r'：', '', str(q_m_xz_pfjs))
        # print("星座评分解释 %s" % q_m_xz_pfjs_pf)

        # 三才五格正则
        # 名字的前两个格
        q_m_scwg_qb = re.compile(r'<p>(. \d+)</p>').findall(q_m_mz_xq_response)
        # print("全部三才五格q_m_scwg_qb %s" % q_m_scwg_qb)
        # 第二个名
        q_m_scwg_ming_2 = re.search(r'<p>(.&nbsp;\d+) </p>', str(q_m_mz_xq_response), re.M).group(1)
        q_m_scwg_ming_2_qx = re.sub(r'&nbsp;', ' ', str(q_m_scwg_ming_2))
        # print('最后一个名的格 %s' % q_m_scwg_ming_2_qx)

        # 天格
        q_m_scwg_tiange = re.search(r'<p>天格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        # print("天格 %s" % q_m_scwg_tiange)
        # 地格
        q_m_scwg_dige = re.search(r'<p>人格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        # print("地格 %s" % q_m_scwg_dige)
        # 人格
        q_m_scwg_renge = re.search(r'<p>地格(.*)</p>', str(q_m_mz_xq_response), re.M).group(1)
        # print("人格 %s" % q_m_scwg_renge)
        # 外格
        q_m_scwg_waige = re.search(r'<em>外格(.*)</em>', str(q_m_mz_xq_response), re.M).group(1)
        # print("外格 %s" % q_m_scwg_waige)
        # 总格
        q_m_scwg_zongge = re.search(r'总格.(\d+)', str(q_m_mz_xq_response), re.M).group(1)
        # print("总格 %s" % q_m_scwg_zongge)
        # 天格解释
        q_m_scwg_tiange_jx = re.search(r'天格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("天格解释 %s" % q_m_scwg_tiange_jx)
        # 地格解释
        q_m_scwg_dige_jx = re.search(r'地格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("地格解释 %s" % q_m_scwg_dige_jx)
        # 人格解释
        q_m_scwg_renge_jx = re.search(r'人格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("人格解释 %s" % q_m_scwg_renge_jx)
        # 外格解释
        q_m_scwg_waige_jx = re.search(r'外格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("外格解释 %s" % q_m_scwg_waige_jx)
        # 总格解释

        # 姓名的姓的五格
        # soup_wuge_jx = BeautifulSoup(q_m_mz_xq_response, 'html')
        # name_detail_title = soup_wuge_jx.find('span', class_="f_l text text02")
        # print('名字的五格detail_title %s ' % name_detail_title)

        q_m_scwg_zongge_jx = re.search(r'总格\d+.*h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("总格解释 %s" % q_m_scwg_zongge_jx)
        # 三才解析
        q_m_scwg_scwg_jx = re.search(r'三才解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("三才解析 %s" % q_m_scwg_scwg_jx)
        # 基础运解析
        q_m_scwg_jcy_jx = re.search(r'基础运解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("基础运解析 %s" % q_m_scwg_jcy_jx)
        # 成功运解析
        q_m_scwg_cgy_jx = re.search(r'成功运解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        print("成功运解析 %s" % q_m_scwg_cgy_jx)
        # 人际关系解析
        q_m_scwg_rjgx_jx = re.search(r'人际关系解析.*\s(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("人际关系解析 %s" % q_m_scwg_rjgx_jx)
        # 性格影响解析
        q_m_scwg_xg_jx = re.search(r'性格影响解析.*_h170">(.*)</div>', str(q_m_mz_xq_response), re.M).group(1)
        # print("性格影响解析 %s" % q_m_scwg_xg_jx)

        # 周易八卦正则

        # 名字卦象解析
        q_m_gx_jx = re.search(r'名字卦象解析</div>(\s.*)专家解卦</div>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gx_jx_qx = re.sub(
            r'[(<div class="f_s16 line_h170">)(<div style="border-top: 1px dashed #efefef;height: 0;" class="m_t20"><div>)(\r)(\n)(<p>)(<p class="pb5">)( <div class="f_s16 f_w700 p_t20 p_b10">)(-)( )]',
            '', str(q_m_gx_jx))
        q_m_gx_jx_qp = q_m_gx_jx_qx.split("/")
        q_m_gx_jx_qp_2 = q_m_gx_jx_qp[0:-3]
        # print("名字卦象解析q_m_gx_jx_qp_2: %s" % q_m_gx_jx_qp_2)

        # #解卦
        q_m_zybg_jg = re.search(r'专家解卦</div>(\s.*)<div class="f_s16 f_w700">卦象运势解析', str(q_m_mz_xq_response),
                                re.S).group(1)
        # print("专家解卦：%s" % q_m_zybg_jg)
        q_m_zybg_jg_qx = re.sub(r'[(\[a-z\])(<)(>)( )(=)(")(;)(\d)(_)(:)(-)(#)(\n)(\r)]', '', str(q_m_zybg_jg))
        # print("专家解卦2：%s" % q_m_zybg_jg_qx)
        q_m_zybg_jg_qx2 = q_m_zybg_jg_qx.split("/")[0:-2]
        del q_m_zybg_jg_qx2[1]
        # print("专家解卦3q_m_zybg_jg_qx2：%s" % q_m_zybg_jg_qx2)

        # 卦象运势解析
        q_m_gxys_jx_dx = re.search(r'大象：</dt>\s.*p_b10">(.*)总论：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_dx_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_dx))
        # print("大象 %s" % q_m_gxys_dx_qx)
        q_m_gxys_jx_zl = re.search(r'总论：</dt>\s.*p_b10">(.*)建议：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_zl_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_zl))
        # print("总论 %s" % q_m_gxys_zl_qx)
        q_m_gxys_jx_jy = re.search(r'建议：</dt>\s.*p_b10">(.*)事业：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_jy_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_jy))
        print("建议 %s" % q_m_gxys_jy_qx)
        q_m_gxys_jx_sy = re.search(r'事业：</dt>\s.*p_b10">(.*)经商：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_sy_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_sy))
        # print("事业 %s" % q_m_gxys_sy_qx)
        q_m_gxys_jx_js = re.search(r'经商：</dt>\s.*p_b10">(.*)求名：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_js_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_js))
        # print("经商 %s" % q_m_gxys_js_qx)
        q_m_gxys_jx_qm = re.search(r'求名：</dt>\s.*p_b10">(.*)婚恋：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_qm_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)]', '', str(q_m_gxys_jx_qm))
        # print("求名 %s" % q_m_gxys_qm_qx)
        q_m_gxys_jx_hl = re.search(r'婚恋：</dt>\s.*p_b10">(.*)没有下一条', str(q_m_mz_xq_response), re.S).group(1)
        q_m_gxys_hl_qx = re.sub(r'[(\[a-z\])(\/_"\r\n)( )(=)(\d)(<>)(:C;)]', '', str(q_m_gxys_jx_hl))
        # print("婚恋 %s" % q_m_gxys_hl_qx)

        # 音形义详解
        # 名字拆分
        q_m_yxy_ming = re.compile(r'<em class="zis">(.)</em>').findall(q_m_mz_xq_response)
        # print("名字拆分 %s" % q_m_yxy_ming)

        # 字义解释
        q_m_yxy_zyjs = re.search(r'字义解释：</dt>(\s.*?\s.*)用字解释：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        # 字义解释一
        q_m_yxy_zyjs1 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_zyjs)[0]
        # print("字义解释1则： %s" % q_m_yxy_zyjs1)
        # 字义解释二
        q_m_yxy_zyjs2 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_zyjs)[-1]
        # print("字义解释2则： %s" % q_m_yxy_zyjs2)

        # 用字解释
        q_m_yxy_yzjs = re.search(r'用字解释：</dt>(.*)来源解释：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_yxy_yzjs1 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_yzjs)[0]
        q_m_yxy_yzjs1_qx = re.sub(r'[(<> =_"\/)(\[a-z\])()()()]', '', str(q_m_yxy_yzjs1))
        # print("用字解释1最终版q_m_yxy_yzjs1_qx： %s" % q_m_yxy_yzjs1_qx)
        q_m_yxy_yzjs2_qx = re.search(r'用字解释：</dt>(\s.*\s.*)', str(q_m_yxy_yzjs), re.S).group(1)
        q_m_yxy_yzjs22_qx = re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)]', '', str(q_m_yxy_yzjs2_qx))
        # print("用字解释2最终版q_m_yxy_yzjs22_qx： %s" % q_m_yxy_yzjs22_qx)

        # 来源解释已经有了，不需要在单独提取

        # 字义分析
        q_m_yxy_zyfx = re.search(r'字义分析：</dt>(.*)音律分析：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_yxy_zyfx_qx1 = re.compile(r'<p>(.*)</p>').findall(q_m_yxy_zyfx)
        # print("字义分析列表： %s" % q_m_yxy_zyfx_qx1)

        # 音律分析
        q_m_yxy_ylfx = re.search(r'音律分析：</dt>(.*)字型分析：</dt>', str(q_m_mz_xq_response), re.S).group(1)
        # print("音律分析： %s" % q_m_yxy_ylfx)
        q_m_yxy_ylfx_qx = re.search(r'p_b10">(.*)</dd>', str(q_m_yxy_ylfx), re.S).group(1)
        # print("音律分析最终版： %s" % q_m_yxy_ylfx_qx)

        # 字型分析
        q_m_yxy_zxfx = re.search(r'字型分析：</dt>(.*)大师点评</div>', str(q_m_mz_xq_response), re.S).group(1)
        q_m_yxy_zxfx_lt = re.compile(r'<p>(.*)</p>', re.S).findall(q_m_yxy_zxfx)
        q_m_yxy_zxfx_lt2 = re.sub(r'[(\r\n<>p  \\)(\[\])(\')(rn)( )(\[a-z\])(\d+)(;)(")(_=)]', '',
                                  str(q_m_yxy_zxfx_lt)).split("/")
        # print("字型分析列表2： %s" % q_m_yxy_zxfx_lt2)

        # 大师点评
        q_m_yxy_dsdp = re.search(r'大师点评</div>(.*)下一条，八字五行分析', str(q_m_mz_xq_response), re.S).group(1)
        # print("大师点评： %s" % q_m_yxy_dsdp)
        q_m_yxy_dsdp_qx = re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)(:I;)]', '', str(q_m_yxy_dsdp))
        # print("总结点评数据清洗： %s" % q_m_yxy_dsdp_qx)

        neirog = {
            'q_m_pingying': q_m_pingying,  # 名字的拼音
            'q_m_hanyi_1_1': q_m_hanyi_1_1,  # 第一个字的含义
            'q_m_hanyi_2_2': q_m_hanyi_2_2,  # 第二个字的含义
            'q_m_zh_df': q_m_zh_df,  # 综合打分
            'q_m_qt_df_qx_lt': q_m_qt_df_qx_lt,  # 其他打分项目
            'q_m_yjjd_qx_3': q_m_yjjd_qx_3,  # 引经据典:
            'q_m_bzky_qx': q_m_bzky_qx,  # 八字开运清洗后数据
            'q_m_dsdp': q_m_dsdp,  # 大师点评
            'li_lt_mz_noxing_1': li_lt_mz_noxing_1,  # 不带姓的名字
            'q_m_sxxg_qp': q_m_sxxg_qp,  # 生肖性格优点
            'q_m_sxxg_qd_qp_2': q_m_sxxg_qd_qp_2,  # 生肖性格缺点
            'q_m_sxxg_jies': q_m_sxxg_jies,  # 生肖评分解释
            'q_m_sm_xz': q_m_sm_xz,  # 什么星座
            'q_m_sm_xz_yd_qx_qp': q_m_sm_xz_yd_qx_qp,  # 星座性格优势
            'q_m_sm_xz_qd_qp': q_m_sm_xz_qd_qp,  # 星座缺点
            'q_m_xz_pfjs_pf': q_m_xz_pfjs_pf,  # 星座评分解释
            'q_m_scwg_qb': q_m_scwg_qb,  # 名字的第一姓和第一个名的格数
            'q_m_scwg_ming_2_qx': q_m_scwg_ming_2_qx,  # 最后一个名的格
            "q_m_scwg_tiange": q_m_scwg_tiange,  # 天格
            'q_m_scwg_dige': q_m_scwg_dige,  # 地格
            'q_m_scwg_renge': q_m_scwg_renge,  # 人格
            'q_m_scwg_waige': q_m_scwg_waige,  # 外格
            'q_m_scwg_zongge': q_m_scwg_zongge,  # 总格
            'q_m_scwg_tiange_jx': q_m_scwg_tiange_jx,  # 天格解释
            'q_m_scwg_dige_jx': q_m_scwg_dige_jx,  # 地格解释
            'q_m_scwg_renge_jx': q_m_scwg_renge_jx,  # 人格解释
            'q_m_scwg_waige_jx': q_m_scwg_waige_jx,  # 外格解释
            'q_m_scwg_zongge_jx': q_m_scwg_zongge_jx,  # 总格解释
            'q_m_scwg_scwg_jx': q_m_scwg_scwg_jx,  # 三才解析
            'q_m_scwg_jcy_jx': q_m_scwg_jcy_jx,  # 基础运解析
            'q_m_scwg_cgy_jx': q_m_scwg_cgy_jx,  # 成功运解析
            'q_m_scwg_rjgx_jx': q_m_scwg_rjgx_jx,  # 人际关系解析
            'q_m_scwg_xg_jx': q_m_scwg_xg_jx,  # 性格影响解析
            'q_m_gx_jx_qp_2': q_m_gx_jx_qp_2,  # 名字卦象解析
            'q_m_zybg_jg_qx2': q_m_zybg_jg_qx2,  # 专家解卦
            'q_m_gxys_dx_qx': q_m_gxys_dx_qx,  # 大象
            'q_m_gxys_zl_qx': q_m_gxys_zl_qx,  # 总论
            'q_m_gxys_jy_qx': q_m_gxys_jy_qx,  # 建议
            'q_m_gxys_sy_qx': q_m_gxys_sy_qx,  # 事业
            'q_m_gxys_js_qx': q_m_gxys_js_qx,  # 经商
            'q_m_gxys_qm_qx': q_m_gxys_qm_qx,  # 求名
            'q_m_gxys_hl_qx': q_m_gxys_hl_qx,  # 婚恋
            'q_m_yxy_yzjs1_qx': q_m_yxy_yzjs1_qx,  # 用字解释1最终版
            'q_m_yxy_yzjs22_qx': q_m_yxy_yzjs22_qx,  # 用字解释2最终版
            'q_m_yxy_zyfx_qx1': q_m_yxy_zyfx_qx1,  # 字义分析列表
            'q_m_yxy_ylfx': q_m_yxy_ylfx,  # q_m_yxy_ylfx_qx
            'q_m_yxy_zxfx_lt2': q_m_yxy_zxfx_lt2,  # 字型分析列表
            'q_m_yxy_dsdp_qx': q_m_yxy_dsdp_qx,  # 总结
            'mz_yx_lt_qx_qp': mz_yx_lt_qx_qp  # 这个是名字的印象
        }
        return neirog
    else:
        return redirect(url_for('helloWorld'))


@app.route('/pay/', methods=["GET", "POST"])
def pay():
    # order_id = str(int(time.time() * 1000)) + str(int(time.clock() * 1000000))
    if request.method == 'POST':
        order_id = request.form.get("order_id")
        # print("这个用户的手机号码也就是订单id %s" % order_id)
        price_order = '9.70'
        # print("这个是前端提交的价格类型 %s" % type(price_order))

        type_order = int(request.form.get("pay_type"))
        # print("这个是前端提交的支付类型 %s" % type_order)
        # print("这个是前端提交的支付类型类型 %s" % type(type_order))
        # 用与给ajax一个返回值，保障有回调，就请求成功了
        global zidian2
        zidian2 = {
            "price": price_order,
            "type": type_order,
            "order_id": order_id,
        }
        api_user = "8fc5501b"
        api_key = "8c60de4c-769c-40cf-98a7-8c2b41581f9a"
        redirect = "http://www.qmg365.com/order_cx/"
        order_info = "12313213"
        param = {
            'api_user': api_user,
            'price': price_order,
            'type': type_order,
            'redirect': redirect,
            'order_id': order_id,
            'order_info': order_info,
        }

        param_keys = list(param.keys())
        param_keys.sort()

        param_str = "8c60de4c-769c-40cf-98a7-8c2b41581f9a"

        for key in param_keys:
            if isinstance(param[key], str):
                param_str += param[key]
            else:
                param_str += str(param[key])

        signature = hashlib.md5(param_str.encode('utf8')).hexdigest()

        p = {
            'api_user': api_user,
            'order_id': order_id,
            'order_info': order_info,
            'type': type_order,
            'price': price_order,
            'redirect': redirect,
            'signature': signature,
        }
        # 对p这个字典进行转码
        p_zhuan = urllib.parse.urlencode(p)
        # 构建请求头
        # pay_headers = {
        #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
        # }

        global pay_url

        pay_url = "https://www.paypayzhu.com/#/pay?"
        # 构建请求对象
        # pay_request = urllib.request.Request(url=pay_url, headers=pay_headers)

        # 发送请求，获取响应
        # pay_response = urllib.request.urlopen(pay_request,data=p_zhuan)

        # print(pay_response)

        pay_url = pay_url + p_zhuan + "&user_id=3146&device_name&bank_mark"
        # print(pay_url)
        # webbrowser.open(pay_url,new=1,autoraise=True)
        return json.dumps(pay_url)

    else:
        webbrowser.open(pay_url, new=1, autoraise=True)


@app.route('/vip_hd/', methods=['GET', 'POST'])
def vip_hd():
    global order_id_hd
    if request.method == 'POST':
        order_id_hd = request.form.get('order_id')
        session['vip_tele'] = order_id_hd
        session.permanent = True
        # print("这个是回调回来的订单号postpost %s" % order_id_hd)
        user = User(telephone=order_id_hd, )
        db.session.add(user)
        db.session.commit()
        asdsakkk = session.get('vip_tele')
        # print("检查一下是否写入了session %s" % asdsakkk)
        return redirect(url_for('helloWorld'))
    else:

        session['vip_tele'] = order_id_hd
        #   # vip_tele_zzz = session.get('vip_tele')
        # print("这个是回调回getgetgetget来的订单号yyyy %s" % order_id_hd)

        return redirect(url_for('order_cx'))
    # pass


@app.route('/zxcqweabc/', methods=['GET', 'POST'])
def zxcqweabc():
    if request.method == 'GET':
        vip_tele = session.get('vip_tele')
        # print("检查一下是否写入了session %s" % vip_tele)
        return redirect(url_for('vip_hd'))
    else:
        pass


# if telephone_vip == '':
# 	return redirect(url_for('order_cx'))
# else:
# 	print('这格式需要写入seesion的订单id %s' %order_id)
# 	session['vip_tele'] = order_id
# 	return redirect(url_for('helloWorld'))


@app.route('/order_cx/', methods=['GET', 'POST'])
def order_cx():
    if request.method == 'POST':
        telephone = request.form.get('vip_nub')
        # print("获取到的vip电话kkk %s" % telephone)
        vip_tele2 = User.query.filter(User.telephone == telephone).first()
        if vip_tele2:
            session['vip_tele'] = vip_tele2.telephone
            session.permanent = True
            return redirect(url_for('helloWorld'))
        else:
            reg_b = re.compile(
                r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
                re.I | re.M)
            use_agent = request.headers.get('User-Agent')
            # print(type(use_agent))
            # print("这个是UA %s" % use_agent)
            basda = reg_b.search(use_agent)
            no_vip = 'block'
            if basda:
                return render_template("m_order_cx.html", no_vip=no_vip)
            else:
                return render_template("order_cx.html", no_vip=no_vip)

    else:
        reg_b = re.compile(
            r"(android|bb\\d+|meego).+mobile|avantgo|bada\\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge|maemo|midp|mmp|mobile.+firefox|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\\.(browser|link)|vodafone|wap|windows ce|xda|xiino",
            re.I | re.M)
        use_agent = request.headers.get('User-Agent')
        # print(type(use_agent))
        # print("这个是UA %s" % use_agent)
        basda = reg_b.search(use_agent)
        if basda:
            return render_template("m_order_cx.html")
        else:
            return render_template("order_cx.html")


@app.context_processor
def my_context_processor():
    global vip_tele
    vip_tele = session.get('vip_tele')
    if vip_tele:
        vip_tele1 = User.query.filter(User.telephone == vip_tele).first()
        if vip_tele1:
            return {'vip_tele': vip_tele1}
    else:
        return {}


@app.route('/pao_author/')
def pao_author():
    author = Author.query.all()
    article_len = len(Article.query.all()) + 1
    for i in range(1, article_len):
        suijishu = random.randint(1, 300)
        name = author[suijishu].author_name
        article = Article.query.filter(Article.id == i).first()
        article.author_name = name
        db.session.commit()
    return '写入成功'


@app.route('/pao_yuedu/')
def pao_des():
    article_len = len(Article.query.all()) + 1
    for i in range(1, article_len):
        suijishu = random.randint(500, 3000)
        article = Article.query.filter(Article.id == i).first()
        article.article_yuedu = str(suijishu)
        db.session.commit()
    return '描述写入完成'

@app.route('/pao_fabutime/')
def pao_fabutime():
    article_len = len(Article.query.all()) + 1
    for i in range(1, article_len):
        moth = random.randint(7, 9)
        dayday = random.randint(1, 30)
        hourhour = random.randint(00, 24)
        minuteminute = random.randint(00, 60)

        riqi = '2020-'+str(moth)+'-'+str(dayday)+' '+str(hourhour)+':'+str(minuteminute)
        print('生成的日期是',riqi)
        article = Article.query.filter(Article.id == i).first()
        article.article_time = str(riqi)
        db.session.commit()
    return '描述写入完成'


@app.route('/dqtime/')
def dqtime():
    for i in range(1, 100):
        moth = random.randint(7, 9)
        dayday = random.randint(1, 30)
        hourhour = random.randint(00, 24)
        minuteminute = random.randint(00, 60)

        riqi = '2020-'+str(moth)+'-'+str(dayday)+' '+str(hourhour)+':'+str(minuteminute)
        print('生成的日期是',riqi)
        article = Article.query.filter(Article.id == i).first()
        article.article_time = str(riqi)
        db.session.commit()
    return '描述写入完成'


if __name__ == "__main__":
    app.run()
