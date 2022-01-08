import redis
import time

r = redis.Redis(host = 'localhost', port = 6379, db = 1)

st = time.time()
for key in r.keys("event*"):
    r.hset(key, "event_created_at", "2020-11-16T00:00:00Z")
ed = time.time()

print("running time: " + str(ed - st) + "s")