import json
import os
import sys
from multiprocessing import Pool
from urllib import request

url = 'http://10.98.80.88:10311/anniversarysign/activity/lottery?callback=index&ptype=5&uuid='

if len(sys.argv) >= 2:
    url = sys.argv[1]

print("the request url is ", url)


def query_info(uuid):
    url_path = url + str(uuid)
    with request.urlopen(url_path) as f:
        data = f.read().decode('utf-8')
        start = data.rfind("(")
        end = data.find(")")
        obj = json.loads(data[start + 1:end])
        code = obj['code']
        if code == 0:
            print("success,the code is %s" % code)
        else:
            print("error,the code is %s" % code)
        return code


def statistic(rs_list):
    success_count = 0
    for rs in rs_list:
        if (rs.get() == 0):
            success_count += 1
    print('All subprocesses done.success:%s,fail:%s' % (success_count, len(rs_list) - success_count))


if __name__ == "__main__":
    print("parent process %s" % os.getpid())
    p = Pool(20)
    rsList = []
    for i in range(1, 10):
        rs = p.apply_async(query_info, args=(5402,))
        rsList.append(rs)
    print('Waiting for all sub_processes done...')
    p.close()
    p.join()
    statistic(rsList)
