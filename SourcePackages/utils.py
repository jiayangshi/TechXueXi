import random
import time
from time import sleep
from sys import argv
from SourcePackages.pdlearn import user
from SourcePackages.pdlearn import mydriver
from SourcePackages.pdlearn import score

def user_flag(uname):
    driver_login = mydriver.Mydriver(nohead=False)
    cookies = driver_login.login()

    a_log = user.get_a_log(uname)
    v_log = user.get_v_log(uname)
    d_log = user.get_d_log(uname)

    return cookies, a_log, v_log, d_log, driver_login


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


def show_score(cookies):
    total, each = score.get_score(cookies)
    print("当前学习总积分：" + str(total))
    print("阅读文章:{}/6,观看视频:{}/6,登陆:{}/1,文章时长:{}/6,视频时长:{}/6,每日答题:{}/5,每周答题:{}/5,专项答题:{}/10".format(*each))
    # print("阅读文章:",each[0],"/6,观看视频:",each[1],"/6,登陆:",each[2],"/1,文章时长:",each[3],"/6,视频时长:",each[4],"/6,每日答题:",each[5],"/6,每周答题:",each[6],"/5,专项答题:",each[7],"/10")
    return total, each

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