# -*-coding:utf-8-*-
# @Time :2020/10/27 23:31
# @Author : LinaWu
# @Email: 786719402@qq.com
# File: test_login_exception.py
# Software: PyCharm

from allure_use.login import login_check

class Test_loginException:
    def test_login_username_is_wrong(self):
        result = login_check("nmb_python11", "lemonban")
        assert result == {"code": 1, "msg": "账号或者密码不正确"}

    def test_login_password_is_wrong(self):
        result = login_check("nmb_python", "lemonban11")
        assert result == {"code": 1, "msg": "账号或者密码不正确"}

    def test_login_username_is_none(self):
        result=login_check(None,"lemonban")
        assert result=={"code":1,"msg":"账号不能为空"}

    def test_login_password_is_none(self):
        result = login_check("nmb_python", None)
        assert result == {"code": 1, "msg": "密码不能为空111"}

    def test_login_username_password_both_none(self):
        result = login_check(None, None)
        assert result == {"code": 1, "msg": "账号不能为空，密码不能为空"}