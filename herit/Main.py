#coding:utf-8

'''
Created on 2017��12��16��

@author: Administrator
'''

from Practises.Fish import Fish
from Practises.Lion import Lion
from Practises.Bird import Bird


f = Fish("鱼", "红色", "0.5千克")
f.eat()
f.move()

l = Lion("狮子", "棕色", "500千克")
l.eat()
l.move()

b = Bird("鹦鹉", "花色", "2千克")
b.eat()
b.move()

