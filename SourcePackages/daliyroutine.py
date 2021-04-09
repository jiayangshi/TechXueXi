import time
from utils import get_argv
from pdlearn.score import show_score
from pdlearn.answer_question import daily, weekly, zhuanxiang
from pdlearn.article_video import article, video
from pdlearn import threads
import math


def daliy_routine(cookies, scores, TechXueXi_mode, uid, article_index, video_index):
    start_time = time.time()
    total, each = show_score(cookies)
    nohead, lock, stime = get_argv()

    if TechXueXi_mode in ["2", "3"]:
        print('开始每日答题……')
        daily(cookies, scores)
    if TechXueXi_mode in ["2"]:
        print('开始每周答题……')
        weekly(cookies, scores)
        print('开始专项答题……')
        zhuanxiang(cookies, scores)

    # from upstream
    article_thread = threads.MyThread("文章学习", article, uid, cookies, article_index, scores, lock=lock)
    video_thread = threads.MyThread("视频学习", video, uid, cookies, video_index, scores, lock=lock)
    article_thread.start()
    video_thread.start()
    article_thread.join()
    video_thread.join()

    seconds_used = int(time.time() - start_time)
    print("总计用时 " + str(math.floor(seconds_used / 60)) + " 分 " + str(seconds_used % 60) + " 秒")
