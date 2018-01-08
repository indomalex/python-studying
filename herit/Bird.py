#coding:utf-8

'''
Created on 2017��12��16��

@author: Administrator
'''
from Practises.Animal import Animal


class Bird(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        
    def eat(self):
        super().eat()
        print("东啄一哈，西啄一哈，啄不到好点东西吃。")
        
    def move(self):
        super().move()
        print("板起飞起快得很。")