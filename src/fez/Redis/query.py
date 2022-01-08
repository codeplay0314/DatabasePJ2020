import json
import redis
import time

r = redis.Redis(host = 'localhost', port = 6379, db = 1)
rr = redis.Redis(host = 'localhost', port = 6379, db = 2)
rr.flushdb()

z = "actorRank"
st = time.time()
for key in r.keys("event*"):
    rr.zincrby(z, 1, r.hget(key, "actor"))
num = int(r.zcard(z) * 0.05)
rr.zrange(z, 0, num, desc = True, withscores = True)
ed = time.time()
print("running time: " + str(ed - st) + "s")

z = "eventRank"
st = time.time()
for key in r.keys("event*"):
    typ = r.hget(key, "type")
    rr.zincrby(z, 1, typ)
    rr.sadd("actorList:" + typ, r.hget(key, "actor"))
rr.zrange(z, 0, -1, desc = True, withscores = True)
for key in r.keys("actorList*"):
    rr.smembers(key)
ed = time.time()
print("running time: " + str(ed - st) + "s")

rr.flushall()