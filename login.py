# -*-coding:utf-8-*-
# @Time :2020/10/27 22:59
# @Author : LinaWu
# @Email: 786719402@qq.com
# File: login.py
# Software: PyCharm

#登录接口的功能逻辑
"""登录校验的函数
   :param username: 账号
   :param password: 密码
   :return dict type
   正确的用户名密码是：nmb_python/lemonban
   并要求用户名密码都不能为None
   """
def login_check(username,password):
   if username is not None and password is not None:
       if username=='nmb_python' and password=='lemonban':
           return {"code":0,"msg":"登录成功"}
       else:
           return {"code":1,"msg":"账号或者密码不正确"}
   elif username is None and password is not None:
       return {"code":1,"msg":"账号不能为空"}
   elif username is not None and password is None:
       return {"code":1,"msg":"密码不能为空"}
   else:
       return {"code":1,"msg":"账号不能为空，密码不能为空"}

if __name__=='__main__':
    print(login_check("nmb_python","lemonban"))




