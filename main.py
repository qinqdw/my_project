#!/usr/bin/python
# -*-coding=utf-8-*-

def public(a):
    b = 10

    def inner():
        print(a+b)
    return inner


dm = public(20)
dm()
dm1 = public(30)
dm1()
