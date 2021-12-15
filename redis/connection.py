import redis

redis_host = '127.0.0.1'
redis_port = 6379
password = '1234'

def redis_string():
    try:
        r = redis.Redis(host=redis_host, port=redis_port, db=0, password=password)
        r.set("mensaje","test")
        msg = r.get("mensaje")
        print(msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    redis_string()
