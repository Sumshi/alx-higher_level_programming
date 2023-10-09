#!/usr/bin/python3
import random
import math

class Warrior:
    def __init__(self, name="", health=0, attMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attMax = attMax
        self.blockMax = blockMax

    def attack(self):
        attAmt = self.attMax * (random.random() + .5)
        return attAmt

    def block(self):
        blockAmt = self.blockMax * (random.random() + .5)
        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "GameOver":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "GameOver":
                print("Game Over")
                break

    
