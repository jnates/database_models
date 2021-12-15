import redis
import os 
from dotenv import load_dotenv
from faker import Faker
load_dotenv()

def redis_string():
    try:
        fake = Faker('it_IT')
        r = redis.Redis(host = os.getenv("REDIS_HOST"), 
                        port = os.getenv("REDIS_PORT"), 
                        db = os.getenv("REDIS_DB"), 
                        password = os.getenv("REDIS_PASSWORD"),
                        )
        for _ in range(10):
            r.sadd("message",fake.name())
            r.sadd("addres",fake.address())
#            r.flushall()
            msg = r.smembers("message")
            print(msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    redis_string()
