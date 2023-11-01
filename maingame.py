import pygame
from pygame.locals import *
import time
import random
from random import randrange
import math
from math import sin
from math import cos
import keyboard
import sys
import termcolor2
import colorama
colorama.init()

pygame.init()
width = 1240
height = 1000

white = (255, 255, 255)
blue = (173, 216, 230)
black = (0, 0, 0)
red = (255, 0, 0)
begin = True

class Movement():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.last_movement = None
        self.collide = False
        self.coin1 = True
        self.coin2 = True
        self.coin3 = True
        self.coin4 = True
        self.coin5 = True
    def initialise (self):
        char = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Pictures\\knight.png")
        screen.blit(char, (self.x, self.y))
        self.collide = False
    def lastMovement(self, movement):
        self.last_movement = movement
        return self.last_movement
    def check_movement(self):
        return self.last_movement
    def get_pos (self):
        return self.x, self.y
    def change_x (self, value):
        self.x = value
        return self.x
    def movement (self, direction):
        if direction == 'd':
            self.x += 3.5
        elif direction == 's':
            self.y += 3.5
        elif direction == 'w':
            self.y -= 3.5
        elif direction == 'a':
            self.x -= 3.5
        return self.x, self.y
    def border_Forest (self, room, blue):
        if self.x <= -0:
            room.move_area("Bonus")
        if self.x >= 1100:
            room.move_area("Village")
        if self.y <= 630:
            self.y += 3.5
        if self.y >= 700:
            self.y -=3.5
        return self.x, self.y
    def border_Bonus (self, room, blue):
        if self.x <= -0:
            self.x += 3.5
        if self.x >= 1100:
            room.move_area("Forest")
        if self.y <= 630:
            self.y += 3.5
        if self.y >= 700:
            self.y -=3.5
        return self.x, self.y 
    def border_Village (self, room, bg2, npc_1, npc_2, npc_3, npc_4):
        if self.x <= 50:
            position = Movement(150, 680)
            room.move_area("Forest")
        if self.x >= 1100:
            self.x -=3.5
        if self.y <= 200:
            self.y += 3.5
        if self.y >= 700:
            self.y -= 3.5
        return self.x, self.y
    def border_Npc(self, npc_x, npc_y, width, height, house_x, house_y, h_width, h_height, number):
        char = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Pictures\\knight.png")
        charRect = pygame.Rect(self.x, self.y + 50, 100, 100)
        npcRect = pygame.Rect(npc_x, npc_y, width, height)
        houseRect = pygame.Rect(house_x, house_y, h_width, h_height)
        if charRect.colliderect(npcRect):
            if self.y >= npc_y:
                if self.x <= npc_x + width:
                    if self.x >= npc_x :
                        self.y += 3.5
                        traveller.move_down()
                        store.move_down()
                        npc_1.move_down()
                        npc_2.move_down()
                        npc_3.move_down()
                        npc_4.move_down()
                
            if self.y <= npc_y + height:
                if self.x <= npc_x + width:
                    if self.x >= npc_x:
                        self.x += 3.5
                
        elif charRect.colliderect(house_x, house_y, h_width, h_height):
            if self.last_movement == 'd':
                self.x -= 3.5
                
            if self.y <= house_y + h_height:
                if self.x <= house_x + h_width:
                    if self.x >= house_x - 45:
                        self.y -= 3.5
                        traveller.move_up()
                        store.move_up()
                        npc_1.move_up()
                        npc_2.move_up()
                        npc_3.move_up()
                        npc_4.move_up()

            if self.y >= house_y - 100:
                if self.x <= house_x + h_width:
                    if self.x >= house_x - 45:
                        collide = True
                        if number == 1:
                            npc_1.speak("You want to come into my house? Okay!")
                            while collide == True:
                                house = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\inside_house.png")
                                house_change = pygame.transform.scale(house, (1240, 1000))
                                screen.blit(house_change, (0,0))
                                leave_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave_room.png")
                                leave_room_change = pygame.transform.scale(leave_room, (200, 100))
                                screen.blit(leave_room_change, (30, 600))
                                if first_room.visited() == True:
                                    if self.coin1 == True:
                                        money = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\goldCoin6.png")
                                        money_change = pygame.transform.scale(money, (100, 100))
                                        screen.blit(money_change, (400, 500))
                                    if self.coin5 == True:
                                        money2 = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\goldCoin6.png")
                                        money2_change = pygame.transform.scale(money2, (100, 100))
                                        screen.blit(money2_change, (700, 500))
                                pygame.display.flip()
                                time.sleep(0.005)
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = event.pos
                                        if pygame.Rect(30, 600, 200, 100).collidepoint(x, y):
                                            collide = False
                                            self.x = 100
                                            self.coin1 = True
                                            return self.x, self.coin1
                                        if pygame.Rect(400, 500, 50, 50):
                                            if self.coin1 == True:
                                                self.coin1 = False
                                                narrator("You got 1 gold coin!", 2)
                                                balance.add_money(1)
                                        if pygame.Rect(700, 500, 50, 50):
                                            if self.coin5 == True:
                                                self.coin5 = False
                                                narrator("You got 1 gold coin!", 2)
                                                balance.add_money(1)
                                    if event.type == pygame.QUIT:
                                        import Start_Game
                                        
                        if number == 2:
                            npc_2.speak("You want to come IN? Well, of course you do!")
                            while collide == True:
                                house = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\inside_house4.png")
                                house_change = pygame.transform.scale(house, (1240, 1000))
                                screen.blit(house_change, (0,0))
                                leave_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave_room.png")
                                leave_room_change = pygame.transform.scale(leave_room, (200, 100))
                                screen.blit(leave_room_change, (30, 600))
                                if first_room.visited() == True:
                                    if self.coin2 == True:
                                        money = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\goldCoin6.png")
                                        money_change = pygame.transform.scale(money, (100, 100))
                                        screen.blit(money_change, (600, 200))
                                pygame.display.flip()
                                time.sleep(0.005)
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = event.pos
                                        if pygame.Rect(30, 600, 200, 100).collidepoint(x, y):
                                            collide = False
                                            self.x = 100
                                            return self.x
                                        if pygame.Rect(600, 200, 100, 100):
                                            if self.coin2 == True:
                                                self.coin2 = False
                                                narrator("You got 1 gold coin!", 2)
                                                balance.add_money(1)
                                    if event.type == pygame.QUIT:
                                        import Start_Game
                                        
                        if number == 4:
                            npc_4.speak("Fine. Go in.")
                            while collide == True:
                                house = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\inside_house2.png")
                                house_change = pygame.transform.scale(house, (1240, 1000))
                                screen.blit(house_change, (0,0))
                                leave_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave_room.png")
                                leave_room_change = pygame.transform.scale(leave_room, (200, 100))
                                screen.blit(leave_room_change, (30, 600))
                                if first_room.visited() == True:
                                    if self.coin3 == True:
                                        money = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\goldCoin6.png")
                                        money_change = pygame.transform.scale(money, (100, 100))
                                        screen.blit(money_change, (600, 700))
                                pygame.display.flip()
                                time.sleep(0.005)
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = event.pos
                                        if pygame.Rect(30, 600, 200, 100).collidepoint(x, y):
                                            collide = False
                                            self.x = 100
                                            return self.x
                                        if pygame.Rect(600, 700, 100, 100):
                                            if self.coin3 == True:
                                                self.coin3 = False
                                                narrator("You got 1 gold coin!", 2)
                                                balance.add_money(1)
                                    if event.type == pygame.QUIT:
                                        import Start_Game
                                        
                        if number == 3:
                            npc_3.speak("You want to look at m-my house?! Sure...")
                            while collide == True:
                                house = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\inside_house3.png")
                                house_change = pygame.transform.scale(house, (1240, 1000))
                                screen.blit(house_change, (0,0))
                                leave_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave_room.png")
                                leave_room_change = pygame.transform.scale(leave_room, (200, 100))
                                screen.blit(leave_room_change, (30, 600))
                                if first_room.visited() == True:
                                    if self.coin4 == True:
                                        money = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\goldCoin6.png")
                                        money_change = pygame.transform.scale(money, (100, 100))
                                        screen.blit(money_change, (800, 300))
                                pygame.display.flip()
                                time.sleep(0.005)
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        x, y = event.pos
                                        if pygame.Rect(30, 600, 200, 100).collidepoint(x, y):
                                            collide = False
                                            self.x = 100
                                            return self.x
                                        if pygame.Rect(800, 300, 100, 100):
                                            if self.coin4 == True:
                                                self.coin4 = False
                                                narrator("You got 1 gold coin!", 2)
                                                balance.add_money(1)
                                    if event.type == pygame.QUIT:
                                        import Start_Game
                                        

    def border_Portal(self, portal, room, Portal):
        char = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Pictures\\knight.png")
        charRect = pygame.Rect(self.x, self.y, *char.get_size())
        portalRect = pygame.Rect(1100, 700, *portal.get_size())
        if charRect.colliderect(portalRect):
            if self.y >= 650:
                if fourth_room.visited() == True:
                    if inventory.check_item("Magical sword") == True:
                        if inventory.check_item("Shield of great power") == True:
                            room.move_area(Portal.check_room())
                            position2.change_x(300)
                        else:
                            narrator("You need to buy a shield to pass!", 3)
                    else:
                        narrator("You need to buy a sword to pass!", 3)
                else:
                    room.move_area(Portal.check_room())
                    position2.change_x(300)

    def border_Shop(self, store, room):
        char = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Pictures\\knight.png")
        charRect = pygame.Rect(self.x, self.y, *char.get_size())
        shopRect = pygame.Rect(store.get_x(), store.get_y(), 200, 200)
        if charRect.colliderect(shopRect):
            room.move_area("shop")


