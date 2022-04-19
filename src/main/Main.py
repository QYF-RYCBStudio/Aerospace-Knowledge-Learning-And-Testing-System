# Author: RYCB studio
# -*- coding:utf-8 -*-
# Version 1.5.2-a


# MIT License
#
# Copyright (c) 2022 RYCBStudio
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import random
import warnings

warnings.filterwarnings("ignore")

import configparser
from fuzzywuzzy import fuzz
var = {'User-Agent': 'Mozilla/5.0 3578.98 Safari/537.36'}
import urllib.request as ur
import easygui as eg
import datetime
import webbrowser as wb
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

dt = datetime.datetime.now()
cfps = configparser.ConfigParser()


def checkForUpdates(rawServerName, serverName):
    cfps.read("update\\update.ucf")
    if rawServerName == "https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/raw/main/latestVersion":
        url = ur.Request(rawServerName, headers=var)
        ur.urlretrieve(url, ".\\update\\version")
    humanReadableVersion = cfps.get("Version", "version")
    machineReadableVersion = cfps.get("programSelfCheck", "version")
    with open("update\\version", "r") as v:
        v = v.readline().strip()
        if humanReadableVersion == v or machineReadableVersion == v:
            eg.msgbox("Congratulations! Your program version is the latest version!\n恭喜！您的程序版本是最新版本！")
        else:
            cc = eg.choicebox(
                "Oops! Your program version is not the latest version. You have two options:\n抱歉！您的程序版本不是最新版，您有两种选择：",
                "qyf-rycbstudio.github.io", ["Download the latest version\t下载最新版本", "No, thanks\t不了，谢谢"])
            if cc == "Download the latest version\t下载最新版本":
                cc1 = eg.choicebox("You have two options:",
                                   "qyf-rycbstudio.github.io",
                                   ["Let the program download the latest version\t让程序下载最新版本", "Manual Download\t手动下载"])
                if cc1 == "Let the program download the latest version\t让程序下载最新版本":
                    pass
                else:
                    eg.msgbox("Please go to the website to download\n请前往网页下载")
                    wb.open(serverName + "releases")
            else:
                pass


def main():
    init()
    a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "检查更新", "退出"], image='.\\yy.png')
    while a != "退出":
        if a == "学习":
            questions()
            a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "检查更新", "退出"], image='.\\yy.png')
        elif a == "做题":
            exercises()
            a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "检查更新", "退出"], image='.\\yy.png')
        elif a == "检查更新":
            choice = eg.buttonbox("请选择版本检查器存放位置：", "qyf-rycbstudio.github.io", ["Github（国外）（可能会报错）", "Gitee（国内镜像）(稳定）"])
            if choice == "Github（国外）（可能会报错）":
                checkForUpdates("https://raw.githubusercontent.com/QYF-RYCBStudio/Aerospace-Knowledge-Learning-And-Testing-System/", "https://github.com/QYF-RYCBStudio/Aerospace-Knowledge-Learning-And-Testing-System/")
            elif choice == "Gitee（国内镜像）(稳定）":
                checkForUpdates("https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/raw/main/latestVersion", "https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/")
            else:
                a = "检查更新"
            main()
    else:
        if eg.ynbox("确定退出吗？", "qyf-rycbstudio.github.io"):
            quit()
        else:
            main()


def init():
    with open("logs/RYCBStudio-Log.log", "w") as w:
        w.write("")
    log("Program is Initializing...")
    log("Loading Module ConfigParser...")
    eg.msgbox("\t\t\t 【 航天知识学习检测系统V1.5.1】", "qyf-rycbstudio.github.io", ok_button="下一步", image='.\\yy2.png')
    log("The Program has been started.")


