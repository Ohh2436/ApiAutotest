'''
fixture 带参数
'''
import pytest
import requests

# # 登录功能的测试数据
# @pytest.fixture(params=[{"mobilephone":18012345678,"pwd":123456},
#                         {"mobilephone":18012345678,"pwd":12345},
#                         {"mobilephone":18012345678,"pwd":""},
#                         {"mobilephone":178,"pwd":123456}])
# def login_data(request): #request是pytest中的关键字，固定写法
#     return request.param # 通过request.param返回每一组数据，固定写法
#
# # 数据驱动测试
# # 登录功能的脚本测试
# def test_login(login_data):
#     print(f"登录功能,测试数据为：{login_data}")
#     print(f"手机号：{login_data['mobilephone']}")
#     print(f"密码：{login_data['pwd']}")

# 注册功能的测试数据
url = "http://jy001:8081/futureloan/mvc/api/member/register"
@pytest.fixture(params=[{"mobilephone":18012345678,"pwd":123456,"regname":""},
                        {"mobilephone":18002345678,"pwd":123456,"regname":"ohh"},
                        {"mobilephone":1801234578,"pwd":123456,"regname":""},
                        {"mobilephone":18012345678,"pwd":12346,"regname":"okk"},
                        {"mobilephone":18012395678,"pwd":'126sdfghjklzxcvbnmk',"regname":""}])
def login1_data(request):
    return request.param

def test_login1(login1_data):
    r = requests.post(url,data=login1_data)
    print(r.text)
    assert r.json()['msg'] =='手机号码已被注册' or '手机号码格式不正确' or '密码长度必须为6~18'
    print(f"注册功能,测试数据为：{login1_data}")
    print(f"手机号：{login1_data['mobilephone']}")
    print(f"密码：{login1_data['pwd']}")
    print(f"用户名：{login1_data['regname']}")