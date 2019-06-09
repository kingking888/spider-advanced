# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# import socket
# import urllib.parse
# import urllib.error
# import urllib.request


# # ==========1.urlopen==========
#
# response = urllib.request.urlopen('http://www.python.org')
# # # 响应类型,HTTPResposne类型的对象
# print(type(response))
# # # 响应状态码
# print(response.status)
# # # 响应头信息
# print(response.getheaders())
# # # 传递单个参数获取响应值
# print(response.getheader('Server'))
# # # 响应网页内容
# print(response.read().decode('utf-8'))
#
# # data参数,post提交参数,字节流编码格式的内容，即bytes类型，则需要通过bytes()方法转化
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response1 = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response1.read())
#
# # timeout,响应超时参数,超出了设置的这个时间，还没有得到响应，就会抛出异常
# try:
#     response2 = urllib.request.urlopen('http://httpbin.org/get', timeout=10)
#     print(response2.read())
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('Time Out')
#
# # context,SSL设置
# # cafile和capath这两个参数分别指定CA证书和它的路径，这个在请求HTTPS链接时会有用
# # cadefault参数现在已经弃用了，其默认值为False。


# # ==========2.Request==========

# # urlopen()方法来发送这个请求，只不过这次该方法的参数不再是URL，而是一个Request类型的对象。
# request = urllib.request.Request('https://python.org')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#     'Host': 'httpbin.org'
# }
# dicts = {
#     'name': 'Germey'
# }
# data = bytes(urllib.parse.urlencode(dicts), encoding='utf8')
# # 第一个参数url用于请求URL，这是必传参数
# # 第二个参数data如果要传，必须传bytes（字节流）类型的
# # 第三个参数headers是一个字典，是请求头，请求时通过headers参数添加，也可以通过调用请求实例的add_header()方法添加。
# request = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))

# # headers也可以用add_header()方法来添加
# request = urllib.request.Request(url=url, data=data, method='POST')
# request.add_header('User-Agent',
#                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')

# # 验证
# from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
# from urllib.error import URLError
#
# username = 'username'
# password = 'password'
# url = 'http: //localhost:sooo/'
# p = HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None, url, username, password)
# auth_handler = HTTPBasicAuthHandler(p)
# opener = build_opener(auth_handler)
# try:
#     result = opener.open(url)
#     html = result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# # 代理
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener
#
# proxy_handler = ProxyHandler({
#     'http': 'http://127.0.0.1:9743',
#     'https': 'https://127.0.0.1:9743'
# })
# opener = build_opener(proxy_handler)
# try:
#     response = opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# Cookies
# import http.cookiejar, urllib.request

# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name + '=' + item.value)

# # cookie输出Mozilla文件格式
# filename = 'cookies.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)

# # cookie输出Mozilla文件格式
# filename = 'cookies.txt'
# cookie = http.cookiejar.LWPCookieJar(filename)
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True, ignore_expires=True)


# 处理异常

# # 1.URLError
# URLError类来自urllib库的error模块，继承自OSError类，是error异常模块的基类，由request模块生的异常都可以通过这个类来处理。
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.URLError as e:
# # reason，即返回错误的原因。
#     print(e.reason)

# # 2.HTIPError
# # 它是URLError的子类，专门用来处理HTTP请求错误，比如认证请求失败等。它有如下3个属性。
# # code：返回HTTP状态码，比如404表示网页不存在，500表示服务器内部错误等。
# # reason：同父类一样，用于返回错误的原因。
# # headers：返回请求头。
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)

# # 先捕获HTTPError，获取它的错误状态码、原因、headers等信息。如果不是HTTPError异常，就会捕获URLError异常，输出错误原因。
# from urllib import request, error
#
# try:
#     response = request.urlopen('https://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason, e.code, e.headers)
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Qequest is Successfully')


# # 解析链接
# # 1.urlparse()
# # 该方法可以实现URL的识别和分段
# from urllib.parse import urlparse

# result = urlparse('http://www.baidu.com/index.html;user?id=S#comment')
# print(type(result), '\n', result)

# # 返回结果是一个ParseResult类型的对象，它包含6部分，分别是scheme、netloc、path、params、query和fragment。
# # ://前面的就是scheme，代表协议；第一个/前面便是netloc，即域名；分号;前面是params，代表参数。
# http://www.baidu.com/index.html;user?id=S#comment
# scheme://netloc/path;params?query#fragment

# # 2. urlunparse()
# # 接受的参数是一个可迭代对象，但是它的长度必须是6，否则会抛出参数数量不足或者过多的问题。
# from urllib.parse import urlunparse
#
# data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data))

# # 3. urlsplit()
# # 这个方法和urlparse()方法非常相似，只不过它不再单独解析params这一部分，只返回5个结果，上面例子中的params会合并到path中。
# from urllib.parse import urlsplit
#
# result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
# # 返回结果是SplitResult，它其实也是一个元组类型，既可以用属性获取值，也可以用索引来获取
# print(result.scheme, result[0])

# # 4. urlunsplit()
# # 将链接各个部分组合成完整链接的方法，传入的参数也是一个可迭代对象，例如列表、元组等，唯一的区别是长度必须为5
# from urllib.parse import urlunsplit
#
# data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data))

# # 5. urljoin()
# # 提供一个base_url（基础链接）作为第一个参数，将新的链接作为第二个参数，该方法会分析base_url的scheme、netloc和path这3个内容并对新链接缺失的部分进行补充，最后返回结果。
# from urllib.parse import urljoin
#
# print(urljoin('http://www.baidu.com', 'FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html'))
# print(urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# print(urljoin('http://www.baidu.com?wd=abc', 'https://cuiqingcai.com/index.php'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'))

# # 6. urlencode()
# # 声明了一个字典来将参数表示出来，然后调用urlencode()方法将其序列化为GET请求参数。
# from urllib.parse import urlencode
#
# params = {
#     'name': 'germey',
#     'age': 22
# }
# base_url = 'http://www.baidu.com?'
# url = base_url + urlencode(params)
# print(url)

# # 7. parse_qs()
# # 一串GET请求参数，利用parse_qs()方法，就可以将它转回字典
# from urllib.parse import parse_qs
#
# query = 'name=germey&age=22'
# print(parse_qs(query))

# # 8.parse_qsl()
# # 将参数转化为元组组成的列表,元组的第一个内容是参数名，第二个内容是参数值。
# from urllib.parse import parse_qsl
#
# query = 'name=germey&age=22'
# print(parse_qsl(query))

# # 9. quote()
# # URL编码，将中文转化为URL编码
# from urllib.parse import quote, unquote
#
# keyword = '壁纸'
# url = 'https://www.baidu.com/s?wd=' + quote(keyword)
# print(url)

# # 10. unquote()
# # URL解码，将URL编码还原
# url1 = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
# print(unquote(url1))


# # Robots协议

# from urllib.robotparser import RobotFileParser
#
# rp = RobotFileParser('https://www.newcoder.top/robots.txt')
# print(rp.read())
# # can_fetch()方法判断了网页是否可以被抓取
# print(rp.can_fetch('*', 'https://newcoder.top/blog/article_detail/rahgip6z/'))
# print(rp.can_fetch('*', 'https://newcoder.top/user/user/b9tq8tq1/'))
