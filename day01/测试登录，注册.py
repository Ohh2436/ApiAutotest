import requests

# 注册
url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15006007981&pwd=123456&regname="
r = requests.get(url)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"

url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15006907981&pwd=123456789101122334&regname=haha"
r = requests.post(url)
print(r.text)
assert r.json()['msg'] == "手机号码已被注册"

url = "http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=15096907981&pwd=&regname="
r = requests.post(url)
print(r.text)
assert r.json()['msg'] == "密码不能为空"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
zc = {"mobilephone":"","pwd":"85846215","regname":""}
r = requests.post(url,data=zc)
print(r.text)
assert r.json()['msg'] == "手机号不能为空"

url = "http://jy001:8081/futureloan/mvc/api/member/register"
data = [{
    "mobilephone":13478900657+i,
         "pwd":'sas1265+i',
         "regname":'ahsjdgjkhdsabnfdfgdgdfgdsgsgssssgsfgsgfdsfgfgckdh'+str(i)
         } for i in range(0,18)]
for i in data:
    r = requests.post(url,i)
    print(r.text)

# 登录
url = "http://jy001:8081/futureloan/mvc/api/member/login"
dl = [{
    "mobilephone":13478903647+i,
    "pwd":'sas1265+i',
}for i in range(0,7)]
for i in dl:
    r = requests.post(url,i)
    print(r.text)