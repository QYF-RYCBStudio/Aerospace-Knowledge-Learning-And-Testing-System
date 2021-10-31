# 航天知识问答系统

## 可以在[这里][here]下载

### 下面是源码：
````
# Author: RYCB studio
# -*- coding:utf-8 -*-
# MIT License
#
# Copyright (c) 2021 RYCBStudio
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
import os
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
    exercises()


def init():
    with open("logs/RYCBStudio-Log.log", "w") as w:
        w.write("")
    log("Program is Initializing...")
    log("Loading Module ConfigParser...")
    try:
        cfps.read("config.cfg", encoding="GBK")
        log("Module ConfigParser is Loaded.")
    except ModuleNotFoundError:
        log("Module ConfigParser isn't Loaded.")
    except UnicodeError or UnicodeEncodeError:
        cfps.read("config.cfg", encoding="UTF-8")
        log("Module ConfigParser is Loaded.")
    eg.msgbox("\t\t\t    欢迎进入航天知识问答系统", "qyf-rycbstudio.github.io", ok_button="下一步")


def exercises():
    global fuzz_res
    choices = ["A", "B", "C"]
    eg.msgbox("题目开始！", "qyf-rycbstudio.github.io", "Start！")
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
    for v in range(len(answer)):
        for k in range(len(ans)):
            fuzz_res = fuzz.ratio(answer[int(v)], ans[str(k + 1)])
            vk += fuzz_res
            cfps.set("Users", "usermarks", str(fuzz_res))
            cfps.write(open("config.cfg", "w"))
            break
    eg.msgbox("您的分数：" + str(fuzz_res), "qyf-rycbstudio.github.io")


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

````

[here]:https://github.com/QYF-RYCBStudio/Aerospace-Knowledge-Question-Answering-System/releases