def questions():
    try:
        cfps.read("config.cfg", encoding="GBK")
        log("Module ConfigParser is Loaded.")
    except ModuleNotFoundError:
        log("Module ConfigParser isn't Loaded.")
    except UnicodeError or UnicodeEncodeError:
        cfps.read("config.cfg", encoding="UTF-8")
        log("Module ConfigParser is Loaded.")
    log("Now choice: Normal Exercise")
    ex_content = eval(cfps['exercise']["ex_dict"])
    log("Dictionaries are showing...")
    choices = eg.buttonbox("请选择序号学习相关知识：", "qyf-rycbstudio.github.io",
                           ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], image=".\\ques.png")
    if choices != ".\\ques.png":
        try:
            eg.msgbox(ex_content[choices])
        except:
            init()
    else:
        questions()
    ex = eg.buttonbox("请选择： ", "qyf-rycbstudio.github.io", ["继续", "返回"], image=".\\ques.png")
    # ex = eg.ccbox("请选择： ", "qyf-rycbstudio.github.io", ["继续", "返回"])
    if ex == "继续":
        questions()
        log('The user had chose choice "next".')
    elif ex == ".\\ques.png":
        questions()
    else:
        log('The user had chose choice "exit".')
        main()


def exercises():
    try:
        cfps.read("exercises.cfg", encoding="GBK")
        log("Module ConfigParser is Loaded.")
    except ModuleNotFoundError:
        log("Module ConfigParser isn't Loaded.")
    except UnicodeError or UnicodeEncodeError:
        cfps.read("exercises.cfg", encoding="UTF-8")
        log("Module ConfigParser is Loaded.")
    global fuzz_res
    choices = ["A", "B", "C"]
    eg.msgbox("题目开始！", "qyf-rycbstudio.github.io", "Start！", image=".\\ans.png")
    log("Now choice: Normal Exercise")
    ex_content = eval(cfps['exercise']["ex_dict"])
    answer = []
    log("Exercises are showing...")
    for k in ex_content:
        i = random.randint(0, 49)
        for j in range(10):
            try:
                res = eg.buttonbox("第" + str(i) + "题：(滑动鼠标滚轮可以查看C选项)" + ex_content[str(i)], "qyf-rycbstudio.github.io",
                                   choices)
                answer.append(res)
                break
            except KeyError as k:
                log(str(k), "fatal")
        else:
            break
    log("Judging...")
    ans = eval(cfps["exercise"]["ex_ans"])
    vk = 0
    wrong = []
    for v in range(len(answer)):
        for k in range(len(ans)):
            fuzz_res = fuzz.ratio(answer[int(v)], ans[str(k + 1)]) / 10
            vk += fuzz_res
            cfps.set("Users", "usermarks", str(fuzz_res))
            cfps.write(open("exercises.cfg", "w"))
            if fuzz_res == 0:
                wrong.append("第" + str(v + 1) + "题   您的答案：" + answer[int(v)] + ";  正确答案：" + ans[str(k + 1)])
            else:
                pass
            break
    eg.msgbox("您的分数：" + str(vk), "qyf-rycbstudio.github.io")
    ex = eg.ccbox("错误题号：" + str(wrong), "qyf-rycbstudio.github.io", ["继续", "退出"])


def log(data, level="info", type="client"):
    with open("logs/RYCBStudio-Log.log", "a") as f:
        Nowtime = dt.strftime("%Y-%m-%d %T")
        if type == "client":
            if level == "info":
                f.write("[Client/INFO] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "warn":
                f.write("[Client/WARN] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "error":
                f.write("[Client/ERROR] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "fatal":
                f.write("[Client/FATAL] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "crash":
                f.write("[Client/CRASH_REPORT] " + '[' + Nowtime + '] ' + str(data) + "\n")
        else:
            if level == "info":
                f.write("[Server/INFO] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "warn":
                f.write("[Server/WARN] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "error":
                f.write("[Server/ERROR] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "fatal":
                f.write("[Server/FATAL] " + '[' + Nowtime + '] ' + str(data) + "\n")
            elif level == "crash":
                f.write("[Server/CRASH_REPORT] " + '[' + Nowtime + '] ' + str(data) + "\n")


if __name__ == "__main__":
    main()
