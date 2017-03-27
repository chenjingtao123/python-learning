def consumer():
    r = ""
    while True:
        '''consumer通过yield拿到消息，处理，又通过yield把结果传回'''
        n = yield r
        if not n:
            return
        print("consumer %s ...." % n)
        r = '200 ok'


def producer(c):
    '''首先调用c.send(None)启动生成器'''
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("producer %s...." % n)
        '''通过c.send(n)切换到consumer执行'''
        r = c.send(n)
        '''produce拿到consumer处理的结果，继续生产下一条消息'''
        print("consumer return :%s" % r)
    '''produce决定不生产了，通过c.close()关闭consumer，整个过程结束'''
    c.close()


c = consumer()
producer(c)
