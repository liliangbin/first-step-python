#!/usr/bin/env python

class Student(object):
    def __init__(self, name, sex, grade):
        self.__name = name
        self.sex = sex
        self.grade = grade

    # 两个下划线表示这是一个private 变量
    def score(self):
        print('%s:%d' % (self.__name, self.grade))


lili = Student('liliangbin', "boy", 33)

lili.score()
print("ihf")


class Anlimail(object):
    def run(self):
        print("anfhfh  is running")


class Dog(Anlimail):
    def run(self):
        print("doc  is running ")


def kjfsdh(alimal):
    alimal.run()


kjfsdh(Dog())
kjfsdh(Anlimail())