class Inventory:
    def __init__(self, path, number):
        self.item_list = []
        self.item_paths = []
        self.path = path
        self.number = number
        
    def add_item(self, name, path):
        self.item_list.append(name)
        self.item_paths.append(path)

    def remove_item(self, name, path):
        self.item_list.remove(name)
        self.item_paths.remove(path)

    def check_item(self, name):
        if name in self.item_list:
            return True
        else:
            return False

    def get_length(self):
        return len(self.item_list)
        
    def get_list(self, number):
        return self.item_list[number]

    def get_path (self, number):
        return self.item_paths[number]
            
    def open(self):
        closed = False
        while closed == False:
            itemscreen = pygame.image.load(self.path)
            itemscreen_change = pygame.transform.scale(itemscreen, (700, 500))
            screen.blit(itemscreen_change, (250, 250))
            item_num = len(self.item_list)
            j = 0
            if item_num >= 7:
                for i in range (0, 6):
                    inventory_item = pygame.image.load(self.item_paths[i])
                    inventory_item_change = pygame.transform.scale(inventory_item, (50, 50))
                    screen.blit(inventory_item_change, (300 + 115*i, 320))
                for i in range (6, item_num):
                    inventory_item = pygame.image.load(self.item_paths[i])
                    inventory_item_change = pygame.transform.scale(inventory_item, (50, 50))
                    screen.blit(inventory_item_change, (300 + 115*j, 390))
                    j +=1
                    
            elif item_num >= 1:
                for i in range (0, item_num):
                    inventory_item = pygame.image.load(self.item_paths[i])
                    inventory_item_change = pygame.transform.scale(inventory_item, (50, 50))
                    screen.blit(inventory_item_change, (300 + 115*i, 320))
                    
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                closed = True
            pygame.display.flip()
            time.sleep(0.005)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.number == 1:
                        x, y = event.pos
                        answer = True
                        if pygame.Rect(300, 320, 50, 50).collidepoint(x, y):
                            narrator("Flowers: 5 gold coins.", 3)
                            amount = 5
                            position = 0
                            answer = False
                        if pygame.Rect(415, 320, 50, 50).collidepoint(x, y):
                            narrator("Magical sword: 100 gold coins.", 3)
                            amount = 100
                            position = 1
                            answer = False
                        if pygame.Rect(300 + 115*2, 320, 50, 50).collidepoint(x, y):
                            narrator("Mystical shield: 50 gold coins.", 3)
                            amount = 50
                            position = 2
                            answer = False
                        while answer == False:
                            narrator("Buy? (Type either Y or N)", 0)
                            if keyboard.is_pressed("Y"):
                                if int(balance.check_money()) >= amount:
                                    narrator("You have purchased this item! I can buy food for my family!", 3)
                                    balance.remove_money(amount)
                                    inventory.add_item(self.item_list[position], self.item_paths[position])
                                    answer = True
                                    closed = True
                                else:
                                    narrator("You don't have enough money and you are wasting my time.", 3)
                                    answer = True
                                    closed = True
                            if keyboard.is_pressed("N"):
                                narrator("You have not purchased this item. Get out of my shop.", 3)
                                answer = True
                                closed = True
                if event.type == pygame.QUIT:
                    import Start_Game

class Money():
    def __init__ (self):
        self.money = 0
    def add_money (self, amount):
        self.money = self.money + amount
        return self.money
    def remove_money (self, amount):
        self.money = self.money - amount
        return self.money
    def check_money (self):
        return self.money
        
        
class Area():
    def __init__ (self, area):
        self.area = area
    def move_area(self, new_area):
        self.area = new_area
        return self.area
    def check_area (self):
        return self.area

class Npc():
    def __init__(self, path, x, y, number):
        self.path = path
        self.x = x
        self.y = y
        self.house_x = self.x - 300
        self.house_y = self.y - 100
        self.char_code = None
        self.charRect = None
        self.number = number
    def set_char_code (self, char_code):
        self.char_code = char_code
        return self.char_code
    def check_char_code (self):
        if self.char_code == "????":
            return False
        else:
            return True
    def get_pos(self):
        return self.x, self.y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_rect(self):
        return self.charRect  
    def create(self, x_change, y_change, position):
        char = pygame.image.load(self.path)
        char_change = pygame.transform.scale(char,(x_change, y_change))
        char_height = y_change
        char_width = x_change
        self.charRect = char_change.get_rect()
        screen.blit(char_change, (self.x, self.y))
        house = pygame.image.load("C:\\Users\\abbyn\\Downloads\\house.png")
        house_larger = pygame.transform.scale(house,(250, 200))
        house_height = 200
        house_width = 250
        position2.border_Npc(self.x, self.y, char_width, char_height, self.house_x, self.house_y, house_width, house_height, self.number)
        screen.blit(house_larger, (self.house_x, self.house_y))
        return self.charRect
    def speak(self, speech):
        textbox = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\textbox.png")
        textbox_adjust = pygame.transform.scale(textbox, (800, 100))
        screen.blit(textbox_adjust, (200, 710))
        font = pygame.font.SysFont("Century", 15)
        name_font = pygame.font.SysFont("Century", 25)
        text = font.render(speech, True, white)
        name = name_font.render(self.char_code, True, white)
        nameRect = name.get_rect()
        nameRect.center = (600, 730)
        screen.blit(name, nameRect)
        textRect = text.get_rect()
        textRect.center = (600, 760)
        screen.blit(text, textRect)
        pygame.display.flip()
        time.sleep(3)
        
    def move_up(self):
        self.y += 3.5
        self.house_y += 3.5
        return self.y, self.house_y
    def move_down(self):
        self.y -=3.5
        self.house_y -= 3.5
        return self.y, self.house_y

def narrator(speech, seconds):
    textbox = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\textbox.png")
    textbox_adjust = pygame.transform.scale(textbox, (800, 100))
    screen.blit(textbox_adjust, (200, 710))
    font = pygame.font.SysFont("Century", 15)
    text = font.render(speech, True, white)
    textRect = text.get_rect()
    textRect.center = (600, 760)
    screen.blit(text, textRect)
    pygame.display.flip()
    time.sleep(seconds)

class CoreValues():
    def __init__(self):
        self.values = []
        self.points = []
        self.highestvalue = 0
        
    def add_value(self, value, number):
        self.values.append(value)
        self.points.append(number)

    def get_length(self):
        return len(self.values)

    def get_item(self, number):
        return self.values[number]

    def highest_value(self):
        if len(self.points) == 0:
            return self.highestvalue
        if len(self.points) == 1:
            self.highestvalue = self.values[0]
            return self.highestvalue
        else:
            for i in range (0, len(self.points)- 1):
                if self.points[i] > self.points[i + 1]:
                    self.highestvalue = self.values[i]
                else:
                    self.highestvalue = self.values[i+1]
                i = i + 1
            return self.highestvalue

class CompareValues():
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
        self.first_counter = 0
        self.second_counter = 0

    def add_points(self, value, number):
        if value == self.first_value:
            self.first_counter += number
        if value == self.second_value:
            self.second_counter += number
        return self.first_counter, self.second_value

    def check_equal(self):
        if self.first_counter == self.second_counter:
            return True
        else:
            return False
            
    def winning_value(self):
        if self.first_counter > self.second_counter:
            corevalues.add_value(self.first_value, self.first_counter)
        if self.second_counter > self.first_counter:
            corevalues.add_value(self.second_value, self.second_counter)

    
class Object():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def move_up(self):
        self.y += 3.5
        return self.y
    def move_down(self):
        self.y -=3.5
        return self.y

class Quests():
    def __init__(self, quest_name, quest_description, quest_giver):
        self.quest_name = quest_name
        self.quest_description = quest_description
        self.quest_giver = quest_giver
        self.given = False
    def set_given(self, questBook):
        self.given = True
        questBook.add_quest(self.quest_name, self.quest_description)
        return self.given
    def check_given (self):
        return self.given

class QuestBook():
    def __init__(self):
        self.quests = None
        self.quest_list = []
        self.quest_description = []
        self.font = pygame.font.SysFont("Century", 20, bold=True)
    def add_quest(self, name, description):
        self.quests = ''
        self.quest_list.append(name)
        self.quest_description.append(description)
        return self.quests, self.quest_list, self.quest_description
    def remove_quest (self, name, description):
        self.quests = None
        self.quest_list.remove(name)
        self.quest_description.remove(description)
        return self.quest_list, self.quest_description
    def check(self):
        return self.quests
    def check_number(self):
        if self.quests == None:
            return True
        else:
            return False
    def display(self, room):
        room.move_area("questbook")
    def display_quests(self):
        start_value = 600
        quest = self.font.render(self.quest_list[0], True, black)
        questRect = quest.get_rect()
        questRect.center = (start_value, 300)
        description = self.font.render(self.quest_description[0], True, black)
        descriptionRect = description.get_rect()
        descriptionRect.center = (start_value, 500)
        screen.blit(quest, questRect)
        screen.blit(description, descriptionRect)

class Screen():
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    def check_width (self):
        return self.width
    def check_height (self):
        return self.height
    def change_width (self):
        self.width +=20
        return self.width

class Portal():
    def __init__(self, room):
        self.room = room
    def change_room (self, room_to_change):
        self.room = room_to_change
        #set this in every portal room so room changed when at village
    def check_room (self):
        return self.room

class Text():
    def __init__(self, writing, center_x, center_y):
        self.writing = writing
        self.center_x = center_x
        self.center_y = center_y
    def display(self, colour):
        self.text = font.render(self.writing, True, colour)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.center_x, self.center_y)
        screen.blit(self.text, self.textRect)
        pygame.display.flip()

