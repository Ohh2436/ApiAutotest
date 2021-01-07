import pytest
import requests

# 注册功能的测试数据
@pytest.fixture(params=[{"mobilephone":18012345678,"pwd":123456,"regname":"","msg":"手机号码已被注册"},
                        {"mobilephone":1801234578,"pwd":123456,"regname":"","msg":"手机号码格式不正确"},
                        {"mobilephone":18012345678,"pwd":12346,"regname":"okk","msg":"密码长度必须为6~18"},
                        {"mobilephone":18012395678,"pwd":'126sdfghjklzxcvbnmk',"regname":"","msg":"密码长度必须为6~18"}])
def register_data(request):
    return request.param

def test_register(register_data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能,测试数据为：{register_data}")
    r = requests.post(url,data=register_data)
    print(r.text)
    assert r.json()['msg'] == register_data['msg']

#########################################################################################

@pytest.fixture(params=[{"data":{"mobilephone":18012345678,"pwd":123456,"regname":""},"expect":{"status":0,"code":"20110","data":None,"msg":"手机号码已被注册"}},
                        {"data":{"mobilephone":1801234578,"pwd":123456,"regname":""}, "expect":{"status":0,"code":"20109","data":None,"msg":"手机号码格式不正确"}},
                        {"data":{"mobilephone":18012345678,"pwd":12346,"regname":"okk"},"expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}},
                        {"data":{"mobilephone":18012395678,"pwd":'126sdfghjklzxcvbnmk',"regname":""},"expect":{"status":0,"code":"20108","data":None,"msg":"密码长度必须为6~18"}}])
def register_data1(request):
    return request.param

def test_register(register_data1):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    print(f"注册功能,测试数据为：{register_data1['data']}")
    r = requests.post(url,data=register_data1['data'])
    print(r.text)
    assert r.json()['msg'] == register_data1['expect']['msg']
    assert r.json()['status'] == register_data1['expect']['status']
    assert r.json()['code'] == register_data1['expect']['code']