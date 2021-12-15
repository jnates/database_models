import redis
import os 
from dotenv import load_dotenv
load_dotenv()

def redis_string():
    try:
        r = redis.Redis(host = os.getenv("REDIS_HOST"), 
                        port = os.getenv("REDIS_PORT"), 
                        db = os.getenv("REDIS_DB"), 
                        password = os.getenv("REDIS_PASSWORD"),
                        )
        r.set("mensaje","test")
        msg = r.get("mensaje")
        print(msg)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    redis_string()
