# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# # 3. GET请求
# import requests

# r = requests.get('https://www.baidu.com/')
# r.encoding = r.apparent_encoding
# print(type(r))
# print(r.status_code)
# print(type(r.text))
# print(r.text)
# print(r.cookies)


# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(type(r.json()))

# import requests
# import re
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

# import requests
#
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)


# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(r.text)


# # 4. POST请求

# import requests
#
# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)


# # 5. 响应
# import requests
#
# r = requests.get('http://www.baidu.com')
# # status_code属性得到状态码
# print(type(r.status_code), r.status_code)
# # 输出headers属性得到响应头
# print(type(r.headers), r.headers)
# # 输出cookies属性得到Cookies
# print(type(r.cookies), r.cookies)
# # 输出url属性得到URL
# print(type(r.url), r.url)
# # 输出history属性得到请求历史
# print(type(r.history), r.history)

# 状态码常用来判断请求是否成功，而requests还提供了一个内置的状态码查询对象requests.codes
# import requests
#
# r = requests.get('http://www.baidu.com')
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')

# # 1. 文件上传
# import requests
#
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text)

# # 2. Cookies
# import requests
#
# r = requests.get("https://www.baidu.com")
# print(r.cookies)
# for key, value in r.cookies.items():
#     print(key + '=' + value)

# import requests
#
# headers = {
#     'Cookie': '_zap=35ec77d7-3f1a-43bd-99f7-60be682256c9; _xsrf=yvlQ4xzecTHYFBAmlWRIv8PbjEHnDfwf; d_c0="ACDrElx4dw-PTqamL9XNjCaxNKL2pbc8vUY=|1558495544"; capsion_ticket="2|1:0|10:1558495563|14:capsion_ticket|44:NTM4ZDlkMWRjMWUxNDczZWJjZWFkNmVmZDUwMzdjYTY=|b29138515960a3c71025b70e3221e9f5ec84688d9263f79c7a20fbbacc57deaf"; z_c0="2|1:0|10:1558495573|4:z_c0|92:Mi4xSDBOVkJ3QUFBQUFBSU9zU1hIaDNEeVlBQUFCZ0FsVk5WUV9TWFFBemZvdlhTZnJkcURZS1NsUi1IUEJWeUw4NDBB|269a0aab9139cfbc0f944531e9174aac704eeea7145afdfb348aaf029cbd69e4"; tst=r; q_c1=a8fac6b1be934b02a59dfc292a4c1395|1558599136000|1558599136000; __utma=51854390.780621626.1558599143.1558599143.1558599143.1; __utmb=51854390.0.10.1558599143; __utmc=51854390; __utmz=51854390.1558599143.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20180115=1^3=entry_date=20180115=1; tgw_l7_route=80f350dcd7c650b07bd7b485fcab5bf7',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)


# # 3. 会话维持
# import requests
#
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


# # 4. SSL证书验证
# # 如果不加verify参数的话，默认是True，会自动验证
# # 如果请求一个HTTPS站点，证书验证错误，避免这个错误,把verify参数设置为False
# import requests
#
# response = requests.get('https://www.newcoder.top', verify=False)
# print(response.status_code)
#
# # 通过捕获警告到日志的方式忽略警告
# import logging
# import requests
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


# # 5. 代理设置
# import requests
#
# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
#
# response = requests.get("https://www.taobao.com", proxies=proxies)
# print(response.status_code)


# # 6. 超时设置
# # 可以将超时时间设置为1秒，如果1秒内没有响应，那就抛出异常。
# import requests
#
# r = requests.get("https://www.taobao.com", timeout=1)
# print(r.status_code)
#
# # 如果想永久等待，可以直接将timeout设置为None，或者不设置直接留空，因为默认是None。
# r1 = requests.get('https://www.taobao.com', timeout=None)
# print(r1.status_code)
# r2 = requests.get('https://www.taobao.com')
# print(r2.status_code)


# # 7. 身份认证
# # 使用requests自带的身份认证功能
# # 如果用户名和密码正确的话，请求时就会自动认证成功，会返回200状态码，如果认证失败，则返回401状态码。
# import requests
# from requests.auth import HTTPBasicAuth
#
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)
# # 简写如下
# import requests
#
# r = requests.get('http://localhost:5000', auth=('username', 'password'))
# print(r.status_code)


# # 8. Prepared Request
# # 引入了Request，然后用url、data和headers参数构造了一个Request对象
# # 再调用Session的prepare_request()方法将其转换为一个Prepared Request对象，然后调用send()方法发送即可
# # 有了Request这个对象，就可以将请求当作独立的对象来看待，这样在进行队列调度时会非常方便。后面我们会用它来构造一个Request队列。
# from requests import Request, Session
#
# url = 'http://httpbin.org/post'
# data = {
#     'name': 'germey'
# }
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }
# s = Session()
# req = Request('POST', url, data=data, headers=headers)
# prepped = s.prepare_request(req)
# r = s.send(prepped)
# print(r.text)
