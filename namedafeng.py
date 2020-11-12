# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for, session, make_response
from flask_script import Manager
import re
import urllib
import ast
from fake_useragent import UserAgent
import requests
from lxml import etree
import http.cookiejar
import random
import config
from models import *
from exts import db
import datetime


def namedafen():
    mizi_ku_nm = request.args.get('name')
    xingbie_js = request.args.get('xb')
    birthtime = request.args.get('birthtime')
    birthplace = request.args.get('birthplace')

    print('这是提交的数据1107 ', mizi_ku_nm, birthtime, xingbie_js, birthplace)

    xing = mizi_ku_nm[0]
    print('提交的姓',xing)

    ming = mizi_ku_nm[1:]
    print('提交的名', ming)

    dingzhi_2 = ''  #定字为空

    biaodan_xz = '9'

    ba_mp_sex = xingbie_js

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

    ymd_ymd = str(birthtime.split(' ')[0])
    h_h = str((birthtime.split(' ')[1]).split(':')[0])
    i_i = str((birthtime.split(' ')[1]).split(':')[1])
    ba_mp_year = str((birthtime.split(' ')[0]).split("-")[0])
    ba_mp_month = str((birthtime.split(' ')[0]).split("-")[1])
    ba_mp_day = str((birthtime.split(' ')[0]).split("-")[2])


    #打分路径格式
    dafenpath='&xing='+urllib.parse.quote(xing)+'&ming='+urllib.parse.quote(ming)+'&xb='+urllib.parse.quote(xingbie_js)+'&ymd='+urllib.parse.quote(ymd_ymd)+'&h='+h_h+'&i='+i_i



    wanzheng_dafenpath = 'https://www.mzi8.com/ceshi/c.php?sign=cha'+dafenpath
    print('这个打分路径是1110',wanzheng_dafenpath)

    uazxcvb_bt_yu = UserAgent().random
    ua_datial_title = {
        'User-Agent': uazxcvb_bt_yu,
        'Connection': 'keep-alive',
    }

    dafen_response=requests.get(wanzheng_dafenpath,headers=ua_datial_title).text

    mz_yx_lt_qx_qp = etree.HTML(dafen_response).xpath("//a[@class='yy']/text()")
    print('这个是获取到的印象',mz_yx_lt_qx_qp)


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
        m_z_ku_gz = "<div class='" + q_m_ze_cl + "'>.*?<b .*?>(.*?)</b>.*?</div>"
        pattern = re.compile(m_z_ku_gz, re.S)
        lt_lt_mz = pattern.findall(response)[0:10]

        print('生成的名字库1107',lt_lt_mz)

        mz_yx = re.compile(r"class='item'><span class='yy'>.*?<div class='item am-margin-top-xs", re.S)
        mz_yx_lt = mz_yx.findall(response)[0:10]
        mz_yx_lt_qx = re.sub(r"[(\[a-z\])(\-)(=)(')( )(<span>)]", '', str(mz_yx_lt))

        print('名字测试打分获取到的印象',mz_yx_lt_qx)
        print('名字测试打分获取到的印象', len(mz_yx_lt_qx))

        vip_regex = xing + "(.)"
        print('vip_regex是个什么鬼', vip_regex)

        vip_mzku_noxing = re.sub(vip_regex, '*', str(lt_lt_mz))
        print("将名字中间一个字替换成*: %s" % vip_mzku_noxing)
        # print(type(vip_mzku_noxing))

        vip1_mzku_noxing = ast.literal_eval(vip_mzku_noxing)
        print("将带*的名转化为列表:", vip1_mzku_noxing)

        # print(type(mi_ku_sy))

        # 将生成的名字库去掉前面的姓
        li_lt_mz_noxing = re.sub(xing, "", str(lt_lt_mz))
        global neirog
        session['name_ku'] = lt_lt_mz
        session.permanent = True

        #写入名字印象到cookei中
        session['mz_yx_lt_qx'] = mz_yx_lt_qx
        session.permanent = True

        jieshi = ''
        if len(ming) == 1:
            jieshi = 'jieshi_display'
        else:
            jieshi = ''
        neirog = {
            'jieshi':jieshi,
            'mizi_ku_nm': mizi_ku_nm,
            'xing': xing,
            'xingbie': ba_mp_sex,
            "xingbie_zhon": ba_mp_sex_zhon,
            'dingzhi': '',
            'biaodan_xz': biaodan_xz,
            'qiwang': '',
            'birthtime': birthtime,
            'birthplace': birthplace,
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
            "li_lt_mz_noxing_1": ming,
            "q_m_pingying": q_m_pingying,
            "q_m_hanyi_1_1": q_m_hanyi_1_1,
            "q_m_hanyi_2_2": q_m_hanyi_2_2,
            "q_m_zh_df": q_m_zh_df,
            "q_m_qt_df_qx_lt": q_m_qt_df_qx_lt,
            "q_m_yjjd_qx_3": q_m_yjjd_qx_3,
            "q_m_bzky_qx": q_m_bzky_qx,
            "q_m_dsdp": q_m_dsdp,
            "mz_yx_lt_qx_qp": mz_yx_lt_qx_qp,  # 名字印象
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
            "qiwang_dt_nb_new": '',
            "qiwang_dt_lb_1": '',
            "qiwang_dt_lb_int": '',
            'pingjian_shijian': pingjian_shijian,  # 这个是生成的评价时间
            'pingjia_content_ls': pingjia_fenzhu,  # 评价内容分组
            'pingjia_fenzhu_one_len': pingjia_fenzhu_one_len,
            'pingjia_fenzhu_two_len': pingjia_fenzhu_two_len,
            'pingjia_fenzhu_three_len': pingjia_fenzhu_three_len,
            'pingjia_fenzhu_four_len': pingjia_fenzhu_four_len,
            'city_fenzu': city_fenzu,
        }


    ###################
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

    qi_ming_url = "https://qm.qumingdashi.com/newqiming/index/index"
    # 构建起名网请求对象
    q_m_request = urllib.request.Request(url=qi_ming_url, headers=q_m_headers)
    # print("这个是请求的链接 %s" % q_m_request)
    # 获取响应，必须要用open进行操作，因为这里面带着cookie
    q_m_response = q_M_opener.open(q_m_request, data=q_m_formdata_ed)
    # 下面是提交信息成功后的，进入名字详情页的操作
    # 起名网名字详情链接
    q_m_mingzi = "https://qm.qumingdashi.com/newqiming/index/detail?"


    print('1110获取到的姓是',xing)

    print('1110获取到的名是', ming)
    q_m_mz_formdata = {
        'surname': xing,
        'name': ming,
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

    # print('这个是获取的响应对象',q_m_mz_xq_response)
    # 开始正则，对响应的内容进行数据的提取
    # # 首先提取的是拼音
    # q_m_pingying_b = re.search(r'的读音是(.*?)，声调为', str(q_m_mz_xq_response), re.M).group(1)
    # q_m_pingying = re.sub('、', ' ', q_m_pingying_b)

    # q_m_hanyi_2_2 = re.sub('[(<span>)(\[a-z\])(<>_")(\/)( )]', '', str(q_m_hanyi_2))

    q_m_pingying = etree.HTML(dafen_response).xpath("//div/a[@class='py']/text()")[0]
    print('获取到的平阴是',q_m_pingying)

    q_m_pingying= str(q_m_pingying)
    print('这个拼音好似什么烈性的',type(q_m_pingying))

    q_m_pingying = re.sub(r'[(\()(\))]','',q_m_pingying)
    print('首先提取的是拼音姓大大说', q_m_pingying)

    # print('首先提取的是拼音 %s' % q_m_pingying)

    if len(ming) == 2:
    # 接着是字义内涵
        q_m_hanyi_quanbu = re.search(r'class="co_s">(.：.*)</p>', str(q_m_mz_xq_response)).group(1)
        print('起名含义全部',q_m_hanyi_quanbu)
        q_m_hanyi_1 = re.search(r'(.*?)<span class="co_s">', str(q_m_hanyi_quanbu), re.S).group(1)
        # print(type(q_m_hanyi_1))
        # print("第一个名未清洗: %s" % q_m_hanyi_1)
        q_m_hanyi_1_1 = re.sub('</span>', '', str(q_m_hanyi_1))
        # print("第一个名已清洗: %s" % q_m_hanyi_1_1)
        q_m_hanyi_2 = re.search(r'<span class="co_s">(.*)', str(q_m_hanyi_quanbu), re.S).group(1)
        q_m_hanyi_2_2 = re.sub('[(<span>)(\[a-z\])(<>_")(\/)( )]', '', str(q_m_hanyi_2))
        print("第二个名已清洗: %s" % q_m_hanyi_2_2)
    else:
        q_m_hanyi_quanbu = re.search(r'class="co_s">(.：.*)</p>', str(q_m_mz_xq_response)).group(1)
        print('起名含义全部', q_m_hanyi_quanbu)
        q_m_hanyi_1_1 = re.search(r'</span>(.*?)<p>', str(q_m_hanyi_quanbu), re.S).group(1)
        q_m_hanyi_1_2 = re.findall(r'<p>(.*?)</p>', str(q_m_hanyi_quanbu), re.S)
        q_m_hanyi_1_3=''
        for i in q_m_hanyi_1_2:
            q_m_hanyi_1_2 =  re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)]','',str(i))
            print('q_m_hanyi_1_2',q_m_hanyi_1_2)
            q_m_hanyi_1_2 +=q_m_hanyi_1_2+'<br>'
            q_m_hanyi_1_3 += q_m_hanyi_1_2
            print('q_m_hanyi_1_3循环', q_m_hanyi_1_3)

        print('q_m_hanyi_1_3',q_m_hanyi_1_3)


        print('zasdasdkash',q_m_hanyi_1_2)

        # q_m_hanyi_1 = ming+':'+q_m_hanyi_1
        # print('起名含义1', q_m_hanyi_1)
        q_m_hanyi_2_2=''

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

    # print("引经据典sadasd1112q_m_mz_xq_response,,,,,,,", q_m_mz_xq_response)


    q_m_yjjd_qx_1 = re.sub('<span class="co_red">', '', str(q_m_yjjd))
    print("引经据典sadasd1112q_m_yjjd_qx_1,,,,,,,", q_m_yjjd_qx_1)

    q_m_yjjd_qx_2 = re.sub('</span>', '', str(q_m_yjjd_qx_1))

    print("引经据典sadasd1112,,,,,,,", q_m_yjjd_qx_2)
    q_m_yjjd_qx_3 = ast.literal_eval(q_m_yjjd_qx_2)
    print("引经据典sadasd1112" ,q_m_yjjd_qx_3)

    #清除重复的列表元素
    q_m_yjjd_qx_3 = list(set(q_m_yjjd_qx_3))
    print("引经据典sadasd1112", q_m_yjjd_qx_3)

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
    print("全部三才五格q_m_scwg_qb %s" % q_m_scwg_qb)
    # 第二个名
    if len(ming)==2:
        q_m_scwg_ming_2 = re.search(r'<p>(.&nbsp;\d+) </p>', str(q_m_mz_xq_response), re.M).group(1)
        q_m_scwg_ming_2_qx = re.sub(r'&nbsp;', ' ', str(q_m_scwg_ming_2))
    # print('最后一个名的格 %s' % q_m_scwg_ming_2_qx)
    else:
        q_m_scwg_ming_2_qx=''

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
    print('11129dian27',q_m_yxy_yzjs)
    q_m_yxy_yzjs1 = re.compile(r'p_b10">(.*)</dd>').findall(q_m_yxy_yzjs)[0]
    q_m_yxy_yzjs1_qx = re.sub(r'[(<> =_"\/)(\[a-z\])()()()]', '', str(q_m_yxy_yzjs1))
    print("用字解释1最终版q_m_yxy_yzjs1_qx： %s" % q_m_yxy_yzjs1_qx)
    if len(ming)==2:
        q_m_yxy_yzjs2_qx = re.search(r'用字解释：</dt>(\s.*\s.*)', str(q_m_yxy_yzjs), re.S).group(1)
        q_m_yxy_yzjs22_qx = re.sub(r'[(<> =_"\/)(\[a-z\])(\n)(\r)(\d+)]', '', str(q_m_yxy_yzjs2_qx))
        # print("用字解释2最终版q_m_yxy_yzjs22_qx： %s" % q_m_yxy_yzjs22_qx)
    else:
        q_m_yxy_yzjs22_qx = ''
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


    #################

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
        'yy': '',
        'page': 1,
    }

    data_mizi = urllib.parse.urlencode(huoqu_data_mizi)

    path_new = "/qiming/" + q_m_url + ".php?" + data_mizi

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
    print('get_url',get_url)
    # 生成新的url
    get_url += data_mizi
    # 构建请求对象
    print('这个是请求的url1109',get_url)



    # 创建名字打分链接
    get_url_dafen = "https://www.mzi8.com/ceshi/c.php?sign=cha" + q_m_url + ".php?"


    qu_dx = urllib.request.Request(url=get_url, headers=headers)

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

    # 发送请求对象,获取响应内容
    response = urllib.request.urlopen(qu_dx).read().decode()
    # print('名字库的响应内容% s' % response)
    zhengze(response)

    return neirog