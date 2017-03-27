import asyncio
import time
from urllib import request

url = 'http://act.zb.mi.com/anniversay-user-account/activity/queryInfo?uuid='

count = 0


@asyncio.coroutine
def query_info(uuid):
    global count
    url_path = url + str(uuid)
    with request.urlopen(url_path) as f:
        data = f.read().decode('utf-8')
        count += 1
        print(data)
        # start = data.find("(")
        # end = data.find(")")
        # obj = json.loads(data[start + 1:end])
        # code = obj['code']
        # if code == 0:
        #     print("success,uuid:%s the code is %s" % (uuid, code))
        # else:
        #     print("error,uuid:%s the code is %s" % (uuid, code))


loop = asyncio.get_event_loop()
tasks = []
begin = time.time();
for uuid in range(21904369, 21904379):
    tasks.append(query_info(uuid))
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
end = time.time();

print(end - begin)
print(count)
