'''
脚本层的一些公共方法
'''
##################################################################
'''
python导入包的规则：
1.安装目录下找
2.如果使用IDE时：从当前工程路径、当前执行文件路径、python安装目录下找包。
3.命令行执行时，从当前执行的文件路径、python安装目录下找包。
命令行执行时，报错找不到包，解决办法：把工程路径，放到sys.path中。
'''
import sys
import os
# print(sys.path)
cp = os.path.realpath(__file__)  #D:\ApiAutoTest\zonghe\caw\DataRead.py
cd = os.path.dirname(cp) #D:\ApiAutoTest\zonghe\caw
cd = os.path.dirname(cd)
cd = os.path.dirname(cd)
sys.path.append(cd)
# print(sys.path)
#################################################################
import pytest

from zonghe.caw import DataRead
from zonghe.caw.BaseRequests import BaseReqests
env_path = r"data_env\env.ini"

# 读取env.ini中的url，设置session级别的，整个执行过程读一次
@pytest.fixture(scope='session')
def url():
    return DataRead.read_ini(env_path,"url")

@pytest.fixture(scope='session')
def db():
    return eval(DataRead.read_ini(env_path,'db'))

# 创建一个的实例，设置session级别的，整个执行过程只有一个实例，自动管理cookie
@pytest.fixture(scope='session')
def baserequests():
    return BaseReqests()