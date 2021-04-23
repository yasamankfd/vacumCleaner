# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 11:49:54 2021

@author: yas
"""
class room :
    def __init__(self , status):
        self.status  = status
    
class Cleaner :
    def __init__(self , position):
        self.position = position

        
print("program started . . .")
room_a = room( input("enter status for room a : "))
room_b = room( input("enter status for room b : "))
cleaner =  Cleaner( int(input("input cleaners position : ")))
price = 0
i=0
while not ( room_a.status == "clean" and room_b.status == "clean") :
   
    price += 1
    if cleaner.position == 0 and room_a.status == "dirty" :
        print("suck room a")
        room_a.status = "clean"
    elif cleaner.position == 0 and room_a.status == "clean" and room_b.status == "dirty" :
        print("right")
        cleaner.position = 1
    elif cleaner.position == 1 and room_b.status == "dirty" :
        print("suck room b")
        room_b.status = "clean"
    elif cleaner.position == 1 and room_b.status == "clean" and room_a.status == "dirty":
        print("left")
        cleaner.position = 0
print ("price for actions : " + str(price) )            
s = input()