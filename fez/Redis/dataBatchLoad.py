import json
import redis
import time

r = redis.Redis(host = 'localhost', port = 6379, db = 1)
r.flushdb()

def upload(ins, name):
    if "id" not in ins.keys(): return
    field = str(name + ":" + str(ins["id"]))
    for (key, val) in ins.items():
        if type(val) is dict:
            r.hset(field, str(key), upload(val, key))
        else:
            r.hset(field, str(key), str(val))
    return field

st = time.time()

for line in open('2020-01-01-0.json', 'r').readlines():
    event = json.loads(line)
    del event["payload"]
    upload(event, "event")

ed = time.time()

print("Hour 0 running time: " + str((ed - st) / 34423 * 1000) + "ms / entry")

st = time.time()

for line in open('2020-01-01-1.json', 'r').readlines():
    event = json.loads(line)
    del event["payload"]
    upload(event, "event")

ed = time.time()

print("Hour 1 running time: " + str((ed - st) / 32719 * 1000) + "ms / entry")

st = time.time()

for line in open('2020-01-01-2.json', 'r').readlines():
    event = json.loads(line)
    del event["payload"]
    upload(event, "event")

ed = time.time()

print("Hour 2 running time: " + str((ed - st) / 33810 * 1000) + "ms / entry")

