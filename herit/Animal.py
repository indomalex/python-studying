#coding:utf-8

'''
Created on 2017��12��16��

@author: Administrator
'''

class Animal:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        
    def eat(self):
        print("%s在吃东西，颜色%s，有%s重" %(self.name, self.color, self.weight))
    
    def move(self):
        print("%s在板，颜色%s，有%s重，直顾在板。" %(self.name, self.color, self.weight))