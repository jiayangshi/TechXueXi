import time
from SourcePackages.continouspd.utils import show_score, get_argv
from SourcePackages.continouspd.question import daily, weekly, zhuanxiang
from SourcePackages.continouspd.articlevideos import article, video
from SourcePackages.pdlearn import threads


def daliy_routine(cookies, a_log, v_log, d_log, TechXueXi_mode, uname):
    start_time = time.time()
    total, each = show_score(cookies)
    nohead, lock, stime = get_argv()

    if TechXueXi_mode in ["2", "3"]:
        print('开始每日答题……')
        daily(cookies, d_log, each, uname)
    if TechXueXi_mode in ["2"]:
        print('开始每周答题……')
        weekly(cookies, d_log, each, uname)
        print('开始专项答题……')
        zhuanxiang(cookies, d_log, each, uname)

    article_thread = threads.MyThread("文章学习", article, cookies, a_log, each, nohead, uname, lock=lock)
    video_thread = threads.MyThread("视频学习", video, cookies, v_log, each, nohead, uname, lock=lock)
    article_thread.start()
    video_thread.start()
    article_thread.join()
    video_thread.join()
    print("总计用时" + str(int(time.time() - start_time) / 60) + "分钟")