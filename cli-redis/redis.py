### pip install redis --user
import redis 

r = redis.Redis(host='localhost', port=7001, db=0)
r.set('key1', 'Hello World')
print('key1 ' + r.get('key1').decode('utf-8'))
