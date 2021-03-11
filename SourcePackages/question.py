import time
from pdlearn import mydriver
from utils import show_score
from utils import check_delay
from datetime import datetime

# todo: handle case fails to answer
# todo: possibility1 calculate the running time
# todo: possibility2 update the questions logics
def daily(cookies, d_log, each, uname):
    begin_time = datetime.now()
    if each[5] < 5:
        # driver_daily = mydriver.Mydriver(nohead=nohead)  time.sleep(random.randint(5, 15))
        driver_daily = mydriver.Mydriver(nohead=False)
        # driver_daily.driver.maximize_window()
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        driver_daily.get_url("https://www.xuexi.cn/notFound.html")
        driver_daily.set_cookies(cookies)
        try_count = 0

        if each[5] < 5:
            d_num = 5 - each[5]
            letters = list("ABCDEFGHIJKLMN")
            driver_daily.get_url('https://pc.xuexi.cn/points/my-points.html')
            driver_daily.click_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[5]/div[2]/div[2]/div')
            while each[5] < 5:
                if (datetime.now() - begin_time).seconds>(15*60):
                    print("包含不支持的题目，暂时跳过")
                    break
                try:
                    category = driver_daily.xpath_getText(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[1]')  # get_attribute("name")
                except Exception as e:
                    print('查找元素失败！')
                    break
                print(category)
                tips = driver_daily._view_tips()
                check_delay()
                if not tips:
                    print("本题没有提示")
                    break
                    if "填空题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "多选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "单选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                        # return driver_daily._search(driver_daily.content, driver_daily.options, driver_daily.excludes)
                    else:
                        print("题目类型非法")
                        break
                else:
                    if "填空题" in category:
                        answer = tips
                        driver_daily.fill_in_blank(answer)

                    elif "多选题" in category:
                        options = driver_daily.radio_get_options()
                        radio_in_tips, radio_out_tips = "", ""
                        for letter, option in zip(letters, options):
                            for tip in tips:
                                if tip in option:
                                    # print(f'{option} in tips')
                                    if letter not in radio_in_tips:
                                        radio_in_tips += letter
                        radio_out_tips = [letter for letter, option in zip(letters, options) if
                                          (letter not in radio_in_tips)]

                        print('含 ', radio_in_tips, '不含', radio_out_tips)
                        if len(radio_in_tips) > 1:  # and radio_in_tips not in driver_daily.excludes:
                            print('根据提示', radio_in_tips)
                            driver_daily.radio_check(radio_in_tips)
                        elif len(radio_out_tips) > 1:  # and radio_out_tips not in excludes
                            print('根据提示', radio_out_tips)
                            driver_daily.radio_check(radio_out_tips)
                        # return driver_daily._search(content, options, excludes)
                        else:
                            print('无法根据提示判断，准备搜索……')
                    elif "单选题" in category:
                        options = driver_daily.radio_get_options()
                        if '因此本题选' in tips:
                            check=[x for x in letters if x in tips]
                            driver_daily.radio_check(check)
                        else:
                            radio_in_tips, radio_out_tips = "", ""
                            '''
                            option_elements = driver_daily.wait.until(driver_daily.EC.presence_of_all_elements_located(
                                (driver_daily.By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]/div[1]')))
                            # option_elements = self.find_elements(rules['challenge_options'])
                            options = [x.get_attribute("name") for x in option_elements]'''
                            for letter, option in zip(letters, options):
                                for tip in tips:
                                    if tip in option:
                                        # print(f'{option} in tips')
                                        if letter not in radio_in_tips:
                                            radio_in_tips += letter
                                    else:
                                        # print(f'{option} out tips')
                                        if letter not in radio_out_tips:
                                            radio_out_tips += letter

                            print('含 ', radio_in_tips, '不含', radio_out_tips)
                            if 1 == len(radio_in_tips):  # and radio_in_tips not in driver_daily.excludes:
                                print('根据提示', radio_in_tips)
                                driver_daily.radio_check(radio_in_tips)
                            elif 1 == len(radio_out_tips):  # and radio_out_tips not in excludes
                                print('根据提示', radio_out_tips)
                                driver_daily.radio_check(radio_out_tips)
                            # return driver_daily._search(content, options, excludes)
                            else:
                                print('无法根据提示判断，准备搜索……')
                    else:
                        print("题目类型非法")
                        break
                    # print("\r每日答题中，题目剩余{}题".format(d_log + d_num - i), end="")
                    time.sleep(1)
                d_log += d_num

            total, each = show_score(cookies)
            if each[5] >= 5:
                print("检测到每日答题分数已满,退出学习")
                driver_daily.quit()
        else:
            with open("./user/{}/d_log".format(uname), "w", encoding="utf8") as fp:
                fp.write(str(d_log))
            # break
        try:
            driver_daily.quit()
        except Exception as e:
            print('……')
    else:
        print("每日答题之前学完了")


def weekly(cookies, d_log, each, uname):
    begin_time = datetime.now()
    if each[6] < 5:
        # driver_weekly = mydriver.Mydriver(nohead=nohead)  time.sleep(random.randint(5, 15))
        driver_weekly = mydriver.Mydriver(nohead=False)
        # driver_weekly.driver.maximize_window()
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        driver_weekly.get_url("https://www.xuexi.cn/notFound.html")
        driver_weekly.set_cookies(cookies)
        try_count = 0

        if each[6] < 5:
            d_num = 6 - each[5]
            letters = list("ABCDEFGHIJKLMN")
            driver_weekly.get_url('https://pc.xuexi.cn/points/my-points.html')
            time.sleep(2)
            driver_weekly.click_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[6]/div[2]/div[2]/div')
            time.sleep(2)
            flag = 1
            for tem in range(0, 40):
                for tem2 in range(0, 5):
                    try:
                        temword = driver_weekly.driver.find_element_by_xpath(
                            '//*[@id="app"]/div/div[2]/div/div[4]/div/div[' + str(tem + 1) + ']/div[2]/div[' + str(
                                tem2 + 1) + ']/button').text
                    except:
                        temword = ''
                    name_list = ["开始答题", "继续答题"]
                    if flag == 1 and (any(name in temword for name in name_list)):
                        driver_weekly.click_xpath(
                            '//*[@id="app"]/div/div[2]/div/div[4]/div/div[' + str(tem + 1) + ']/div[2]/div[' + str(
                                tem2 + 1) + ']/button')
                        flag = 0
            while each[6] < 5:# and try_count < 10:
                if (datetime.now() - begin_time).seconds>(15*60):
                    print("包含不支持的题目，暂时跳过")
                    break
                try:
                    category = driver_weekly.xpath_getText(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div[1]/div[1]')  # get_attribute("name")
                except Exception as e:
                    print('查找元素失败！')
                    break
                print(category)
                tips = driver_weekly._view_tips()
                check_delay()
                if not tips:
                    print("本题没有提示")
                    break
                    if "填空题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "多选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "单选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                        # return driver_daily._search(driver_daily.content, driver_daily.options, driver_daily.excludes)
                    else:
                        print("题目类型非法")
                        break
                else:
                    if "填空题" in category:
                        answer = tips
                        driver_weekly.fill_in_blank(answer)

                    elif "多选题" in category:
                        options = driver_weekly.radio_get_options()
                        radio_in_tips, radio_out_tips = "", ""
                        for letter, option in zip(letters, options):
                            for tip in tips:
                                if tip in option:
                                    # print(f'{option} in tips')
                                    if letter not in radio_in_tips:
                                        radio_in_tips += letter
                        radio_out_tips = [letter for letter, option in zip(letters, options) if
                                          (letter not in radio_in_tips)]

                        print('含 ', radio_in_tips, '不含', radio_out_tips)
                        if len(radio_in_tips) > 1:  # and radio_in_tips not in driver_weekly.excludes:
                            print('根据提示', radio_in_tips)
                            driver_weekly.radio_check(radio_in_tips)
                        elif len(radio_out_tips) > 1:  # and radio_out_tips not in excludes
                            print('根据提示', radio_out_tips)
                            driver_weekly.radio_check(radio_out_tips)
                        # return driver_weekly._search(content, options, excludes)
                        else:
                            print('无法根据提示判断，准备搜索……')
                    elif "单选题" in category:
                        options = driver_weekly.radio_get_options()
                        if '因此本题选' in tips:
                            check=[x for x in letters if x in tips]
                            driver_weekly.radio_check(check)
                        else:
                            radio_in_tips, radio_out_tips = "", ""
                            '''
                            option_elements = driver_weekly.wait.until(driver_weekly.EC.presence_of_all_elements_located(
                                (driver_weekly.By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]/div[1]')))
                            # option_elements = self.find_elements(rules['challenge_options'])
                            options = [x.get_attribute("name") for x in option_elements]'''
                            for letter, option in zip(letters, options):
                                for tip in tips:
                                    if tip in option:
                                        # print(f'{option} in tips')
                                        if letter not in radio_in_tips:
                                            radio_in_tips += letter
                                    else:
                                        # print(f'{option} out tips')
                                        if letter not in radio_out_tips:
                                            radio_out_tips += letter

                            print('含 ', radio_in_tips, '不含', radio_out_tips)
                            if 1 == len(radio_in_tips):  # and radio_in_tips not in driver_weekly.excludes:
                                print('根据提示', radio_in_tips)
                                driver_weekly.radio_check(radio_in_tips)
                            elif 1 == len(radio_out_tips):  # and radio_out_tips not in excludes
                                print('根据提示', radio_out_tips)
                                driver_weekly.radio_check(radio_out_tips)
                            # return driver_weekly._search(content, options, excludes)
                            else:
                                print('无法根据提示判断，准备搜索……')
                    else:
                        print("题目类型非法")
                        break
                    # print("\r每周答题中，题目剩余{}题".format(d_log + d_num - i), end="")
                    time.sleep(1)
                d_log += d_num

            total, each = show_score(cookies)
            if each[6] >= 5:
                print("检测到每周答题分数已满,退出学习")
                driver_weekly.quit()
        else:
            with open("./user/{}/d_log".format(uname), "w", encoding="utf8") as fp:
                fp.write(str(d_log))
            # break
        try:
            driver_weekly.quit()
        except Exception as e:
            print('……')
    else:
        print("每周答题之前学完了")


def zhuanxiang(cookies, d_log, each, uname):
    begin_time = datetime.now()
    if each[7] < 10:
        # driver_zhuanxiang = mydriver.Mydriver(nohead=nohead)  time.sleep(random.randint(5, 15))
        driver_zhuanxiang = mydriver.Mydriver(nohead=False)
        # driver_zhuanxiang.driver.maximize_window()
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        # print('请保持窗口最大化')
        driver_zhuanxiang.get_url("https://www.xuexi.cn/notFound.html")
        driver_zhuanxiang.set_cookies(cookies)
        #try_count = 0

        if each[7] < 10:
            d_num = 10 - each[5]
            letters = list("ABCDEFGHIJKLMN")
            driver_zhuanxiang.get_url('https://pc.xuexi.cn/points/my-points.html')
            driver_zhuanxiang.click_xpath('//*[@id="app"]/div/div[2]/div/div[3]/div[2]/div[7]/div[2]/div[2]/div')
            time.sleep(2)
            for tem in range(0, 40):
                try:
                    temword = driver_zhuanxiang.driver.find_element_by_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div[' + str(tem + 1) + ']/div[2]/button').text
                except:
                    temword = ''
                name_list = ["开始答题", "继续答题"]  # , "重新答题"
                if (any(name in temword for name in name_list)):
                    driver_zhuanxiang.click_xpath(
                        '//*[@id="app"]/div/div[2]/div/div[4]/div/div/div/div[' + str(tem + 1) + ']/div[2]/button')
                    break
            while each[7] < 10:
                if (datetime.now() - begin_time).seconds>(15*60):
                    print("包含不支持的题目，暂时跳过")
                    break
                try:
                    category = driver_zhuanxiang.xpath_getText(
                        '//*[@id="app"]/div/div[2]/div/div[6]/div[1]/div[1]')  # get_attribute("name")
                except Exception as e:
                    print('查找元素失败！')
                    break
                print(category)
                tips = driver_zhuanxiang._view_tips()
                check_delay()
                if not tips:
                    print("本题没有提示")
                    break
                    if "填空题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "多选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                    elif "单选题" in category:
                        print('没有找到提示，暂时略过')
                        continue
                        # return driver_daily._search(driver_daily.content, driver_daily.options, driver_daily.excludes)
                    else:
                        print("题目类型非法")
                        break
                else:
                    if "填空题" in category:
                        answer = tips
                        driver_zhuanxiang.zhuanxiang_fill_in_blank(answer)

                    elif "多选题" in category:
                        options = driver_zhuanxiang.radio_get_options()
                        radio_in_tips, radio_out_tips = "", ""
                        for letter, option in zip(letters, options):
                            for tip in tips:
                                if tip in option:
                                    # print(f'{option} in tips')
                                    if letter not in radio_in_tips:
                                        radio_in_tips += letter
                        radio_out_tips = [letter for letter, option in zip(letters, options) if
                                          (letter not in radio_in_tips)]

                        print('含 ', radio_in_tips, '不含', radio_out_tips)
                        if len(radio_in_tips) > 1:  # and radio_in_tips not in driver_zhuanxiang.excludes:
                            print('根据提示', radio_in_tips)
                            driver_zhuanxiang.radio_check(radio_in_tips)
                        elif len(radio_out_tips) > 1:  # and radio_out_tips not in excludes
                            print('根据提示', radio_out_tips)
                            driver_zhuanxiang.radio_check(radio_out_tips)
                        # return driver_zhuanxiang._search(content, options, excludes)
                        else:
                            print('无法根据提示判断，准备搜索……')
                    elif "单选题" in category:
                        options = driver_zhuanxiang.radio_get_options()
                        if '因此本题选' in tips:
                            check=[x for x in letters if x in tips]
                            driver_zhuanxiang.radio_check(check)
                        else:
                            radio_in_tips, radio_out_tips = "", ""
                            '''
                            option_elements = driver_zhuanxiang.wait.until(driver_zhuanxiang.EC.presence_of_all_elements_located(
                                (driver_zhuanxiang.By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]/div[1]')))
                            # option_elements = self.find_elements(rules['challenge_options'])
                            options = [x.get_attribute("name") for x in option_elements]'''
                            for letter, option in zip(letters, options):
                                for tip in tips:
                                    if tip in option:
                                        # print(f'{option} in tips')
                                        if letter not in radio_in_tips:
                                            radio_in_tips += letter
                                    else:
                                        # print(f'{option} out tips')
                                        if letter not in radio_out_tips:
                                            radio_out_tips += letter

                            print('含 ', radio_in_tips, '不含', radio_out_tips)
                            if 1 == len(radio_in_tips):  # and radio_in_tips not in driver_zhuanxiang.excludes:
                                print('根据提示', radio_in_tips)
                                driver_zhuanxiang.radio_check(radio_in_tips)
                            elif 1 == len(radio_out_tips):  # and radio_out_tips not in excludes
                                print('根据提示', radio_out_tips)
                                driver_zhuanxiang.radio_check(radio_out_tips)
                            # return driver_zhuanxiang._search(content, options, excludes)
                            else:
                                print('无法根据提示判断，准备搜索……')
                    else:
                        print("题目类型非法")
                        break
                    # print("\r专项答题中，题目剩余{}题".format(d_log + d_num - i), end="")
                    time.sleep(1)
                d_log += d_num

            total, each = show_score(cookies)
            if each[6] >= 5:
                print("检测到专项答题分数已满,退出学习")
                driver_zhuanxiang.quit()
        else:
            with open("./user/{}/d_log".format(uname), "w", encoding="utf8") as fp:
                fp.write(str(d_log))
            # break
        try:
            driver_zhuanxiang.quit()
        except Exception as e:
            print('……')
    else:
        print("专项答题之前学完了")