class Arc():
    def __init__ (self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.radius = 0.5
        self.angle = randrange(1, 50, 15)
    def move(self):
        self.x = self.x + cos(self.angle) * self.radius
        self.y = self.y + sin(self.angle) * self.radius
    def get_x (self):
        return self.x
    def get_y(self):
        return self.y
    

class Room1():
    def __init__(self):
        self.time = True
        self.end = False
    def check_time (self):
        return self.time
    def check_end(self):
        return self.end
    def visited (self):
        if self.time == False:
            return True
        else:
            return False
    def dialogue (self, room, position2):
        font = pygame.font.SysFont("Century", 25)
        first = Text("Hello again. Remember me?", 620, 330)
        first.display(red)
        time.sleep(2)
        second = Text("Your friendly little voice in your head.", 620, 370)
        second.display(red)
        time.sleep(4)
        third = Text("Your advisor.", 620, 410)
        third.display(red)
        time.sleep(2)
        fourth = Text("Your friend.", 620, 450)
        fourth.display(red)
        time.sleep(3)
        third = Text("Or am I?", 620, 490)
        third.display(red)
        time.sleep(2)
        screen.fill(black)
        question = False
        while question == False:
            question1 = Text("(1) Who are you?", 500, 440)
            question1.display(red)
            question2 = Text("(2) Do I know you?", 800, 440)
            question2.display(red)
            narrator("Press the number in front of the question you'd like to ask.", 0)
            if keyboard.is_pressed("1"):
                screen.fill(black)
                answer = Text("I'm in your head. Just like you.", 620, 500)
                answer.display(red)
                pygame.display.flip()
                time.sleep(3)
                question = True
            elif keyboard.is_pressed("2"):
                screen.fill(black)
                answer = Text("Oh, you know me. We're great friends.", 620, 500)
                answer.display(red)
                pygame.display.flip()
                time.sleep(3)
                question = True
        room.move_area("Village")
        position2.change_x(300)
        self.time = False
        return self.time
    def change_end(self):
        self.end = True
        return self.end

class Room2():
    def __init__(self):
        self.time = True
        self.end = False
    def check_time (self):
        return self.time
    def check_end(self):
        return self.end
    def visited (self):
        if self.time == False:
            return True
        else:
            return False
    def dialogue (self, room, position2):
        choice1 = False
        comparisonA = CompareValues("Impulse", "Cautious")
        area1 = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\city_area.jpg")
        area1_change = pygame.transform.scale(area1, (width, height))
        screen.blit(area1_change, (0, 0))
        scared_man = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\scared_man.png")
        scared_man_change = pygame.transform.scale(scared_man, (200, 200))
        screen.blit(scared_man_change, (width//3, height//2))
        narrator("HELP ME HELP ME PLEASE", 3)
        narrator("Someone's chasing me! Please, help!", 3)
        while choice1 == False:
            narrator("(1) Hide him  (2)Fight   (3) Run away  (4)Run away and call the police", 0)
            if keyboard.is_pressed("1"):
                choice1 = True
                screen.fill(black)
                impact = Text("You hide the scared guy and faintly hear footsteps outside your hiding spot...but the footsteps soon fade.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Impulse", 1)
                time.sleep(3)
            if keyboard.is_pressed("2"):
                choice1 = True
                screen.fill(black)
                impact = Text("You take the attacker head-on, and the element of surprise contributes to your victory.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Impulse", 2)
                time.sleep(3)
            if keyboard.is_pressed("3"):
                choice1 = True
                screen.fill(black)
                impact = Text("You run away, not particularly wanting to do anything to help- in order to save your own skin.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Cautious", 2)
                time.sleep(3)
            if keyboard.is_pressed("4"):
                choice1 = True
                screen.fill(black)
                impact = Text("You run away and call the police. But were you fast enough to save the man?", 620, 320)
                impact.display(white)
                comparisonA.add_points("Cautious", 1)
                time.sleep(3)     
        area2 = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\kitchen.png")
        area2_change = pygame.transform.scale(area2, (width, height))
        screen.fill(black)
        screen.blit(area2_change, (0, 0))
        child = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\little_boy.png")
        child_change = pygame.transform.scale(child, (300, 500))
        screen.blit(child_change, (width//3, 300))
        narrator("I'm back from my friend's house! Guess what?", 3)
        narrator("I got two free concert tickets from some guy on the street! Wanna go?", 3)
        choice2 = False
        while choice2 == False:
            narrator("(1) Yes (2) Go but back out if there's noone else around  (3)No  (4)Check the concert is real", 0)
            if keyboard.is_pressed("1"):
                choice2 = True
                screen.fill(black)
                impact = Text("You go, enthralled by a free concert.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Impulse", 2)
                time.sleep(3)
            if keyboard.is_pressed("2"):
                choice2 = True
                screen.fill(black)
                impact = Text("You go, enthralled by a free concert, but see noone else around..you two run out of there.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Impulse", 1)
                time.sleep(3)
            if keyboard.is_pressed("3"):
                choice2 = True
                screen.fill(black)
                impact = Text("You don't go. A random guy giving out tickets? No thanks.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Cautious", 2)
                time.sleep(3)
            if keyboard.is_pressed("4"):
                choice2 = True
                screen.fill(black)
                impact = Text("You check the concert is real before you go..you don't want to fall into a scam of some kind.", 620, 320)
                impact.display(white)
                comparisonA.add_points("Cautious", 1)
                time.sleep(3)
        if (comparisonA.check_equal()) == True:
            choice3 = False
            time.sleep(3)
            screen.fill(black)
            tie = Text("You and your friends had plans to backpack around Europe- but they've backed out.", 620, 320)
            tie.display(white)
            choice = Text("What will you do?", 620, 360)
            choice.display(white)
            while choice3 == False:
                narrator("(1) Don't go  (2) Go", 0)
                if keyboard.is_pressed("1"):
                    choice3 = True
                    comparisonA.add_points("Cautious", 1)
                if keyboard.is_pressed("2"):
                    choice3 = True
                    comparisonA.add_points("Impulse", 1)
        comparisonA.winning_value()
        room.move_area("Village")
        position2.change_x(300)
        self.time = False
        return self.time
    def change_end(self):
        self.end = True
        return self.end

class Room3():
    def __init__(self):
        self.time = True
        self.end = False
        self.chosen_values = []
    def check_time (self):
        return self.time
    def check_end(self):
        return self.end
    def visited (self):
        if self.time == False:
            return True
        else:
            return False
    def dialogue (self, room, position2):
        screen.fill(black)
        first_scene = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\scene1.png")
        screen.blit(first_scene,(0, 100))
        question = Text("What do you think is happening here?", 920, 500)
        question.display(white)
        choiceA = False
        while choiceA == False:
            answer1 = Text("(1) The girl is upset because of her mother.", 300, 650)
            answer1.display(white)
            answer2 = Text("(2) The girl's brother has done something to anger the woman.", 400, 700)
            answer2.display(white)
            answer3 = Text("(3) The girl's brother is trying to find something for his mother.", 430, 750)
            answer3.display(white)
            if keyboard.is_pressed("1"):
                choiceA = True
                scene_choice = 1
                self.chosen_values.append("Compassion")
            if keyboard.is_pressed("2"):
                choiceA = True
                scene_choice = 2
                self.chosen_values.append("Practicality")
            if keyboard.is_pressed("3"):
                choiceA = True
                scene_choice = 3
                self.chosen_values.append("Loyalty")
        choiceB = False
        screen.fill(black)
        if scene_choice == 1:
            second_scene = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\scene4.png")
            screen.blit(second_scene,(0, 100))
            question = Text("How do you think the story ends?", 920, 500)
            question.display(white)
            time.sleep(3)
            while choiceB == False:
                answer1 = Text("(1) The girl recovers of her own accord.", 300, 650)
                answer1.display(white)
                answer2 = Text("(2) The girl's mother apologises.", 300, 700)
                answer2.display(white)
                answer3 = Text("(3) The girl's brother comes back and the two play a game.", 400, 750)
                answer3.display(white)
                if keyboard.is_pressed("1"):
                    choiceB = True
                    self.chosen_values.append("Autonomy")
                if keyboard.is_pressed("2"):
                    choiceB = True
                    self.chosen_values.append("Kindness")
                if keyboard.is_pressed("3"):
                    choiceB = True
                    self.chosen_values.append("Friendship")
        if scene_choice == 2:
            second_scene = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\scene3.png")
            screen.blit(second_scene,(0, 100))
            question = Text("How do you think the story ends?", 920, 500)
            question.display(white)
            time.sleep(3)
            while choiceB == False:
                answer1 = Text("(1) The boy apologises to his mother.", 300, 650)
                answer1.display(white)
                answer2 = Text("(2) The boy decides to take a walk to calm down.", 350, 700)
                answer2.display(white)
                answer3 = Text("(3) The boy doesn't speak to his mother at all.", 350, 750)
                answer3.display(white)
                if keyboard.is_pressed("1"):
                    choiceB = True
                    self.chosen_values.append("Faith")
                if keyboard.is_pressed("2"):
                    choiceB = True
                    self.chosen_values.append("Growth")
                if keyboard.is_pressed("3"):
                    choiceB = True
                    self.chosen_values.append("Boldness")
        if scene_choice == 3:
            second_scene = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\scene2.png")
            screen.blit(second_scene,(0, 100))
            impact = Text("The boy finds the item.", 920, 500)
            impact.display(white)
            question = Text("How do you think the story ends?", 920, 540)
            question.display(white)
            time.sleep(3)
            while choiceB == False:
                answer1 = Text("(1) The boy's mother feels better.", 300, 650)
                answer1.display(white)
                answer2 = Text("(2) His sister has already found the item.", 330, 700)
                answer2.display(white)
                answer3 = Text("(3) The boy makes a joke about the whole situation.", 360, 750)
                answer3.display(white)
                if keyboard.is_pressed("1"):
                    choiceB = True
                    self.chosen_values.append("Achievement")
                if keyboard.is_pressed("2"):
                    choiceB = True
                    self.chosen_values.append("Trustfulness")
                if keyboard.is_pressed("3"):
                    choiceB = True
                    self.chosen_values.append("Humour")
        for i in range (0, len(self.chosen_values)):
            screen.fill(black)
            time.sleep(2)
            value = Text(self.chosen_values[i], 620, 360)
            value.display(white)
            choice = Text("How important is this value to you?", 620, 410)
            choice.display(white)
            pick = False
            time.sleep(3)
            while pick == False:
                narrator("(1)Very important (2)Important (3)Not so important (4)Not at all important", 0)
                if keyboard.is_pressed("1"):
                    pick = True
                    corevalues.add_value(self.chosen_values[i], 4)
                if keyboard.is_pressed("2"):
                    pick = True
                    corevalues.add_value(self.chosen_values[i], 3)
                if keyboard.is_pressed("3"):
                    pick = True
                    corevalues.add_value(self.chosen_values[i], 2)
                if keyboard.is_pressed("4"):
                    pick = True
                    corevalues.add_value(self.chosen_values[i], 1)
            i +=1
        room.move_area("Village")
        position2.change_x(300)
        self.time = False
        return self.time, self.chosen_values
    def change_end(self):
        self.end = True
        return self.end

class Room4():
    def __init__(self):
        self.time = True
    def is_visited(self):
        self.time = False
        return self.time
    def visited (self):
        if self.time == False:
            return True
        else:
            return False

class Room5():
    def __init__(self):
        self.time = True
    def is_visited(self):
        self.time = False
        return self.time
    def visited (self):
        if self.time == False:
            return True
        else:
            return False
        

position = Movement(150, 680)
position2 = Movement(150, 680)
position3 = Movement(1050, 680)
position4 = Movement(150, 680)
balance = Money()
corevalues = CoreValues()
room = Area("Forest")
npc_1 = Npc("C:\\Users\\abbyn\\Downloads\\npc_1.png", 650, 580, 1)#village leader? they are basically whatever trait is your strongest atm
npc_1.set_char_code("????")
npc_2 = Npc("C:\\Users\\abbyn\\Downloads\\npc_2.png", 500, 200, 2)#fighting battles...maybe creativity? Could go for
npc_2.set_char_code("????")
npc_3 = Npc("C:\\Users\\abbyn\\Downloads\\ghost.png", 800, 100, 3)#embodiment of fear, probably? (low-hanging fruit I know, can't resist)
npc_3.set_char_code("????")
npc_4 = Npc("C:\\Users\\abbyn\\Downloads\\redman.png", 1000, 400, 4)#..gotta be anger, I can't not do that, and now this is Inside, perfect
npc_4.set_char_code("????")
inventory = Inventory("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\inventory_gui.png", 0)
store_menu = Inventory("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\store_menu.jpg", 1)
store_menu.add_item("Flowers", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\flowers.png")
store_menu.add_item("Magical sword", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\sword.png")
store_menu.add_item("Shield of great power", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\shield.png")
traveller = Object(1100, 700)
store = Object(150, -400)
Portal = Portal("room1")
comparisonA = CompareValues("Impulse", "Cautious")
sunny = Arc(200, 250)
font = pygame.font.SysFont("Century", 20, bold=True)
questBook = QuestBook()
said = False
said2 = False
said3 = False
said4 = False
said5 = False
said6 = False
said7 = False
said8 = False
said9 = False
friend = False
used1 = False
used2 = False
used3 = False
inventory_items = []
numbers = []
chosen_values = []
health = 50
quest1 = Quests("Flowers from the store", "Go to the shop directly north and buy the flowers for the knight.", "Sir Roman")
quest2 = Quests("Picture from the sad room", "Go left of the forest and click on the picture.", "Timor")
quest3 = Quests("Collect parcel", "Go to the village leader and collect the knight's parcel.", "Sir Roman")
quest4 = Quests("Yell at shopkeeper", "Go to the shopkeeper and yell at him.", "Kaen")
quest5 = Quests("Smile at shopkeeper", "Go to the shopkeeper and smile at him.", "Kaen")
main_theme = pygame.mixer.Sound("music_zapsplat_game_music_zen_calm_soft_arpeggios_013.mp3")
pygame.mixer.music.load("music_zapsplat_game_music_zen_calm_soft_arpeggios_013.mp3")
main_theme.set_volume(0.04)
main_theme.play(-1)
scary = pygame.mixer.Sound("scary.mp3")
pygame.mixer.music.load("scary.mp3")
scary.set_volume(0)
scary.play(-1)
sad = pygame.mixer.Sound("music_zapsplat_darkest_hours.mp3")
sad.set_volume(0)
sad.play(-1)
trust = False
fire_trust = False
picture_seen = False
parcel = False
complete = False
complete1 = False
complete2 = False
complete3 = False
first_room = Room1()
second_room = Room2()
third_room = Room3()
fourth_room = Room4()
running = True

while (running):
    while (room.check_area() == "Forest"):
        sad.set_volume(0)
        scary.set_volume(0)
        main_theme.set_volume(0.04)
        bg = Screen(width, height)
        screen = pygame.display.set_mode((bg.check_width(), bg.check_height()))
        screen.fill(blue)
        #also at end of game traits are listed on screen during credits and the such
        sun = pygame.image.load("C:\\Users\\abbyn\Downloads\\sun_shiny.png")
        screen.blit(sun, (sunny.get_x(),sunny.get_y()))
        grass = pygame.image.load("C:\\Users\\abbyn\\Downloads\\Grass Texture 1.jpg")
        for i in range (0, 1300, 20):
            for j in range (0, 300, 20):
                screen.blit(grass, (i, j + 650))
        tree = pygame.image.load("C:\\Users\\abbyn\\Downloads\\stendhal_trees-7e096de\\PNG\\32x32\\pine_tree_1.png")
        tree_big = pygame.transform.scale(tree,(200, 300))
        for i in range (0, 1100, 100):
            screen.blit(tree_big, (i, 450))
        sign = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\sign.png")
        sign_small = pygame.transform.scale(sign, (100, 100))
        screen.blit(sign_small, (800, 630))
        position.initialise()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            position.movement('a')
            sunny.move()
        if keys[pygame.K_w]:
            position.movement('w')
        if keys[pygame.K_s]:
            position.movement('s')
        if keys[pygame.K_d]:
            position.movement('d')
            sunny.move()
        if keys[pygame.K_SPACE]:
            inventory.open()
        position.border_Forest(room, blue)
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "Village"):
        sunny = Arc(200, 250)
        main_theme.set_volume(0.04)
        scary.set_volume(0)
        sad.set_volume(0)
        bg2 = Screen(width, height)
        screen = pygame.display.set_mode((bg2.check_width(), bg2.check_height()))
        screen.fill(blue)
        if (corevalues.highest_value() != 0):
            npc_1.set_char_code(corevalues.highest_value())
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            position2.movement('a')
            position2.lastMovement('a')
        if keys[pygame.K_w]:
            position2.movement('w')
            position2.lastMovement('w')
            npc_1.move_up()
            npc_2.move_up()
            npc_3.move_up()
            npc_4.move_up()
            traveller.move_up()
            store.move_up()
        if keys[pygame.K_s]:
            position2.movement('s')
            position2.lastMovement('s')
            traveller.move_down()
            store.move_down()
            npc_1.move_down()
            npc_2.move_down()
            npc_3.move_down()
            npc_4.move_down()
        if keys[pygame.K_d]:
            position2.movement('d')
            position2.lastMovement('d')
        for i in range (0, width, 20):
            for j in range (0, height, 20):
                screen.blit(grass, (i, j))
        npc_1.create(60, 90, position2)
        n1_rect = npc_1.get_rect()
        npc_2.create(80, 110, position2)
        n2_rect = npc_2.get_rect()
        if fourth_room.visited() == False:
            npc_3.create(80, 100, position2)
            n3_rect = npc_3.get_rect()
        npc_4.create(80, 110, position2)
        n4_rect = npc_4.get_rect()
        portal = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\teleport.png")
        screen.blit(portal, (traveller.get_x(), traveller.get_y()))
        shop = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\Shop.png")
        shop_larger = pygame.transform.scale(shop, (200, 200))
        screen.blit(shop_larger, (store.get_x(), store.get_y()))
        quest_book = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\quest_book.png")
        quest_book_smaller = pygame.transform.scale(quest_book, (90, 100))
        screen.blit(quest_book_smaller, (20,710))
        pause_icon = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\pause.png")
        screen.blit(pause_icon, (0, 150))
        help_icon = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\help.png")
        help_icon_small = pygame.transform.scale(help_icon, (70, 70))
        screen.blit(help_icon_small, (100, 150))
        coin_icon = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\coin_icon.png")
        coin_icon_change = pygame.transform.scale(coin_icon, (70, 70))
        screen.blit(coin_icon_change, (1000, 150))
        guide = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\guide.png")
        guide_change = pygame.transform.scale(guide, (70, 70))
        screen.blit(guide_change, (1100, 150))
        position2.border_Portal(portal, room, Portal)
        position2.initialise()
        position2.border_Village(room, bg2, npc_1, npc_2, npc_3, npc_4)
        position2.border_Shop(store, room)
        if keys[pygame.K_SPACE]:
            inventory.open()
        pygame.display.flip()
        if first_room.visited() == True:
            if first_room.check_end() == False:
                narrator("Hold off on going into that portal again.", 3)
                narrator("I think there needs to be a little explanation about what exactly is going on here.", 3)
                narrator("I am your real guide.", 2)
                narrator("That voice back there isn't someone you'd want to let into your head.", 3)
                narrator("However, I don't believe you had a choice.", 2)
                narrator("These portal rooms help you understand yourself better.", 3)
                narrator("But I suggest you wait until you've talked to the people in the village after every room.", 4)
                narrator("You'll miss out on key parts of the story if you choose to move on.", 3)
                narrator("But, as always, you are in control here. I can only provide suggestions.", 3)
                narrator("I suggest you now talk to the village leader (the one in green).", 3)
                narrator("Good luck. You may need it.", 2)
                first_room.change_end()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(0, 150, 100, 100).collidepoint(x, y):
                    room.move_area("pause")
                if pygame.Rect(100, 150, 70, 70).collidepoint(x, y):
                    room.move_area("help")
                if pygame.Rect(1000, 150, 70, 70).collidepoint(x, y):
                    room.move_area("coin")
                if pygame.Rect(1100, 150, 70, 70).collidepoint(x, y):
                    room.move_area("guide")
                if pygame.Rect(20, 710, 90, 100).collidepoint(x, y):
                    questBook.display(room)
                if pygame.Rect(npc_1.get_x(), npc_1.get_y(), 60, 90).collidepoint(x, y):
                    if fourth_room.visited() == True:
                        if said6 == True:
                            npc_1.speak("You already got 15 coins from me, you're not getting any more!")
                        else:
                            npc_1.speak("Hello again!")
                            npc_1.speak("Wanna try another puzzle?")
                            question = False
                            while question == False:
                                narrator("(1) Where's Timor?  (2)Yes  (3)No", 0)
                                if keyboard.is_pressed("2") and said6 == False:
                                    riddle = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\riddle.jpg")
                                    riddle_change = pygame.transform.scale(riddle, (500, 400))
                                    screen.blit(riddle_change, (100, 200))
                                    pygame.display.flip()
                                    answer = "easter eggs"
                                    question2 = False
                                    while question2 == False:
                                        narrator("Type out your answer.", 0)
                                        for i in range (0, len(answer)):
                                            if keyboard.is_pressed(answer[i]):
                                                i +=1
                                        question2 = True
                                    npc_1.speak("Congrats, you completed the puzzle! Here you go.")
                                    balance.add_money(10)
                                    question = True
                                    complete3 = True
                                    if complete1 == True:
                                        if complete2 == True:
                                            if complete3 == True:
                                                corevalues.add_value("Logic", 3)
                                    said6= True
                                    narrator("You got 10 gold coins!", 2)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_1.speak("Timor?")
                                    npc_1.speak("I don't think I've heard that name.")
                                if keyboard.is_pressed("3"):
                                    question = True
                                    npc_1.speak("That's okay!")
                                    npc_1.speak("Come back if you want to try again.")
                                
                    elif third_room.visited() == True:
                        if (quest3.check_given() == True and said3 == False):
                            npc_1.speak("You want a parcel for Sir Roman?")
                            npc_1.speak("Here you go!")
                            narrator("You have acquired Sir Roman's parcel.", 4)
                            inventory.add_item("Parcel", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\parcel.png")
                            parcel = True
                        elif said5 == True:
                            npc_1.speak("You already got 15 coins from me, you're not getting any more!")
                        else:
                            npc_1.speak("Hello again!")
                            npc_1.speak("Wanna try another puzzle?")
                            question = False
                            while question == False:
                                narrator("(1) Yes  (2) No", 0)
                                if keyboard.is_pressed("1") and said5 == False:
                                    question = True
                                    mouse_puzzle = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\mouse_puzzle.gif")
                                    mouse_puzzle_change = pygame.transform.scale(mouse_puzzle, (500, 400))
                                    screen.blit(mouse_puzzle_change, (100, 200))
                                    pygame.display.flip()
                                    narrator("How many pieces of cheese can the mouse get?", 7)
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1) Two  (2) Three (3) Four  (4) Five (5) Six", 0)
                                        if keyboard.is_pressed("4"):
                                            question2 = True
                                            npc_1.speak("Congrats, you completed the puzzle! Here you go.")
                                            balance.add_money(10)
                                            said5 = True
                                            complete2 = True
                                            narrator("You got 10 gold coins!", 2)
                                        if keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("3") or keyboard.is_pressed("5"):
                                            npc_1.speak("Sorry, that's incorrect!")
                                if keyboard.is_pressed("2"):
                                    question = True
                                    npc_1.speak("Okay!")
                                    npc_1.speak("Come back later if you want to try!")
                                
                    elif second_room.visited() == True:
                        if said4 == True:
                            npc_1.speak("You already got 15 coins from me, you're not getting any more!")
                        else:
                            npc_1.speak("Welcome back, village hero!")
                            npc_1.speak("You know my name now? Wonderful! I'm glad.")
                            npc_1.speak("Names are a strange thing for me. They can often change, if I'm not careful.")
                            npc_1.speak("Now, to business! I have a puzzle for you!")
                            npc_1.speak("Would you like to give it a try? There's gold in it for you!")
                            question = False
                            while question == False:
                                narrator("Would you like to try the puzzle? (1) Yes  (2) No", 0)
                                if keyboard.is_pressed("1") and said4 == False:
                                    question = True
                                    logic_puzzle = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\logic_puzzle.jpg")
                                    logic_puzzle_change = pygame.transform.scale(logic_puzzle, (500, 400))
                                    screen.blit(logic_puzzle_change, (100, 200))
                                    hints = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\hints.jpg")
                                    hints_change = pygame.transform.scale(hints, (400, 400))
                                    screen.blit(hints_change, (700, 200))
                                    pygame.display.flip()
                                    narrator("Figure out which options are linked together- each option is used only once. Good luck!", 6)
                                    names = ['Lindsay', 'Sam', 'River']
                                    schools = ['Ridgeview', 'Seacoast', 'Woodside']
                                    sports = ['Tennis', 'Football', 'Netball']
                                    mascots = ['Bear', 'Lion', 'Fox']
                                    for i in range (0, len(names)):
                                        narrator("What is the school that " + names[i] + " attends?", 4)
                                        question2 = False
                                        while question2 == False:
                                            narrator("(1)Ridgeview  (2)Seacoast  (3)Woodside ", 0)
                                            if keyboard.is_pressed("1"):
                                                if schools[i] == "Ridgeview":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("2"):
                                                if schools[i] == "Seacoast":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("3"):
                                                if schools[i] == "Woodside":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                    for i in range (0, len(names)):
                                        narrator("What is the sport that " + names[i] + " participates in?", 4)
                                        question2 = False
                                        while question2 == False:
                                            narrator("(1)Tennis  (2)Netball  (3)Football ", 0)
                                            if keyboard.is_pressed("1"):
                                                if sports[i] == "Tennis":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("2"):
                                                if sports[i] == "Netball":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("3"):
                                                if sports[i] == "Football":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                    for i in range (0, len(names)):
                                        narrator("What is the mascot for " + names[i] + "'s school?", 4)
                                        question2 = False
                                        while question2 == False:
                                            narrator("(1)Bear  (2)Lion  (3)Fox ", 0)
                                            if keyboard.is_pressed("1"):
                                                if mascots[i] == "Bear":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("2"):
                                                if mascots[i] == "Lion":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                            if keyboard.is_pressed("3"):
                                                if mascots[i] == "Fox":
                                                    question2 = True
                                                    narrator("Correct!", 1)
                                                else:
                                                    narrator("Incorrect, try again.", 2)
                                    npc_1.speak("Congrats, you completed the puzzle! Here you go.")
                                    balance.add_money(10)
                                    complete1 = True
                                    narrator("You got 10 gold coins!", 2)
                                    said4 = True
                                if keyboard.is_pressed("2"):
                                    question = True
                                    npc_1.speak("Okay!")
                                    npc_1.speak("Come back later if you want to try!")

                    elif first_room.visited() == True:
                        npc_1.speak("Wow, it seems like you can enter the portal! That's a great feat in our world, you know.")
                        npc_1.speak("You must be special! If you decide to become a hero, you might get some gold out of it!")
                        narrator("Press the number in front of the question you'd like to ask.", 3)
                        question = False
                        while question == False:
                            narrator("(1) Name?  (2) Where am I?   (3) How do I get money? ", 0)
                            if keyboard.is_pressed("1"):
                                npc_1.speak("Huh? Sorry, must be the wind...I couldn't hear you. Repeat your question?")
                                question = True
                            if keyboard.is_pressed("2"):
                                npc_1.speak("Why, you're in ?!?!??!?, of course!")
                                time.sleep(2)
                                npc_1.speak("What do you mean you couldn't hear me? I said it so clearly...")
                                question = True
                            if keyboard.is_pressed("3"):
                                npc_1.speak("Oh, you want to become a hero now, do you? There are tasks that our people can't do themselves.")
                                npc_1.speak("If you help them, they're sure to give you a reward!")
                                question = True
                    else:
                        npc_1.speak("Hey, welcome to our village! I'm the village leader, I'm sure you'll get to know me more soon!")
                        
                if pygame.Rect(npc_2.get_x(), npc_2.get_y(), 80, 110).collidepoint(x, y):
                    if fourth_room.visited() == True:
                        npc_2.speak("You're here.")
                        while said7 == False:
                            narrator("(1) Why wouldn't I be?  (2) Any quests?", 0)
                            if keyboard.is_pressed("1"):
                                said7 = True
                                npc_2.speak("Something's coming.")
                                npc_2.speak("You don't deserve this.")
                                npc_2.speak("Look, I have some money for you.")
                                npc_2.speak("Buy a sword and shield.")
                                npc_2.speak("Please. For a friend.")
                                narrator("You got 100 gold coins!", 2)
                                balance.add_money(100)
                            if keyboard.is_pressed("2"):
                                said7 = True
                                npc_2.speak("Q-quests?")
                                npc_2.speak("Oh yeah, I have one.")
                                npc_2.speak("Here, take this money.")
                                npc_2.speak("Go to the store and buy a sword and shield.")
                                npc_2.speak("Please.")
                                narrator("You got 100 gold coins!", 2)
                                balance.add_money(100)
                        if said7 == True:
                            npc_2.speak("Have you got weapons yet?")
                    elif third_room.visited() == True:
                        if parcel == True and said3 == False:
                            questBook.remove_quest("Collect parcel", "Go to the village leader and collect the knight's parcel.")
                            inventory.remove_item("Parcel", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\parcel.png")
                            said3 = True
                            npc_2.speak("Thanks!")
                            npc_2.speak("Here, for your troubles.")
                            narrator("You got 25 gold coins!", 2)
                            balance.add_money(25)
                        else:
                            npc_2.speak("You're back!")
                            npc_2.speak("Okay, I have a tas-quest for you.")
                            npc_2.speak("Can you get a parcel from the village leader for me?")
                            question = False
                            while question == False:
                                narrator("(1) Yes  (2) No", 0)
                                if keyboard.is_pressed("1"):
                                    if (questBook.check_number() == False):
                                        narrator("You already have a quest, complete that before getting another.", 3)
                                        question = True
                                    elif (quest3.check_given() == False):
                                        question = True
                                        quest3.set_given(questBook)
                                        npc_2.speak("Cool! Just ask about my parcel, it'll be good.")
                                        narrator("You've got a new quest!", 2)
                                    else:
                                        if said3 == False:
                                            npc_2.speak("I've already given you a quest, go do that!")
                                        else:
                                            npc_2.speak("You already got 25 coins from me, you're not getting any more!")
                                        question = True
                                        
                                if keyboard.is_pressed("2"):
                                    question = True
                                    npc_2.speak("Okay then, jeez.")
                                    npc_2.speak("Come back if you wanna help.")

                                
                    elif second_room.visited() == True:
                        if npc_2.check_char_code() == False:
                            npc_2.speak("....")
                            question = False
                            while question == False:
                                narrator("(1) Name? ", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_2.set_char_code("Sir Roman")
                                    npc_2.speak("Sir Roman.")
                                    npc_2.speak("Thanks for asking.")
                                    npc_2.speak("Finally.")
                        else:
                            npc_2.speak("Hey again! Listen, I know it's weird to have two knights here.")
                            npc_2.speak("But I think we can get along! We should have a friend bonding session!")
                            question = False
                            while question == False:
                                narrator("(1) Yes   (2) No ", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_2.speak("Cool! Okay...what kind of things do you like?")
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1)Reading (2)Video games (3)Sports", 0)
                                        if keyboard.is_pressed("1"):
                                            question2 = True
                                            npc_2.speak("We-I used to read.")
                                            npc_2.speak("Yeah! Good interest!")
                                            npc_2.speak("Okay, new question!")
                                            npc_2.speak("What's your favourite colour?")
                                            question3 = False
                                            while question3 == False:
                                                narrator("(1)Blue (2)Green (3)Red (4)Pink", 0)
                                                if keyboard.is_pressed("3"):
                                                    question3 = True
                                                    npc_2.speak("Really! I like red too!")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                                                if keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("4"):
                                                    question3 = True
                                                    npc_2.speak("That's cool!")
                                                    npc_2.speak("My favourite is red.")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                                        if keyboard.is_pressed("2"):
                                            question2 = True
                                            npc_2.speak("Really? Huh.")
                                            npc_2.speak("For some reason, that's surprising.")
                                            npc_2.speak("Okay, new question!")
                                            npc_2.speak("What's your favourite colour?")
                                            question3 = False
                                            while question3 == False:
                                                narrator("(1)Blue (2)Green (3)Red (4)Pink", 0)
                                                if keyboard.is_pressed("3"):
                                                    question3 = True
                                                    npc_2.speak("Really! I like red too!")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                                                if keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("4"):
                                                    question3 = True
                                                    npc_2.speak("That's cool!")
                                                    npc_2.speak("My favourite is red.")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                                        if keyboard.is_pressed("3"):
                                            question2 = True
                                            npc_2.speak("I like sports too!")
                                            npc_2.speak("I think football's a lot of fun.")
                                            npc_2.speak("Okay, new question!")
                                            npc_2.speak("What's your favourite colour?")
                                            question3 = False
                                            while question3 == False:
                                                narrator("(1)Blue (2)Green (3)Red (4)Pink", 0)
                                                if keyboard.is_pressed("3"):
                                                    question3 = True
                                                    npc_2.speak("Really! I like red too!")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                                                if keyboard.is_pressed("1") or keyboard.is_pressed("2") or keyboard.is_pressed("4"):
                                                    question3 = True
                                                    npc_2.speak("That's cool!")
                                                    npc_2.speak("My favourite is red.")
                                                    npc_2.speak("Okay! Last question.")
                                                    npc_2.speak("Why'd you become a knight?")
                                                    time.sleep(4)
                                                    npc_2.speak("You can't say? That's okay.")
                                                    npc_2.speak("See you around, then!")
                    elif first_room.visited() == True:
                        if inventory.check_item('Flowers') == True and quest1.check_given() == True and said == False:
                            questBook.remove_quest("Flowers from the store", "Go to the shop directly north and buy the flowers for the knight.")
                            inventory.remove_item("Flowers", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\flowers.png")
                            npc_2.speak("Thanks, I guess. I didn't think you had the money.")
                            npc_2.speak("Since I'm such a kind soul, here you go.")
                            narrator("You got 20 gold coins!", 2)
                            said = True
                            balance.add_money(20)
                        else:
                            npc_2.speak("I cannot believe you stole my hero moment! I'm the better knight, not you!")
                            npc_2.speak("I should be able to go through the portal.")
                            question = False
                            narrator("Press the number in front of the question you'd like to ask.", 3)
                            while question == False:
                                narrator("""(1) Name?   (2)Shouldn't you have a horse?   (3) Do you have any quests for me?""", 0)
                                if keyboard.is_pressed("1"):
                                    npc_2.speak("You DON'T know my name?!? Sir Roman, saviour of the Sparking Islands and hero to the Twillows.")
                                    npc_2.set_char_code("Sir Roman")
                                    npc_2.speak("You can bow to me now.")
                                    question = True
                                if keyboard.is_pressed("2"):
                                    npc_2.speak("I...I lost my horse! On the side of a road! This..this isn't any fault of mine!!")
                                    question = True
                                if keyboard.is_pressed("3"):
                                    if (quest1.check_given() == False):
                                        npc_2.speak("Well, how dare you! I'm the hero around here, not you!")
                                        npc_2.speak("But if you must, fetch me some flowers from the store, please.")
                                        quest1.set_given(questBook)
                                        narrator("You've got a quest, cool!", 2)
                                        narrator("Move upward to find the shop, good luck!", 2)
                                        question = True
                                    else:
                                        if said == False:
                                            npc_2.speak("I've already given you a quest, go do that!")
                                        else:
                                            npc_2.speak("You already got 10 coins from me, you're not getting any more!")
                                        question = True
                    else:
                        npc_2.speak("Don't distract me, newbie! I'm pysching myself up.")
                        npc_2.speak("Why? I'm getting ready to go into that portal, of course!")
                        npc_2.speak("See? To the right, and down, with the blue pattern on top.")
                        
                if pygame.Rect(npc_3.get_x(), npc_3.get_y(), 80, 100).collidepoint(x, y):
                    if third_room.visited() == True:
                        if trust == True:
                            npc_3.speak("Hey friend!")
                            npc_3.speak("I found something cool!")
                            npc_3.speak("Do you want me to share it with you?")
                            narrator("Press the number in front of your answer.", 3)
                            question = False
                            while question == False:
                                narrator("(1) Yes  (2) No", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_3.speak("I found this in my house a while ago.")
                                    npc_3.speak("But I've only just realised what it does!")
                                    npc_3.speak("It's a special kind of spring!")
                                    npc_3.speak("You can use it to jump reallll high!")
                                    npc_3.speak("You can have it!")
                                    narrator("Super spring has been added to your inventory!", 4)
                                    inventory.add_item("Super spring", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\spring.png")
                                if keyboard.is_pressed("2"):
                                    question = True
                                    npc_3.speak("That's okay..")
                                    npc_3.speak("Come back if you want to know!")
                        else:
                            npc_3.speak("Hey...")
                            npc_3.speak("I found something..")
                            npc_3.speak("But I don't trust you..")
                            npc_3.speak("So I won't tell you what it is...")
                            
                    elif second_room.visited() == True:
                        if npc_3.check_char_code() == False:
                            npc_3.speak("....")
                            question = False
                            while question == False:
                                narrator("(1) Name? ", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_3.set_char_code("Timor")
                                    npc_3.speak("Timor.")
                                    npc_3.speak("Thanks for asking.")
                                    npc_3.speak("Finally.")
                        else:
                            if picture_seen == True and quest2.check_given() == True and said2 == False:
                                questBook.remove_quest("Picture from the sad room", "Go left of the forest and click on the picture.")
                                npc_3.speak("So, what'd you think of it?")
                                narrator("Press the number in front of your answer.", 3)
                                question = False
                                while question == False:
                                    narrator("(1) Good! (2) Interesting... (3) Deeply philosophical", 0)
                                    if keyboard.is_pressed("1"):
                                        question = True
                                        npc_3.speak("I'm glad you liked it!")
                                    if keyboard.is_pressed("2"):
                                        question = True
                                        npc_3.speak("It is interesting, isn't it?")
                                        npc_3.speak("I love to go to the SAD room.")
                                    if keyboard.is_pressed("3"):
                                        question = True
                                        npc_3.speak("I agree.")
                                        npc_3.speak("It's like a snapshot into the depths of human life and its many challenges.")
                                        time.sleep(5)
                                        npc_3.speak("Or just an apple.")
                                npc_3.speak("Thankyou for discussing this with me.")
                                npc_3.speak("I feel more...friendly with you now.")
                                npc_3.speak("So here. Money for my friend.")
                                balance.add_money(20)
                                trust = True
                                said2 = True
                                narrator("You got 20 gold coins!", 2)
                            else:   
                                npc_3.speak("Hello again...you're not just a tourist, are you...")
                                npc_3.speak("Oh well..I've grown accustomed to your presence..")
                                npc_3.speak("So I don't mind you here.")
                                narrator("Press the number in front of the question you'd like to ask.", 3)
                                question = False
                                while question == False:
                                    narrator("(1) Could we be friends? (2) Do you have any quests for me?", 0)
                                    if keyboard.is_pressed("1"):
                                        npc_3.speak("That's a bit too much for now...")
                                        npc_3.speak("But you can hang out here whenever...")
                                        question = True
                                    if keyboard.is_pressed("2"):
                                        if (questBook.check_number() == False):
                                            narrator("You already have a quest, complete that before getting another.", 3)
                                            question = True
                                        elif (quest2.check_given() == False):
                                            npc_3.speak("Quests? Oh! You're a hero!")
                                            npc_3.speak("I only ask one thing of you.")
                                            npc_3.speak("Go over to the SAD room and look at the picture there.")
                                            npc_3.speak("Then come back here and discuss it with me!")
                                            quest2.set_given(questBook)
                                            narrator("You have a new quest!", 2)
                                            narrator("You can find the SAD room left of the forest; click on the picture there!", 5)
                                            question = True
                                        else:
                                            if said2 == False:
                                                npc_3.speak("I've already given you a quest, go do that!")
                                            else:
                                                npc_3.speak("You already got 20 coins from me, you're not getting any more!")
                                            question = True
                    elif first_room.visited() == True:
                        npc_3.speak("Ohhh nooo, you're s-speaking to me? Have I done anything to offend?")
                        narrator("Press the number in front of the question you'd like to ask.", 3)
                        question = False
                        while question == False:
                            narrator("(1) Name?   (2) How are you?  (3) Why are you scared of me? ", 0)
                            if keyboard.is_pressed("1"):
                                npc_3.speak("O-oh, I'm Timor!")
                                npc_3.set_char_code("Timor")
                                time.sleep(1)
                                npc_3.speak("N-nice to meet you.")
                                question = True
                            if keyboard.is_pressed("2"):
                                npc_3.speak("I'm...okay.")
                                question = True
                            if keyboard.is_pressed("3"):
                                npc_3.speak("I'm not...scared!")
                                time.sleep(2)
                                npc_3.speak("I just don't like speaking much. Especially to new people.")
                                question = True
                    else:
                        npc_3.speak("Ohhh nooo, not a newbie! S-sorry, just doing some gardening! Come back later!")
                        
                if pygame.Rect(npc_4.get_x(), npc_4.get_y(), 80, 110).collidepoint(x, y):
                    if fourth_room.visited() == True:
                        if complete == True:
                            npc_4.speak("Thankyou.")
                            balance.add_money(10)
                            npc_4.speak("You got 10 gold coins!")
                        npc_4.speak("Hello again. I have a quest for you.")
                        npc_4.speak("Want to give it a go?")
                        question = False
                        while question == False:
                            narrator("(1) Yes  (2) No", 0)
                            if keyboard.is_pressed("1"):
                                if (questBook.check_number() == False):
                                    narrator("You already have a quest, complete that before getting another.", 3)
                                    question = True
                                elif (fire_trust == True and quest5.check_given() == False and said9 == False):
                                    quest5.set_given(questBook)
                                    npc_4.speak("Alright! Go to the shop.")
                                    npc_4.speak("And smile at the shopkeeper.")
                                    npc_4.speak("I know it seems weird.")
                                    npc_4.speak("But I want to help.")
                                    narrator("Your quest has been added to your questbook.", 4)
                                    #if you smile- in the final battle your inner demon expresses confusion as to why
                                    #confusion makes his health go down a little
                                elif (fire_trust == False and quest4.check_given() == False and said8 == False):
                                    quest4.set_given(questBook)
                                    npc_4.speak("Your task is to SCREAM at the shopkeeper.")
                                    npc_4.speak("And you'd BETTER do it.")
                                    npc_4.speak("HURRY UP!")
                                    narrator("Your quest has been added to your questbook.", 4)
                                    #if you scream- in the final battle your inner demon is angry and his health increases
                                    #lesson- yelling does not solve your problems...or something like that
                                else:
                                    npc_4.speak("You already got 10 coins from me, you're not getting any more!")
                                    question = True
                            if keyboard.is_pressed("2"):
                                npc_4.speak("That's okay.")
                                npc_4.speak("Come back if you want to try.")
                            
                    elif third_room.visited() == True:
                        npc_4.speak("Hello again.")
                        npc_4.speak("Look, sorry for yelling earlier.")
                        npc_4.speak("I still don't like you, but that was stupid.")
                        npc_4.speak("I'm just angry, like always.")
                        question = False
                        while question == False:
                            narrator("(1) Why did I ignore you?  (2) I'm sorry too.", 0)
                            if keyboard.is_pressed("1"):
                                question = True
                                npc_4.speak("You thought emotions were taking over your life.")
                                npc_4.speak("So you suppressed them. Suppressed us.")
                                npc_4.speak("That was dangerous.")
                                npc_4.speak("And you started to forget who you were.")
                                question2 = False
                                while question2 == False:
                                    narrator("(1) Is that why I'm here?  (2) I'm sorry.", 0)
                                    if keyboard.is_pressed("1"):
                                        question2 = True
                                        npc_4.speak("That's what I think.")
                                        npc_4.speak("You delved into your mind.")
                                        npc_4.speak("Maybe you want to change things.")
                                        npc_4.speak("Do you?")
                                        question3 = False
                                        while question3 == False:
                                            narrator("(1) I do.", 0)
                                            if keyboard.is_pressed("1"):
                                                question3 = True
                                                npc_4.speak("Thankyou, then.")
                                                npc_4.speak("I'm sorry for doubting you.")
                                                fire_trust = True
                                    if keyboard.is_pressed("2"):
                                        question2 = True
                                        npc_4.speak("You're sorry for forgetting?")
                                        npc_4.speak("Sorry for yourself?")
                                        npc_4.speak("You don't understand.")
                            if keyboard.is_pressed("2"):
                                question = True
                                npc_4.speak("You don't remember what you're sorry for.")
                                npc_4.speak("That's not a real apology.")
                                
                    elif second_room.visited() == True:
                        if npc_4.check_char_code() == False:
                            npc_4.speak("....")
                            question = False
                            while question == False:
                                narrator("(1) Name? ", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_4.set_char_code("Kaen")
                                    npc_4.speak("Kaen.")
                                    npc_4.speak("Thanks for asking.")
                                    npc_4.speak("Finally.")
                        else:
                            npc_4.speak("You still look so smug.")
                            npc_4.speak("You were always going to be walking through the portal.")
                            npc_4.speak("It was designed for you, after all.")
                            question = False
                            while question == False:
                                narrator("(1) How do you know so much?  (2)I really don't know why you hate me.", 0)
                                if keyboard.is_pressed("1"):
                                    question = True
                                    npc_4.speak("It's obvious.")
                                    npc_4.speak("You're important around here.")
                                    npc_4.speak("Everyone knows you.")
                                    npc_4.speak("If they recognised you...")
                                    npc_4.speak("But you're not meant to be here.")
                                    npc_4.speak("This place isn't for you.")
                                    npc_4.speak("There's only one scenario where you'd be here.")
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1) WHY AM I HERE!?!?", 0)
                                        if keyboard.is_pressed("1"):
                                            question2 = True
                                            npc_4.speak("Something went wrong.")
                                            npc_4.speak("You MESSED UP.")
                                            npc_4.speak("And you don't deserve to hear anymore.")
                                if keyboard.is_pressed("2"):
                                    question = True
                                    npc_4.speak("Stop LYING.")
                                    npc_4.speak("To me and to yourself.")
                                    npc_4.speak("YOU SHUT ME OUT!")
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1) How did I shut you out?", 0)
                                        if keyboard.is_pressed("1"):
                                            question2 = True
                                            npc_4.speak("STOP ACTING SO INNOCENT!!")
                                            npc_4.speak("YOU WEREN'T ANGRY ANYMORE!")
                                            npc_4.speak("YOU WEREN'T ANYTHING AT ALL!")
                                            npc_4.speak("Maybe that's why you're here.")
                                            
                    elif first_room.visited() == True:
                        npc_4.speak("Suppose you think you're a hero now.")
                        npc_4.speak("Well, I've got some news for you- walking though yet another open door doesn't make you fearless.")
                        npc_4.speak("It makes you spoiled.")
                        narrator("Press the number in front of the question you'd like to ask.", 3)
                        question = False
                        while question == False:
                            narrator("(1) Name?  (2) What have I done to you?", 0)
                            if keyboard.is_pressed("1"):
                                npc_4.speak("You don't remember anything, do you?")
                                npc_4.speak("I'm Kaen.")
                                npc_4.set_char_code("Kaen")
                                question = True
                            if keyboard.is_pressed("2"):
                                npc_4.speak("You really have the nerve, don't you?")
                                npc_4.speak("Just stay out of my way.")
                                npc_4.speak("The others don't recognise you, but I do.")
                                question = True
                    else:
                        npc_4.speak("Look at you, waltzing in here like you own the place.")
                        npc_4.speak("You actually look confused. Wow.")
            if event.type == pygame.QUIT:
                import Start_Game
            
    while (room.check_area() == "room1"):
        bg3 = Screen(width, height)
        screen = pygame.display.set_mode((bg3.check_width(), bg3.check_height()))
        screen.fill(black)
        main_theme.set_volume(0)
        scary.set_volume(0.04)
        Portal.change_room("room2")
        pygame.display.flip()
        if first_room.check_time() == True:
            first_room.dialogue(room, position2)
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "room2"):
        Portal.change_room("room3")
        main_theme.set_volume(0)
        screen.fill(black)
        font = pygame.font.SysFont("Century", 25)
        intro = Text("In this area, you must answer truthfully to your own values.", 620, 400)
        intro.display(white)
        time.sleep(4)
        pygame.display.flip()
        if second_room.check_time() == True:
            second_room.dialogue(room, position2)
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "room3"):
        Portal.change_room("room4")
        main_theme.set_volume(0)
        screen.fill(black)
        font = pygame.font.SysFont("Century", 25)
        intro = Text("In this area, you must answer truthfully to your own values.", 620, 400)
        intro.display(white)
        time.sleep(4)
        pygame.display.flip()
        if third_room.check_time() == True:
            third_room.dialogue(room, position2)
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "room4"):
        fourth_room.is_visited()
        bg4 = Screen(width, height)
        screen = pygame.display.set_mode((bg4.check_width(), bg4.check_height()))
        Portal.change_room("room5")
        main_theme.set_volume(0)
        screen.fill(black)
        new_area = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\room2_scene.png")
        new_area_change = pygame.transform.scale(new_area, (1240, 1000))
        screen.blit(new_area_change, (0,0))
        woman = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\woman.png")
        woman_change = pygame.transform.scale(woman, (100, 120))
        screen.blit(woman_change, (500, 600))
        narrator("Click on the woman to talk to her.", 0)
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(500, 600, 100, 120).collidepoint(x, y):
                    time.sleep(2)
                    narrator("Hello, my child. You look lost.", 4)
                    narrator("Would you like to come into my house?", 4)
                    question = False
                    while question == False:
                        narrator("Will you go in, or leave the area?", 0)
                        arrow_up = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\arrow.png")
                        screen.blit(arrow_up, (550, 500))
                        arrow_right = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\arrow_right.png")
                        screen.blit(arrow_right, (950, 700))
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if pygame.Rect(550, 500, 100, 100).collidepoint(x, y):
                                    comparisonA.add_points("Impulse", 1)
                                    question = True
                                    inside_area = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\room2_sceneinside.png")
                                    inside_area_change = pygame.transform.scale(inside_area, (1240, 1000))
                                    screen.blit(inside_area_change, (0,0))
                                    woman = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\woman.png")
                                    woman_change = pygame.transform.scale(woman, (100, 120))
                                    screen.blit(woman_change, (500, 600))
                                    pygame.display.flip()
                                    narrator("Welcome to my house!", 3)
                                    narrator("I'll get to making you some food, or you can make some yourself.", 6)
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1)Woman makes you food  (2)You make your own food", 0)
                                        if keyboard.is_pressed("1"):
                                            question2 = True
                                            corevalues.add_value("Caring", 2)
                                            narrator("The woman goes to the kitchen to make you some food.", 4)
                                        if keyboard.is_pressed("2"):
                                            question2 = True
                                            corevalues.add_value("Contribution", 2)
                                            narrator("You head to the kitchen to make some food.", 4)
                                    narrator("You then see an item on the floor- the woman must've dropped it.", 4)
                                    narrator("Do you take it?", 3)
                                    question3 = False
                                    while question3 == False:
                                        narrator("(1) Yes  (2) No", 0)
                                        if keyboard.is_pressed("1"):
                                            question3 = True
                                            corevalues.add_value("Curiosity", 2)
                                            narrator("You take the item.", 2)
                                            inventory.add_item("Potion", "C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\potion.png")
                                        if keyboard.is_pressed("2"):
                                            question3 = True
                                            corevalues.add_value("Justice", 2)
                                            narrator("You leave the item alone.", 2)
                                    narrator("Without looking at you, the woman speaks.", 4)
                                    screen.fill(black)
                                    woman = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\woman.png")
                                    woman_change = pygame.transform.scale(woman, (100, 120))
                                    screen.blit(woman_change, (500, 600))
                                    narrator("You seem to be reaching the end of your journey, my child.", 6)
                                    narrator("But heed my words.", 3)
                                    narrator("You will soon enter a battle where you MUST win.", 4)
                                    narrator("For the sake of us all.", 3)
                                    room.move_area("Village")
                                    position2.change_x(300)
                                                               
                                if pygame.Rect(950, 700, 200, 100).collidepoint(x, y):
                                    comparisonA.add_points("Cautious", 1)
                                    screen.fill(black)
                                    question = True
                                    forest = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\foresttrees.png")
                                    forest_change = pygame.transform.scale(forest, (1340, 820))
                                    screen.blit(forest_change, (0,0))
                                    bat = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\bat.png")
                                    screen.blit(bat, (300, 200))
                                    kestral = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\kestral.png")
                                    screen.blit(kestral, (500, 650))
                                    pygame.display.flip()
                                    narrator("What do you do here?", 3)
                                    question2 = False
                                    while question2 == False:
                                        narrator("(1)Examine the bat (2)Examine the kestral (3)Sit in silence", 0)
                                        if keyboard.is_pressed("1"):
                                            question2 = True
                                            corevalues.add_value("Curiosity", 2)
                                            friend = True
                                            narrator("You take a closer look at the bat.", 3)
                                            narrator("It seems to like you.", 2)
                                        if keyboard.is_pressed("2"):
                                            question2 = True
                                            corevalues.add_value("Curiosity", 2)
                                            narrator("You take a closer look at the kestral.", 3)
                                            narrator("It moves away from you.", 2)
                                        if keyboard.is_pressed("3"):
                                            question2 = True
                                            corevalues.add_value("Gratitude", 2)
                                            narrator("You sit in silence, and listen to the music.", 4)
                                    room.move_area("Village")
                                    position2.change_x(300)
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "room5"):
        main_theme.set_volume(0)
        screen.fill(black)
        font = pygame.font.SysFont("Century", 25)
        first = Text("Guess who?", 620, 330)
        first.display(red)
        time.sleep(2)
        
        if complete == True and quest4.check_given() == True:
            second = Text("You screamed at me.", 620, 370)
            second.display(red)
            time.sleep(2)
            third = Text("That really doesn't help anyone.", 620, 420)
            third.display(red)
            time.sleep(3)
            fourth = Text("Seems you still have a couple of internal conflicts.", 620, 460)
            fourth.display(red)
            time.sleep(4)
            fifth = Text("That'll make it even harder to defeat me.", 620, 500)
            fifth.display(red)
            time.sleep(3)
            narrator("His health has increased!", 2)
            health += 5
            
        if complete == True and quest5.check_given() == True:
            if trust == True:
                second = Text("Seems you have a couple of allies.", 620, 370)
                second.display(red)
                time.sleep(3)
            else:
                second = Text("Seems you made an ally in Kaen.", 620, 370)
                second.display(red)
                time.sleep(3)
            third = Text("I didn't expect that.", 620, 420)
            third.display(red)
            time.sleep(2)
            fourth = Text("But don't think that means anything.", 620, 460)
            fourth.display(red)
            time.sleep(3)
            fifth = Text("You may have solved some internal conflicts.", 620, 500)
            fifth.display(red)
            time.sleep(3)
            sixth = Text("But I'm still going to destroy you.", 620, 540)
            sixth.display(red)
            time.sleep(3)
            narrator("His health has decreased!", 2)
            health -= 5

        if complete == False:
            second = Text("You didn't really do much of anything, did you?", 620, 370)
            second.display(red)
            time.sleep(2)
            third = Text("Skipping side quests...tsk tsk.", 620, 420)
            third.display(red)
            time.sleep(2)
            fourth = Text("Your confidence will be your downfall.", 620, 460)
            fourth.display(red)
            time.sleep(2)
    
        screen.fill(black)
        shopkeeper = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\shop-keeper.png")
        shopkeeper_change = pygame.transform.scale(shopkeeper, (220, 340))
        screen.blit(shopkeeper_change, (520, 150))
        your_health = 50
        pygame.display.flip()
        
        while health > 0:
            question = False
            defence = False
            while question == False:
                narrator("(1) Sword  (2)Shield  (3)Flower  (4)Parcel  (5)Potion  (6)Spring", 0)
                if friend == True:
                    question = True
                    friend = False
                    narrator("Your friend appears and defends you!", 3)
                    narrator("10 damage dealt!", 2)
                    
                if keyboard.is_pressed("1"):
                    question = True
                    num = str(random.randint(3,7))
                    narrator(num + " damage dealt.", 2)
                    health -= int(num)
                    
                if keyboard.is_pressed("2"):
                    question = True
                    defence = True
                    narrator("Your defence has gone up!", 2)

                if keyboard.is_pressed("3"):
                    if inventory.check_item("Flower") == True:
                        question = True
                        narrator("You throw a flower at him.", 3)
                        narrator("It does nothing.", 2)
                    else:
                        question = True
                        narrator("Sorry, you don't have a flower to attack with.", 3)

                if keyboard.is_pressed("4"):
                    if inventory.check_item("Parcel") == True and used1 == False:
                        question = True
                        used1 = True
                        narrator("The parcel opens to reveal...a hammer!", 4)
                        narrator("You throw it at him.", 2)
                        narrator("7 damage dealt.", 2)
                    else:
                        narrator("Sorry, you don't have a parcel to attack with.", 3)

                if keyboard.is_pressed("5"):
                    if inventory.check_item("Potion") == True and used2 == False:
                        question = True
                        used2 = True
                        narrator("You throw your potion at him.", 4)
                        narrator("15 damage dealt.", 2)
                    else:
                        narrator("Sorry, you don't have a potion to attack with.", 3)

                if keyboard.is_pressed("6"):
                    if inventory.check_item("Super spring") == True and used3 == False:
                        question = True
                        used3 = True
                        narrator("You use your super spring to jump at him.", 4)
                        narrator("10 damage dealt.", 2)
                    else:
                        narrator("Sorry, you don't have a spring to attack with.", 3)

            narrator("He attacks you!", 2)
            if defence == True:
                num = str(random.randint(0, 3))
                if random.randint(0, 1) == 1:
                    narrator("He takes 3 knockback damage!", 2)
                    health -= 3
            else:
                num = str(random.randint(3, 7))
            narrator("You take "+ num + " damage!", 2)
            your_health -= int(num)
            if your_health <= 0:
                narrator("You lost!", 2)
                room.move_area("Village")

        narrator("You beat him!", 2)
        screen.fill(black)
        narrator("Here are your core traits!", 3)
        for i in range (0, corevalues.get_length()):
            value = Text(corevalues.get_item(i), 500, 100 + (100 * i))
            value.display(white)
        import Start_Game
                
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game
        
    while (room.check_area() == "questbook"):
        if (questBook.check() == None):
            screen.fill(white)
            no_quests = font.render("""No current quests. Press Q to exit this screen.""", True, black)
            no_questsRect = no_quests.get_rect()
            no_questsRect.center = (500, 500)
            screen.blit(no_quests, no_questsRect)
        else:
            screen.fill(white)
            questBook.display_quests()
            exit_room = font.render("Press Q to exit this screen.", True, black)
            exit_roomRect = exit_room.get_rect()
            exit_roomRect.center = (600, 700)
            screen.blit(exit_room, exit_roomRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            room.move_area("Village")  
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "pause"):
        screen.fill(black)
        play_button = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\play_button.png")
        play_button_smaller = pygame.transform.scale(play_button,(200, 100))
        screen.blit(play_button_smaller, (400, 200))
        menu_button = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\menu_button.png")
        menu_button_smaller = pygame.transform.scale(menu_button, (200, 100))
        screen.blit(menu_button_smaller, (400, 400))
        exit_button = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\exit_button.png")
        exit_button_smaller = pygame.transform.scale(exit_button,(200, 100))
        screen.blit(exit_button_smaller, (400, 600))
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(400, 200, 200, 100).collidepoint(x, y):
                    room.move_area("Village")
                if pygame.Rect(400, 400, 200, 100).collidepoint(x, y):
                    import Start_Game
                if pygame.Rect(400, 600, 200, 100).collidepoint(x, y):
                    pygame.quit()
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "help"):
        screen.fill(black)
        if first_room.visited() == True:
            clue = font.render("Having trouble finding money? Take a look in the villagers' houses.", True, white)
            clue2 = font.render("You can enter a house by walking up to the door!", True, white)
            clue2Rect = clue2.get_rect()
            clue2Rect.center = (600, 600)
            clueRect = clue.get_rect()
            clueRect.center = (600, 500)
            screen.blit(clue, clueRect)
            screen.blit(clue2, clue2Rect)
        else:
            clue = font.render("Remember, press on the villagers to talk to them! One might reveal something...", True, white)
            clueRect = clue.get_rect()
            clueRect.center = (600, 500)
            screen.blit(clue, clueRect)
        exit_room = font.render("Press Q to exit this screen.", True, white)
        exit_roomRect = exit_room.get_rect()
        exit_roomRect.center = (600, 700)
        screen.blit(exit_room, exit_roomRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            room.move_area("Village")
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "coin"):
        screen.fill(black)
        amount = balance.check_money()
        money = font.render("You have " + str(amount) + " coins!", True, white)
        moneyRect = money.get_rect()
        moneyRect.center = (600, 400)
        screen.blit(money, moneyRect)
        exit_room = font.render("Press Q to exit this screen.", True, white)
        exit_roomRect = exit_room.get_rect()
        exit_roomRect.center = (600, 700)
        screen.blit(exit_room, exit_roomRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            room.move_area("Village")
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game
                

    while (room.check_area() == "guide"):
        screen.fill(black)
        first = font.render("Open your inventory by pressing space.", True, white)
        firstRect = first.get_rect()
        firstRect.center = (600, 400)
        screen.blit(first, firstRect)
        second = font.render("Close your inventory by pressing enter.", True, white)
        secondRect = second.get_rect()
        secondRect.center = (600, 500)
        screen.blit(second, secondRect)
        third = font.render("Talk by people you meet by clicking on them.", True, white)
        thirdRect = third.get_rect()
        thirdRect.center = (600, 600)
        screen.blit(third, thirdRect)
        exit_room = font.render("Press Q to exit this screen.", True, white)
        exit_roomRect = exit_room.get_rect()
        exit_roomRect.center = (600, 700)
        screen.blit(exit_room, exit_roomRect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            room.move_area("Village")
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                import Start_Game
                
    while (room.check_area() == "shop"):
        screen.fill(white)
        shop_inside = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\store.jpg")
        shop_inside_change = pygame.transform.scale(shop_inside, (1240, 1000))
        screen.blit(shop_inside_change, (0,0))
        shopkeeper = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\shop-keeper.png")
        shopkeeper_change = pygame.transform.scale(shopkeeper, (220, 340))
        screen.blit(shopkeeper_change, (520, 150))
        leave_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\leave_room.png")
        leave_room_change = pygame.transform.scale(leave_room, (200, 100))
        screen.blit(leave_room_change, (30, 600))
        if quest4.check_given() == True:
            if said8 == False:
                screen.fill(black)
                shopkeeper = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\shop-keeper.png")
                shopkeeper_change = pygame.transform.scale(shopkeeper, (220, 340))
                screen.blit(shopkeeper_change, (520, 150))
                pygame.display.flip()
                yelling = False
                while yelling == False:
                    narrator("Press Y to yell.", 0)
                    if keyboard.is_pressed("Y"):
                        complete = True
                        room.move_area("Village")
                        for i in range (0, 20):
                            position2.movement('s')
                            traveller.move_down()
                            store.move_down()
                            npc_1.move_down()
                            npc_2.move_down()
                            npc_3.move_down()
                            npc_4.move_down()
                            
        if quest5.check_given() == True:
            if said8 == False:
                screen.fill(black)
                shopkeeper = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\shop-keeper.png")
                shopkeeper_change = pygame.transform.scale(shopkeeper, (220, 340))
                screen.blit(shopkeeper_change, (520, 150))
                pygame.display.flip()
                smiling = False
                while smiling == False:
                    narrator("Press C to smile.", 0)
                    if keyboard.is_pressed("C"):
                        complete = True
                        room.move_area("Village")
                        for i in range (0, 20):
                            position2.movement('s')
                            traveller.move_down()
                            store.move_down()
                            npc_1.move_down()
                            npc_2.move_down()
                            npc_3.move_down()
                            npc_4.move_down()
                            
        narrator("Click on the smiley shopkeeper to access the store menu.", 0)
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(30, 600, 200, 100).collidepoint(x, y):
                    room.move_area("Village")
                    for i in range (0, 20):
                        position2.movement('s')
                        traveller.move_down()
                        store.move_down()
                        npc_1.move_down()
                        npc_2.move_down()
                        npc_3.move_down()
                        npc_4.move_down()
                if pygame.Rect(520, 150, 220, 340).collidepoint(x, y):
                    store_menu.open()
            if event.type == pygame.QUIT:
                import Start_Game

    while (room.check_area() == "Bonus"):
        sunny = Arc(200, 250)
        main_theme.set_volume(0)
        sad.set_volume(0.04)
        screen.fill(blue)
        bonus_room = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\sadman_saddog.png")
        bonus_room_change = pygame.transform.scale(bonus_room, (620, 1000))
        screen.blit(bonus_room_change, (0, 0))
        pink = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\pink.png")
        pink_change = pygame.transform.scale(pink, (620, 600))
        screen.blit(pink_change, (620, 400))
        apple = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\apple.png")
        apple_change = pygame.transform.scale(apple, (70, 70))
        screen.blit(apple_change, (320, 350))
        position3.initialise()
        position3.border_Bonus(room, blue)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            position3.movement('a')
        if keys[pygame.K_w]:
            position3.movement('w')
        if keys[pygame.K_s]:
            position3.movement('s')
        if keys[pygame.K_d]:
            position3.movement('d')
        if keys[pygame.K_SPACE]:
            inventory.open()
        pygame.display.flip()
        time.sleep(0.005)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if pygame.Rect(320, 350, 70, 70).collidepoint(x, y):
                    condition = False
                    while condition == False:
                        apple = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\apple.png")
                        apple_change = pygame.transform.scale(apple, (300, 300))
                        screen.blit(apple_change, (320, 350))
                        exit_view = pygame.image.load("C:\\Users\\abbyn\\OneDrive\\Documents\\Introspection\\Images\\exit_view.png")
                        exit_view_change = pygame.transform.scale(exit_view, (300, 70))
                        screen.blit(exit_view_change, (320, 700))
                        pygame.display.flip()
                        time.sleep(0.005)
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                                if pygame.Rect(320, 700, 300, 70).collidepoint(x, y):
                                    condition = True
                                    narrator("You feel like your life has changed after looking at this picture.", 5)
                                    narrator("For better or for worse, you can't tell.", 3)
                                    picture_seen = True
                        if event.type == pygame.QUIT:
                            import Start_Game
            if event.type == pygame.QUIT:
                import Start_Game
