# Author: RYCB studio
# -*- coding:utf-8 -*-
# Version 1.5.2


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
import urllib.request as ur
from urllib.error import HTTPError, URLError
import warnings

warnings.filterwarnings("ignore")

import configparser
from fuzzywuzzy import fuzz
import easygui as eg
import datetime
import webbrowser as wb
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

dt = datetime.datetime.now()
cfps = configparser.ConfigParser()


def checkForUpdates(rawServerName, serverName):
    cfps.read("update\\update.ucf")
    try:
        ur.urlretrieve("{}/main/latestVersion".format(rawServerName), "update\\version")
    except HTTPError as httpE:
        eg.msgbox("There are some problems with this program.\nDetailed error information: {}.".format(str(httpE), "Error"))
        eg.msgbox("This problem will NOT be answered on GitHub.", "Information")
        main()
    except URLError as urlE:
        eg.msgbox("There are some problems with this program.\nDetailed error information: {}.\nPlease open a VPN connection or choose a better location, and then restart this program.".format(str(urlE), "Error"))
        eg.msgbox("This problem will NOT be answered on GitHub.", "Information")
        main()
    humanReadableVersion = cfps.get("Version", "version")
    machineReadableVersion = cfps.get("programSelfCheck", "version")
    with open("update\\version", "r") as v:
        v = v.readline().strip()
        if humanReadableVersion == v or machineReadableVersion == v:
            eg.msgbox("Congratulations! Your program version is the latest version!\n?????????????????????????????????????????????")
        else:
            cc = eg.choicebox(
                "Oops! Your program version is not the latest version. You have two options:\n??????????????????????????????????????????????????????????????????",
                "qyf-rycbstudio.github.io", ["Download the latest version\t??????????????????", "No, thanks\t???????????????"])
            if cc == "Download the latest version\t??????????????????":
                cc1 = eg.choicebox("You have two options:",
                                   "qyf-rycbstudio.github.io",
                                   ["Let the program download the latest version\t???????????????????????????", "Manual Download\t????????????"])
                if cc1 == "Let the program download the latest version\t???????????????????????????":
                    pass
                else:
                    eg.msgbox("Please go to the website to download\n?????????????????????")
                    wb.open(serverName + "releases")
            else:
                pass


def main():
    init()
    choice = ["????????????","????????????", "????????????", "????????????",  "??????"]
    a = eg.buttonbox("?????????:", "qyf-rycbstudio.github.io", choice, image=".\\pic\\yy.png")
    while a != choice[4]:
        if a == choice[0]:
            questions()
            a = eg.buttonbox("?????????:", "qyf-rycbstudio.github.io", choice, image=".\\pic\\yy.png")
        elif a == choice[2]:
            exercises()
            a = eg.buttonbox("?????????:", "qyf-rycbstudio.github.io", choice, image=".\\pic\\yy.png")
        elif a == choice[3]:
            choice = eg.buttonbox("???????????????????????????????????????", "qyf-rycbstudio.github.io",
                                  ["Github?????????????????????????????????", "Gitee??????????????????(WIP???"])
            if choice == "Github?????????????????????????????????":
                checkForUpdates(
                    "https://raw.githubusercontent.com/QYF-RYCBStudio/Aerospace-Knowledge-Learning-And-Testing-System/",
                    "https://github.com/QYF-RYCBStudio/Aerospace-Knowledge-Learning-And-Testing-System/")
            elif choice == "Gitee??????????????????(WIP???":
                #checkForUpdates("https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/raw/main/latestVersion","https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/")
                pass
            else:
                a = choice[3]
            main()
        elif a == choice[1]:
            buttons = ["????????????", "????????????", "?????????????????????", "?????????????????????"]
            res = eg.buttonbox("?????????????????????: ", "qyf-rycbstudio.github.io", buttons,image=".\\pic\\sp.png")
            #if res == buttons[0]:
            #     webbrowser.open("https://gitee.com/RYCBStudio/Aerospace-Knowledge-Question-Answering-System/tree/main/resources", autoraise=True)
            if res == buttons[0]:
                wb.open("http://www.cmse.gov.cn/kpjy/tkkt/tkkt/", autoraise=True)
            elif res == buttons[1]:
                wb.open("http://www.spacechina.com/n25/n148/n272/n4787/index.html", autoraise=True)   
            elif res == buttons[2]:
                wb.open("http://www.spacemore.com.cn/", autoraise=True)
            elif res == buttons[3]:
                wb.open("https://moon.bao.ac.cn/", autoraise=True)
            else:
                main()
        else:
            main()
    else:
        if eg.ynbox("??????????????????", "qyf-rycbstudio.github.io"):
            quit()
        else:
            main()


