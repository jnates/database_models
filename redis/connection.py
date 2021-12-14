import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0, password="1234")
r.set('name', 'test')
print(r.get('name'))