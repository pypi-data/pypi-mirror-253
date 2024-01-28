import numpy as np
from random import randint
from enum import Enum
from sympy import isprime
from colormap import rgb2hex

class invalidInputsException(Exception):
    def __init__(self, message:str="Incorrect Inputs provided"):
        self.message = message
        super().__init__(self.message)



def mapToNPArray( xValues, function):
    yValues = np.array([function(x) for x in xValues])
    return yValues

def lowestSumList(lis):
    lowest = lis[0]

    for item in lis[1::]:
        if sum(item) < sum(lowest):
            lowest = item

    return lowest

def calculateDimensions(graphsNum:int): 
    '''
    We dont want (15, 2) from 30, we want (6,5) or (5,6)
    so find each solution sum and return the one with the lowest 
    NOTE: This will mean that (6,5) and (5,6) are both valid solutions 
    '''
   
    MINIMUM = 2, 2
    isgraphsnumBelowMinimum = graphsNum in range(4)

    if isgraphsnumBelowMinimum:
        return MINIMUM
    
    if isprime(graphsNum): 
        CONVERT_PRIME_TO_NONPRIME = 1
        graphsNum = graphsNum + CONVERT_PRIME_TO_NONPRIME  # generally primes are odd so + 1 makes them even and not prime

    solutions = []

    for i in range(graphsNum-1, 1, -1):
        
        isDivisible = graphsNum % i == 0
       
        if isDivisible: 
            solutions.append([ i, int(graphsNum / i)])

    lowestSumSolution = lowestSumList(solutions)
    x, y = lowestSumSolution

    return x,y

def getCoordinates(x, y,num):
    
    inBounds = num < x*y
    if not inBounds: return

    willCauseDivideByZero = num < y
    if willCauseDivideByZero: return 0, num


    xcoord = num // y
    ycoord = num % (y * xcoord)

    return xcoord, ycoord

class COLORTYPE(Enum):
    RGB = 0
    HEXADECIMAL = 1
    #Add other types of colors and add them to the other stuff, maybe add this to a new package of its own
def getRandomColor(colortype=COLORTYPE.HEXADECIMAL):

    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    colorTypeMapping = {
        COLORTYPE.HEXADECIMAL: rgb2hex(r,g,b),
        COLORTYPE.RGB: f"rgb({r},{g},{b})"
    }

    return colorTypeMapping.get(colortype)

def areAllElementsInListOfCertainType(listOfElements, dataType):
    if type(listOfElements)!= list: return
    for element in listOfElements:
        if type(element)!= dataType:
            return False
    return True