def init():
    with open("logs/RYCBStudio-Log.log", "w") as w:
        w.write("")
    log("Program is Initializing...")
    log("Loading Module ConfigParser...")
    eg.msgbox("\t\t\t ??? ??????????????????????????????V1.5.2???", "qyf-rycbstudio.github.io", ok_button="?????????", image='.\\pic\\yy2.png')
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
    choices = eg.buttonbox("????????????????????????????????????", "qyf-rycbstudio.github.io",
                           ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], image=".\\pic\\ques.png")
    if choices != ".\\pic\\ques.png":
        try:
            eg.msgbox(ex_content[choices])
        except:
            init()
    else:
        questions()
    ex = eg.buttonbox("???????????? ", "qyf-rycbstudio.github.io", ["??????", "??????"], image=".\\pic\\ques.png")
    # ex = eg.ccbox("???????????? ", "qyf-rycbstudio.github.io", ["??????", "??????"])
    if ex == "??????":
        questions()
        log('The user had chose choice "next".')
    elif ex == ".\\pic\\ques.png":
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
    global fuzz_res, k
    choices = ["A", "B", "C"]
    eg.msgbox("\t\t\t\t???????????????????????? \n\n\t\t??????????????????10????????????????????????10???????????????????????????", "qyf-rycbstudio.github.io", "????????????", image=".\\pic\\ans.png")
    log("Now choice: Normal Exercise")
    ex_content = eval(cfps["exercise"]["ex_dict"])
    answer = []
    ctrl = []
    log("Exercises are showing...")
    for k in range(10):
        i = random.randint(0, 49)
        for j in range(10):
            try:
                res = eg.buttonbox("???" + str(k + 1) + "??????" + ex_content[str(i)], "qyf-rycbstudio.github.io",
                                   choices)
                if res is not None:
                    answer.append(res)
                    ctrl.append(i)
                    break
                else:
                    continue
            except KeyError as k:
                log(str(k), "fatal")
            except NameError as n:
                log(str(n), "fatal")
        else:
            break
    log("Judging...")
    ans = dict(eval((cfps["exercise"]["ex_ans"])))
    vk = 0
    wrong = []
    for v in range(len(answer)):
        fuzz_res = fuzz.ratio(answer[int(v)], ans[str(ctrl[v])]) / 10
        vk += fuzz_res
        cfps.set("Users", "usermarks", str(vk))
        cfps.write(open("exercises.cfg", "w"))
        if fuzz_res == 0:
            wrong.append("???{}???".format(v + 1)+"    ???????????????{}".format(answer[int(v)]) + ";  ???????????????{}".format(ans[str(ctrl[v])])) 
        else:
            pass
        
    if vk==100:
        tips="\n\t\t  ??????????????????????????????????????????????????????"
    elif  vk>=80:
        tips="\n\t\t  ??????????????????????????????????????????????????????"
    elif vk>=60:
        tips="\n\t\t  ??????????????????????????????????????????????????????"
    else:
        tips="\n\t\t  ??????????????????????????????????????????????????????"
    eg.msgbox("\t\t\t??????????????????????????????" + str(int(vk))+"???\n"+tips, "qyf-rycbstudio.github.io")
    ex = eg.ccbox("???????????????\n" + str(wrong), "qyf-rycbstudio.github.io", ["??????", "??????"])


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
