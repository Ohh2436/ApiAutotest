'''
上传文件：
    本地文件上传到服务器上。比如：上传头像，上传附件等。
'''

import requests

# 上传文件的接口
url = "http://www.httpbin.org/post"
# 要上传的文件files参数（本地磁盘上的文件）
filePath = "D:/test.txt"
filePath2 = "D:/logo.png"
# 'name':file-tuple
#  2-tuple ``('filename', fileobj)``,
#  3-tuple ``('filename', fileobj, 'content_type')``
#  4-tuple ``('filename', fileobj, 'content_type', custom_headers)``
with open(filePath,'rb') as f:
    with open(filePath2,'rb') as f2:
        file = {
            "file1":(filePath,f), #二元组2-tuple ``('filename', fileobj)``,
            # content_type MIME类型，大类型/子类型 text/plain image/pig application/json......
            "file2":(filePath2,f2,"image/png")
        }
        r = requests.post(url,files=file)
        print(r.text)