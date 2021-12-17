import redis, os, json
from dotenv import load_dotenv
load_dotenv()

def redis_string():
    try:
        r = redis.Redis(host = os.getenv("REDIS_HOST"), 
                        port = os.getenv("REDIS_PORT"), 
                        db = os.getenv("REDIS_DB"), 
                        password = os.getenv("REDIS_PASSWORD"),
                        )
        with open('despacho.json') as file:
            datos = json.load(file)

            for dato in datos:
                data = json.dumps(dato)
                print(data)
                r.sadd("Despacho",data)
    #r.flushall()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    redis_string()
