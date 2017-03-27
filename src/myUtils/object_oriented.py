class Human:
    pass


class Woman(Human):
    count = 0


    def __init__(self, name):
        self.__name = name

    @property
    def name1(self):
        print("get name invoked")
        return self.__name

    @name1.setter
    def name1(self, name):
        print("set name invoked")
        self.__name = name

    @classmethod
    def count11(cls):
        print("count is ", cls.count)


human = Woman("wangmin")

human.name1 = "fdfdfd"
Woman.count11()
