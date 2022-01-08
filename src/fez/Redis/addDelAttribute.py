import json
import redis
import time

r = redis.Redis(host = 'localhost', port = 6379, db = 1)

def upload(ins, name):
    if "id" not in ins.keys(): return
    field = str(name + ":" + str(ins["id"]))
    for (key, val) in ins.items():
        if type(val) is dict:
            r.hset(field, str(key), upload(val, key))
        else:
            r.hset(field, str(key), str(val))
    return field

# t = 0
totTime = 0
entry = 0
def delOrg(ins):
    global totTime, entry
    if "org" not in ins.keys(): return
    event = "event:" + str(ins["id"])
    org = "org:" + str(ins["org"]["id"])
    st = time.time()
    r.hdel(event, "org");
    r.delete(org)
    ed = time.time()
    totTime = totTime + ed - st
    entry = entry + 1

for line in open('2020-01-01-012.json', 'r').readlines():
    event = json.loads(line)
    del event["payload"]
    delOrg(event)
    # t = t + 1
    # if t > 5: break

print("deleting time: " + str(totTime) + "s with total " + str(entry) + " entries")

def addOrg(ins):
    global totTime, entry
    if "org" not in ins.keys(): return
    event = "event:" + str(ins["id"])
    org = "org:" + str(ins["org"]["id"])
    st = time.time()
    r.hset(event, "org", org)
    upload(ins["org"], "org")
    ed = time.time()
    totTime = totTime + ed - st
    entry = entry + 1

# t = 0
totTime = 0
entry = 0
for line in open('2020-01-01-012.json', 'r').readlines():
    event = json.loads(line)
    del event["payload"]
    addOrg(event)
    # t = t + 1
    # if t > 5: break

print("adding time: " + str(totTime) + "s with total " + str(entry) + " entries")
