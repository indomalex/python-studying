#coding:utf-8

'''
Created on 2017��12��16��

@author: Administrator
'''
from Practises.Animal import Animal


class Fish(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        
    def eat(self):
        super().eat()
        print("，一般吃TM一点点鱼食就饱了。")
        
    def move(self):
        super().move()
        print("，在水里游起板。")
    