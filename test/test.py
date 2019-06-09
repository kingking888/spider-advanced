# -*- coding: utf-8 -*-
# -*- author: GXR -*-
import re

proxy = '127.0.0.1:5050'
aaa = re.match('\d+\.\d+\.\d+\.\d+:\d+', proxy)
print(aaa.group())
