import pytest

from zonghe.baw import Db, Member
from zonghe.caw import DataRead, Asserts

'''
def test_login():
    # 注册用户
    # 下发请求
    # 检查结果
    # 删除注册用户
    pass
'''
@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_setup.yaml"))
def setup_data(request):
    return request.param
@pytest.fixture(params=DataRead.read_yaml(r"data_case\login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture()
def register(setup_data,url,db,baserequests):
    ##################第一部分执行的#######################
    mobilephone = setup_data['casedata']['mobilephone']
    # 初始化环境：删除注册用户（数据库中可能有其他人的测试数据，与本用例冲突）
    Db.delete_user(db, mobilephone)
    # 下发注册请求
    Member.register(url, baserequests, setup_data['casedata'])
    yield
    ##################第三部分执行的#######################
    # 清理环境：删除注册的用户
    Db.delete_user(db, mobilephone)


def test_login2(register,url,baserequests,login_data):
    ##################第二部分执行的#######################
    print("下发登录请求")
    # 下发登录请求
    r = Member.login(url,baserequests,login_data['casedata'])
    print("检查结果")
    # assert str(r.json()['code']) == str(login_data['expect']['code'])
    # assert str(r.json()['msg']) == str(login_data['expect']['msg'])
    # assert str(r.json()['status']) == str(login_data['expect']['status'])

    Asserts.check(r.json(),login_data['expect'],"code,msg,status")