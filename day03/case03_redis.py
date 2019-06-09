# -*- coding: utf-8 -*-
# -*- author: GXR -*-
from redis import StrictRedis, ConnectionPool

'''
Redis TCP连接
    redis://[:password]@host:port/db
Redis TCP+SSL连接
    rediss://[:password]@host:port/db
Redis UNIX socket连接
    unix://[:password]@/path/to/socket.sock?db=db
'''

# url = 'redis://:1111@39.106.189.108:6379/0'
# pool = ConnectionPool.from_url(url)
# redis = StrictRedis(connection_pool=pool)
# redis.set('name', 'Bob')
# print(redis.get('name'))

redis = StrictRedis(host='127.0.0.1', port=6379, db=0, password='1111')
redis.set('name', 'Bob')
print(redis.get('name'))
print(redis.dbsize())
print(redis.getset('name', 'Mike'))
