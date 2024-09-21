'''File: studentATT.py
Features for managing a student's name and grades'''
class Student:
    '''Represents a student'''
    def __init__(self, name, roll, age, number):
        '''All scores are initially 0.'''
        self.name = name
        self._roll = roll
        self.__age = age
        self.scores = []
        for count in range(number):
            self.scores.append(0)
            
    def __str__(self):
        '''Returns the string representation of the student.'''
        return "Name: " + self.name + "\nRoll: " + self._roll + \
            "\nAge: " + str(self.__age) + "\nScores: " + \
            " ".join(map(str, self.scores))    

    def __eq__(self, other):
        return self.getName() == other.getName()
    
    def __lt__(self, other):
        return self.getName() < other.getName()
    
    def __gt__(self, other):
        return self.getName() > other.getName()
            
    def getName(self): # Method to get the name
        '''Returns the student's name'''
        return self.name
    
    def setName(self, name):
        self.name = name
        
    def getRoll(self):
        '''Returns the student's roll number'''
        return self._roll
    
    def setRoll(self, roll):
        self._roll = roll
    
    def getAge(self):
        '''returns the student's age'''
        return self.__age
    
    def setAge(self, age):
        self.__age = age