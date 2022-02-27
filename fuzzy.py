import math
import json

class Fuzzy:
    def __init__(self):
        self.setT = 0.0
        self.T2 = 0.0
        self.T3 = 0.0
        self.T4 = 0.0
        self.lvlOne = 0
        self.lvlTwo = 0
        self.lvlThree = 0
        self.lvlFour = 0
        #default values
        self.zero = 0
        self.low = 30
        self.medium = 60
        self.high = 100
    
    def defineFuzzyValues(self,s1,s2,s3,s4):
        self.zero = s1
        self.low = s2
        self.medium = s3
        self.high = s4

    def setpoints(self,T):
        self.setT = T
        self.T2 = T-2.0
        self.T3 = T-3.0
        self.T4 = T-4.0

    def lvlOneFuzzy(self,curT):
        if curT <= self.T4:
            self.lvlOne = 1
        if curT > self.T4 or curT < self.T3:
            self.lvlOne = round((self.T3 - curT)/(self.T3-self.T4),2)
            if self.lvlOne < 0:
                self.lvlOne = 0
            elif self.lvlOne > 1:
                self.lvlOne =1
        #print('f.malejaca lvl1 , wartosc = {}'.format(self.lvlOne))
        if curT >= self.T3:
            self.lvlOne = 0

    def lvlTwoFuzzy(self,curT):
        if curT <= self.T4 or curT >= self.T2:
            self.lvlTwo = 0
            if self.lvlTwo < 0:
                self.lvlTwo = 0
            elif self.lvlTwo > 1:
                self.lvlTwo = 1
        else:
            if curT > self.T3 and curT < self.T2:
                self.lvlTwo = round(((self.T2 - curT)/(self.T2-self.T3)),2)
                print('f.malejaca lvl2 , wartosc = {}'.format(self.lvlTwo))
            elif curT > self.T4 and curT <= self.T3:
                self.lvlTwo = round((curT - self.T4)/(self.T3-self.T4),2)
                print('f.rosnaca lvl2 , wartosc = {}'.format(self.lvlTwo))

    def lvlThreeFuzzy(self,curT):
        if curT <= self.T3 or curT >= self.setT:
            self.lvlThree = 0
            if self.lvlThree < 0:
                self.lvlThree = 0
            elif self.lvlThree > 1:
                self.lvlThree = 1
        else:
            if curT > self.T2 and curT < self.setT:
                self.lvlThree = round((self.setT - curT)/(self.setT-self.T2),2)
                print('f.malejaca lvl3 , wartosc = {}'.format(self.lvlThree))
            elif curT > self.T3 and curT <= self.T2:
                self.lvlThree = round((curT - self.T3)/(self.T2-self.T3),2)
                print('f.rosnaca lvl3 , wartosc = {}'.format(self.lvlThree))

    def lvlFourFuzzy(self,curT):
        if curT <= self.T2:
            self.lvlFour = 0
        elif curT >= self.setT:
            self.lvlFour = 1
        elif curT > self.T2 or curT <= self.setT:
            self.lvlFour = round((curT - self.T2)/(self.setT-self.T2),2)
            if self.lvlFour < 0:
                self.lvlFour = 0
            elif self.lvlFour > 1:
                self.lvlFour =1
            print('f.rosnaca lvl4 , wartosc = {}'.format(self.lvlFour))

    def fuzzyRegulation(self,setPoint,currentTemp):
        self.setpoints(setPoint)
        print(self.setT,self.T2,self.T3,self.T4)
        #fuzzification
        self.lvlOneFuzzy(currentTemp)
        self.lvlTwoFuzzy(currentTemp)
        self.lvlThreeFuzzy(currentTemp)
        self.lvlFourFuzzy(currentTemp)
        print('wartość lvl1 = {}, wartosć lvl2 = {}, wartosć lvl3 = {}, wartość lv4 = {}'.format(self.lvlOne,self.lvlTwo,self.lvlThree,self.lvlFour))       
        #HEATING LEVELS:
        # -->ZERO (0%)
        # -->LOW (30%)
        # -->MEDIUM (60%)
        # -->HIGH (100%)
        #Example
        #heating is ZERO (0%) with the truth value 0.2
        #heating is LOW (30%) with the truth value 0.8
        #then defuzzyfication using COG method

        val = self.lvlOne*self.high+self.lvlTwo*self.medium+self.lvlThree*self.low+self.lvlFour*self.zero
        #print(val)
        return val


