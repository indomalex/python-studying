#coding:utf-8

'''
Created on 2017��12��16��

@author: Administrator
'''

from Practises.Animal import Animal


class Lion(Animal):
    def __init__(self, name, color, weight):
        super().__init__(name, color, weight)
        
    def eat(self):
        super().eat()
        print("一口吃TM一大堆，凶得很。")
        
    def move(self):
        super().move()
        print("在地上跑起板起快得很，阵仗嘿大。")