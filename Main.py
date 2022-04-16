# Author: RYCB studio
# -*- coding:utf-8 -*-


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


import warnings

warnings.filterwarnings("ignore")

import configparser
from fuzzywuzzy import fuzz
import sys
import easygui as eg
import datetime

dt = datetime.datetime.now()
cfps = configparser.ConfigParser()


def main():
    init()
    a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "退出"], image='./yy.png')
    while a != "退出":
        if a == "学习":
            questions()
            a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "退出"], image='./yy.png')
        elif a == "做题":
            exercises()
            a = eg.buttonbox("请选择:", "qyf-rycbstudio.github.io", ["学习", "做题", "退出"], image='./yy.png')
        else:
            a = "学习"
    else:
        sys.exit(0)


def init():
    with open("logs/RYCBStudio-Log.log", "w") as w:
        w.write("")
    log("Program is Initializing...")
    log("Loading Module ConfigParser...")
    eg.msgbox("\t\t\t 【 航天知识学习检测系统V1.5 】", "qyf-rycbstudio.github.io", ok_button="下一步", image='./yy2.png')
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
                           ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], image="./ques.png")
    if choices != "./ques.png":
        try:
            eg.msgbox(ex_content[choices])
        except:
            init()
    else:
        questions()
    ex = eg.buttonbox("请选择： ", "qyf-rycbstudio.github.io", ["继续", "返回"], image="./ques.png")
    # ex = eg.ccbox("请选择： ", "qyf-rycbstudio.github.io", ["继续", "返回"])
    if ex == "继续":
        questions()
        log('The user had chose choice "next".')
    elif ex == "./ques.png":
        init()
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
    eg.msgbox("题目开始！", "qyf-rycbstudio.github.io", "Start！", image="./ans.png")
    log("Now choice: Normal Exercise")
    ex_content = eval(cfps['exercise']["ex_dict"])
    answer = []
    log("Exercises are showing...")
    for i in ex_content:
        try:
            res = eg.buttonbox("第" + str(i) + "题：(滑动鼠标滚轮可以查看C选项)" + ex_content[str(i)], "qyf-rycbstudio.github.io",
                               choices)
            answer.append(res)
        except KeyError as k:
            log(str(k), "fatal")
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
