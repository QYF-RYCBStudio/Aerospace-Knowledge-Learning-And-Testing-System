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
    # account()
    ex = exercises().__init__()


def init():
    with open("logs/RYCBStudio-Log.log", "w") as w:
        w.write("")
    log("Program is Initializing...")
    log("Loading Module ConfigParser...")
    try:
        cfps.read("config.cfg", encoding="GBK")
        log("Module ConfigParser is Loaded.")
    except:
        log("Module ConfigParser isn't Loaded.")
    eg.msgbox("\t\t\t    欢迎进入航天知识问答系统", "qyf-rycbstudio.github.io", ok_button="下一步")


def account():
    log("Now choice: Create a Account.")
    eg.msgbox("\t\t\t\t创建一个账户", "qyf-rycbstudio.github.io", ok_button="下一步")
    res = eg.enterbox("请输入用户名", "qyf-rycbstudio.github.io")
    try:
        try:
            try:
                cfps.set("Users", "username", res)
                cfps.write(open("config.cfg", "w"))
            except IndexError:
                log("Index Error:Err111", "fatal")
            except KeyError as k:
                log("Unknown Error:Err405    Detailed information:" + str(k), "fatal")
                sys.exit()
            except configparser.NoSectionError as NSE:
                log("Unknown Error:Err405    Detailed information:" + str(NSE), "fatal")
                sys.exit()
        except ValueError:
            pass
        res = eg.enterbox("请输入用户密码", "qyf-rycbstudio.github.io")
        try:
            try:
                cfps.set("Users", "userpwd", res)
                cfps.write(open("config.cfg", "w"))
            except IndexError:
                log("Index Error:Err111", "fatal")
        except ValueError:
            pass
    except KeyError as k:
        log("Unknown Error:Err405 " + str(k), "fatal")
        sys.exit()


class exercises():
    def __init__(self, wans, nans, ):
        self.with_answer = wans
        self.no_answer = nans

    def with_answer(self):
        eg.msgbox("题目开始！", "qyf-rycbstudio.github.io", "Start！")
        log("Now choice: Normal Exercise But with Answers")
        ex_content = eval(cfps['exercise']["ex_dict"])
        answer = []
        log("Exercises are showing...")
        ans = eval(cfps["exercise"]["ex_ans"])
        for v in range(1, len(ans) + 1):
            try:
                res = eg.buttonbox("第" + str(v) + "题：" + ex_content[str(v)], "qyf-rycbstudio.github.io", ans[str(v)])
                answer.append(res)
            except KeyError as k:
                log("KeyError:" + str(k), "fatal")
        log("Judging...")
        print(str(ans), "\n", str(answer))
        k = 0
        for v in range(len(answer)):
            for k in range(1, len(ans) + 1):
                print("用户答案\t" + answer[int(v)] + "\n与\n" + "标准答案\t" + ans[str(k + 1)])
                print("比较结果为：", end="")
                fuzz_res = fuzz.ratio(answer[int(v)], ans[str(k)])
                print(str(fuzz_res) + "%")
                break

    def no_answer(self):
        eg.msgbox("题目开始！", "qyf-rycbstudio.github.io", "Start！")
        log("Now choice: Normal Exercise")
        ex_content = eval(cfps['exercise']["ex_dict"])
        answer = []
        log("Exercises are showing...")
        for i in ex_content:
            try:
                res = eg.enterbox("第" + str(i) + "题：" + ex_content[str(i)], "qyf-rycbstudio.github.io", "")
                answer.append(res)
            except KeyError as k:
                log(str(k), "fatal")
        log("Judging...")
        ans = eval(cfps["exercise"]["ex_ans"])
        print(str(ans), "\n", str(answer))
        k = 0
        for v in range(len(answer)):
            for k in range(len(ans)):
                print(answer[int(v)])
                fuzz_res = fuzz.ratio(answer[int(v)], ans[str(k + 1)])
                cfps.set("Users", "usermarks", str(fuzz_res))
                break


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


def crash_log(data):
    Nowtime = dt.strftime("%Y-%m-%d-%H-%M-%S")
    with open("crash-reports/Crash-Report " + Nowtime + ".log", "w") as c:
        c.write("")
    with open("crash-reports/Crash-Report " + Nowtime + ".log", "a") as c:
        c.write(data + "\n")


if __name__ == "__main__":
    main()
