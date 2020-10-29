# -*-coding:utf-8-*-
# @Time :2020/10/27 22:54
# @Author : LinaWu
# @Email: 786719402@qq.com
# File: main.py
# Software: PyCharm

import pytest
if __name__=='__main__':
    # pytest.main()   #执行pytest命令，去收集用例，然后执行用例，当前文件所在目录为rootdir
    pytest.main(["--alluredir=allure_testresult_files"]) #执行pytest命令，并生成allure能识别的测试结果文件