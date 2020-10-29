# -*-coding:utf-8-*-
# @Time :2020/10/27 23:14
# @Author : LinaWu
# @Email: 786719402@qq.com
# File: test_login.py
# Software: PyCharm

from allure_use.login import login_check

def test_login_success():
    # 步骤
    result=login_check("nmb_python","lemonban")
    # 断言
    assert result=={"code":0,"msg":"登录成功"}


