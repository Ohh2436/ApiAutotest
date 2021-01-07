'''
注册的测试脚本
'''

# 注册失败的测试脚本
import json

import pytest
import requests

from zonghe.caw import DataRead, Asserts
from zonghe.baw import Member, Db
# env_path = r"/futureloan/mvc/api/member/login"
# pytest数据驱动的方式
# 从yaml中读取测试数据
from zonghe.test_script.conftest import baserequests


@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_fail.yaml"))
def fail_data(request):
    return request.param
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_pass.yaml"))
def pass_data(request):
    return request.param

def test_register_fail(url,baserequests,fail_data):
    # 下发注册请求
    r = Member.register(url,baserequests,fail_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == fail_data['expect']['code']
    # assert r.json()['msg'] == fail_data['expect']['msg']
    # assert r.json()['status'] == fail_data['expect']['status']
    Asserts.check(r.json(), fail_data['expect'], "code,msg,status")
# 注册成功的数据写到register_pass.yaml
# 注册成功的脚本，下发请求，断言相应结果
def test_register_pass(url, baserequests, pass_data,db):
    mobilephone = pass_data['data']['mobilephone']
    r = Member.list(url, baserequests)
    # 初始化环境：删除注册用户（数据库中可能有其他人的测试数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    r = Member.register(url,baserequests,pass_data['data'])
    # 断言响应的结果
    print(r.text)
    # assert r.json()['code'] == pass_data['expect']['code']
    # assert r.json()['msg'] == pass_data['expect']['msg']
    # assert r.json()['status'] == pass_data['expect']['status']
    Asserts.check(r.json(), pass_data['expect'], "code,msg,status")
    #调用查询的接口，在查询的结果中能找到本次注册的手机号
    r = Member.list(url,baserequests)
    print(r.text)
    assert str(mobilephone) in r.text
    d = r.json()['data']
    for i in d:
        print(i['mobilephone'])
        if i['mobilephone'] == '15129938653':
            break

    # 重复注册
@pytest.fixture(params=DataRead.read_yaml(r"data_case\register_repeat.yaml"))
def repeat_data(request):
    return request.param

def test_register_repeat(url, baserequests, repeat_data, db):
    mobilephone = repeat_data['data1']['mobilephone']
    # 初始化环境：删除注册用户（数据库中可能有其他人的测试数据，与本用例冲突）
    # Db.delete_user(db, mobilephone)
    # 下发注册环境
    r = Member.register(url, baserequests, repeat_data['data1'])
    Asserts.check(r.json(), repeat_data['expect1'], "code,msg,status")
    # 重复注册
    r = Member.register(url, baserequests, repeat_data['data2'])
    # assert str(r.json()['code']) == str(repeat_data['expect']['code'])
    # assert str(r.json()['msg']) == str(repeat_data['expect']['msg'])
    # assert str(r.json()['status']) == str(repeat_data['expect']['status'])
    Asserts.check(r.json(), repeat_data['expect2'], "code,msg,status")
    # print(r.json()['code'])
    # 清理环境：删除注册的用户
    Db.delete_user(db,mobilephone)
    # 注册失败，注册成功的测试数据补充完
