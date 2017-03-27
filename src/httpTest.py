import threading
from urllib import request

url = 'http://act.zb.mi.com/anniversay-user-account/activity/queryInfo?uuid='


def query_info(uuid):
    url_path = url + str(uuid)
    with request.urlopen(url_path) as f:
        print('status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))


count, uuid = 1, 21904369
while count < 20:
    t = threading.Thread(target=query_info(uuid), name="query_info" + str(count))
    t.start()
    t.join()
    count += 1
    uuid += count

print('thread %s ended.' % threading.current_thread().name)
