import time

from pdlearn import version
from pdlearn import user
from pdlearn import threads
from datetime import datetime
from datetime import date

from SourcePackages.continouspd.utils import user_flag, keep_alive
from SourcePackages.continouspd.daliyroutine import daliy_routine


if __name__ == '__main__':
    #  0 读取版本信息

    print("=" * 120,'''
    科技强国官方网站：https://techxuexi.js.org
    Github地址：https://github.com/TechXueXi
使用本项目，必须接受以下内容，否则请立即退出：
    - TechXueXi 仅额外提供给“热爱党国”且“工作学业繁重”的人
    - 项目开源协议 LGPL-3.0
    - 不得利用本项目盈利
另外，我们建议你参与一个维护劳动法的项目：
https://996.icu/ 或 https://github.com/996icu/996.ICU/blob/master/README_CN.md
TechXueXi 现支持以下模式（答题时请值守电脑旁处理少部分不正常的题目）：
    1 文章+视频
    2 每日答题+每周答题+专项答题+文章+视频
      （可以根据当日已得做题积分，及是否有可得分套题，决定是否做题）
    3 每日答题+文章+视频
      （可以根据当日已得做题积分，决定是否做题）
''',"=" * 120)
    # TechXueXi_mode = input("请选择模式（输入对应数字）并回车： ")
    # always 2 to get possible most scores
    TechXueXi_mode = "2"

    info_shread = threads.MyThread("获取更新信息...", version.up_info)
    info_shread.start()
    #  1 创建用户标记，区分多个用户历史纪录
    dd_status, uname = user.get_user()
    cookies, a_log, v_log, d_log, driver_login = user_flag(uname)
    # login finished here
    cur_time = datetime.now()

    while True:
        # do daily routine everyday on 6 am
        if abs((datetime.now() - cur_time).seconds)<600:
            daliy_routine(cookies, a_log, v_log, d_log, TechXueXi_mode, uname)
        elif abs((datetime.now() - datetime.strptime(str(date.today()) + ' ' + "17:05:00",'%Y-%m-%d %H:%M:%S')).seconds)<600:
                # update cookies
                cookies = driver_login.get_cookies()
                a_log = user.get_a_log(uname)
                v_log = user.get_v_log(uname)
                d_log = user.get_d_log(uname)
                daliy_routine(cookies, a_log, v_log, d_log, TechXueXi_mode, uname)
        else:
            keep_alive(driver_login)


