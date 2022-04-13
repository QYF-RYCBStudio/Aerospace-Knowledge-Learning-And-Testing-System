@rem 安装程序所需模块
@echo off
chcp 65001
cd %program files%/python
cd ./Scripts
title 安装程序所需模块...
echo 安装程序所需模块 EasyGUI...
pip install easygui
echo 安装程序所需模块 ConfigParser...
pip install configparser
echo 安装程序所需模块 datetime...
pip install datetime
echo 安装程序所需模块 fuzzywuzzy...
pip install fuzzywuzzy
echo 按任意键继续
pause>nul
echo 完成
echo 请按任意键退出...
pause>nul
exit