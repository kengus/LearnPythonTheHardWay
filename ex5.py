#!/usr/bin/python
#-*- coding:utf-8 -*-
my_name = "benfree"
my_age = 35
my_height = 180
my_weight = 95
my_eyes = "brown"
my_teeth = "White"
my_hair = "Black"

print "Let's talk about %s." %my_name
print "He's %d cm tall." %my_height
print "He's %d Kg heavy." %my_weight
print "Actually that;s not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(my_age,my_height,my_weight,my_age + my_height + my_weight)
