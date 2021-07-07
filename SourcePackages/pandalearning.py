import os
import sys
import time
from pdlearn import version
from pdlearn import user

from pdlearn import threads
from pdlearn.config          import cfg
from pdlearn.mydriver        import Mydriver
from pdlearn.score           import show_score

from datetime import datetime
from datetime import date

from utils import keep_alive, get_argv, update_cookies
from daliyroutine import daliy_routine


if __name__ == '__main__':
    #  0 读取版本信息
    start_time = time.time()
    if(cfg['display']['banner'] != "false"): # banner文本直接硬编码，不要放在ini中
        print("=" * 60 + \
        '\n    科技强国官方网站：https://techxuexi.js.org' + \
        '\n    Github地址：https://github.com/TechXueXi' + \
        '\n使用本项目，必须接受以下内容，否则请立即退出：' + \
        '\n    - TechXueXi 仅额外提供给“爱党爱国”且“工作学业繁重”的人' + \
        '\n    - 项目开源协议 LGPL-3.0' + \
        '\n    - 不得利用本项目盈利' + \
        '\n另外，我们建议你参与一个维护劳动法的项目：' + \
        '\nhttps://996.icu/ 或 https://github.com/996icu/996.ICU/blob/master/README_CN.md')
    cookies = user.check_default_user_cookie()
    user.list_user()
    # user.select_user()
    print("=" * 60, '''\nTechXueXi 现支持以下模式（答题时请值守电脑旁处理少部分不正常的题目）：''')
    print(cfg['base']['ModeText'] + '\n' + "=" * 60) # 模式提示文字请在 ./config/main.ini 处修改。
    # always 2 to get possible most scores
    TechXueXi_mode = "2"

    info_shread = threads.MyThread("获取更新信息...", version.up_info)
    info_shread.start()
    #  1 创建用户标记，区分多个用户历史纪录
    #uid = user.get_default_userId()

    print("未找到有效登录信息，需要登录")
    driver_login = Mydriver(nohead=False)
    cookies = driver_login.login()
    # driver_login.quit()
    user.save_cookies(cookies)
    uid = user.get_userId(cookies)
    user_fullname = user.get_fullname(uid)
    user.update_last_user(uid)

    article_index = user.get_article_index(uid)
    video_index = user.get_video_index(uid)
    
    total, scores = show_score(cookies)
    nohead, lock, stime = get_argv()
    cur_time = datetime.now()

    while True:
        # execute once immediately
        if abs((datetime.now() - cur_time).seconds)<500:
            daliy_routine(cookies, scores, TechXueXi_mode, uid, article_index, video_index)
        elif abs((datetime.now() - datetime.strptime(str(date.today()) + ' ' + "18:05:00",'%Y-%m-%d %H:%M:%S')).seconds)<600:
                # update cookies
                cookies,uid,article_index,video_index,total, scores = update_cookies(driver_login)
                daliy_routine(cookies, scores, TechXueXi_mode, uid, article_index, video_index)

        elif abs((datetime.now() - datetime.strptime(str(date.today()) + ' ' + "06:05:00",'%Y-%m-%d %H:%M:%S')).seconds)<600:
                # update cookies
                cookies,uid,article_index,video_index,total, scores = update_cookies(driver_login)
                daliy_routine(cookies, scores, TechXueXi_mode, uid, article_index, video_index)
        else:
            keep_alive(driver_login)



