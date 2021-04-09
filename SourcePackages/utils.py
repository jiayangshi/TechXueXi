import random
import time
import requests
import json
from time import sleep
from sys import argv
from pdlearn.const import const
from pdlearn import user
from requests.cookies import RequestsCookieJar


def get_argv():
    nohead = True
    lock = False
    stime = False
    if len(argv) > 2:
        if argv[2] == "hidden":
            nohead = True
        elif argv[2] == "show":
            nohead = False
    if len(argv) > 3:
        if argv[3] == "single":
            lock = True
        elif argv[3] == "multithread":
            lock = False
    if len(argv) > 4:
        if argv[4].isdigit():
            stime = argv[4]
    return nohead, lock, stime


def get_score(cookies):
    try:
        jar = RequestsCookieJar()
        for cookie in cookies:
            jar.set(cookie['name'], cookie['value'])
        total_json = requests.get("https://pc-api.xuexi.cn/open/api/score/get", cookies=jar,
                                  headers={'Cache-Control': 'no-cache'}).content.decode("utf8")
        total = int(json.loads(total_json)["data"]["score"])
        userId = json.loads(total_json)["data"]["userId"]
        score_json = requests.get("https://pc-api.xuexi.cn/open/api/score/today/queryrate", cookies=jar,
                                  headers={'Cache-Control': 'no-cache'}).content.decode("utf8")
        today_json = requests.get("https://pc-api.xuexi.cn/open/api/score/today/query", cookies=jar,
                                  headers={'Cache-Control': 'no-cache'}).content.decode("utf8")
        today = 0
        today = int(json.loads(today_json)["data"]["score"])
        dayScoreDtos = json.loads(score_json)["data"]["dayScoreDtos"]
        rule_list = [1, 2, 9, 1002, 1003, 6, 5, 4]
        score_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 长度为十
        for i in dayScoreDtos:
            for j in range(len(rule_list)):
                if i["ruleId"] == rule_list[j]:
                    score_list[j] = int(i["currentScore"])
        # 阅读文章，视听学习，登录，文章时长，视听学习时长，每日答题，每周答题，专项答题
        scores = {}
        scores["article_num"] = score_list[0]  # 0阅读文章
        scores["video_num"] = score_list[1]  # 1视听学习
        scores["login"] = score_list[2]  # 7登录
        scores["article_time"] = score_list[3]  # 6文章时长
        scores["video_time"] = score_list[4]  # 5视听学习时长
        scores["daily"] = score_list[5]  # 2每日答题
        scores["weekly"] = score_list[6]  # 3每周答题
        scores["zhuanxiang"] = score_list[7]  # 4专项答题

        scores["today"] = today  # 8今日得分
        return userId, total, scores
    except:
        print("=" * 60)
        print("get_score 获取失败")
        print("=" * 60)
        raise

def show_score(cookies):
    userId, total, scores = get_score(cookies)
    print("当前学习总积分：" + str(total) + "\t" + "今日得分：" + str(scores["today"]))
    print("阅读文章:", scores["article_num"], "/", const.article_num_all, ",",
        "观看视频:", scores["video_num"], "/", const.video_num_all, ",",
        "文章时长:", scores["article_time"], "/", const.article_time_all, ",",
        "视频时长:", scores["video_time"], "/", const.video_time_all, ",",
        "\n每日登陆:", scores["login"], "/", const.login_all, ",",
        "每日答题:", scores["daily"], "/", const.daily_all, ",",
        "每周答题:", scores["weekly"], "/", const.weekly_all, ",",
        "专项答题:", scores["zhuanxiang"], "/", const.zhuanxiang_all)
    return total, scores

def check_delay():
    delay_time = random.randint(2, 5)
    print('等待 ', delay_time, ' 秒')
    time.sleep(delay_time)

def keep_alive(driver_login):
    driver_alive = driver_login
    #driver_alive.set_cookies(cookies)
    driver_alive.get_url('https://pc.xuexi.cn/points/my-points.html')
    print("每5分钟刷新一次界面，防止登录超时...")
    sleep(300)


def update_cookies(driver_login):
    cookies = driver_login.get_cookies()
    uid = user.get_userId(cookies)

    article_index = user.get_article_index(uid)
    video_index = user.get_video_index(uid)

    total, scores = show_score(cookies)

    return cookies,uid,article_index,video_index,total, scores
