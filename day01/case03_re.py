# -*- coding: utf-8 -*-
# -*- author: GXR -*-

# 2. match()
import re

content = 'Hello 123 4567 World_This is a Regex Demo'
print(len(content))
# 在match()方法中，第一个参数传入了正则表达式，第二个参数传入了要匹配的字符串。
result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
print(result)
# group()方法可以输出匹配到的内容
print(result.group())
# span()方法可以输出匹配的范围,就是匹配到的结果字符串在原字符串中的位置范围
print(result.span())

# 可以使用()括号将想提取的子字符串括起来。()实际上标记了一个子表达式的开始和结束位置，被标记的每个子表达式会依次对应每一个分组，调用group()方法传入分组的索引即可获取提取的结果。
import re

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
