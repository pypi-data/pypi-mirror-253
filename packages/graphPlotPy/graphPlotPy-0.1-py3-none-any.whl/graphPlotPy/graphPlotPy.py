import matplotlib.pyplot as plt
import numpy as np

from typing import Callable
from graphPlotPy.graphUtils import *

# For type hints:
from matplotlib.figure import Figure
from matplotlib.axes import Axes

def _customiseAxesDefault_(ax):
    ax.set_facecolor( color='black' )
    ax.grid(color='#0000ff', linewidth=.5, alpha=0.3)

def _customiseFigDefault_(fig):
    fig.set_facecolor( color='#4287F5')

def _customiseColorsDefault_():
    return getRandomColor()

def formatCustomXvalues(customXValues, constructions):

    if type(customXValues) == type(np.array([1,2,3])):
        customXValues = [customXValues]

    # if construction length 4 and customXValues length 2, repeat it twice or customXValues length 1, repeat it four times
    # if construction length 5 and customXValues length 3, throw error      
    isCustomXValuesLengthMultipleOfConstructionsLength = len(constructions) % len(customXValues) == 0
    if isCustomXValuesLengthMultipleOfConstructionsLength:
        customXValues = customXValues * int(len(constructions) / len(customXValues))

    elif len(customXValues)!= len(constructions):
        raise invalidInputsException(
            "The length of customXValues must be a multiple of the length of constructions"
        )
    
    return customXValues


def genFigAndAxes(numDimensions, figsize, x, y):
    if numDimensions <= 2:
        fig, axes = plt.subplots( 
            1, numDimensions,
            figsize = figsize
        )
    elif numDimensions > 2:
        fig, axes = plt.subplots( 
            x, y,
            figsize = figsize
        )
    return fig, axes

def formatConstructions(constructions):

    # lambda x : x**2 -> [lambda x: x**2]
    isConstructionsOnlyOneFunction = type(constructions) == type(lambda x : None)
    if isConstructionsOnlyOneFunction:
        constructions = [constructions]
    
    if type(constructions)!= type([]):
        raise invalidInputsException(
            "constructions must be a single function, a list of functions, or a list of lists of functions"
        )
    
    isConstructionsEmpty = len(constructions) == 0
    if isConstructionsEmpty: 
        raise invalidInputsException("No functions provided")
    
    # [lambda x: x**2] -> [[lambda x: x**2]]
    isConstructionsOnlyOneListOfFunctions = areAllElementsInListOfCertainType(constructions, type(lambda x : None))
    if isConstructionsOnlyOneListOfFunctions:
        constructions = [constructions]

    return constructions

def generateEachGraphAxes(numDimensions, axes, xcoord, ycoord):
    if numDimensions == 1:
        ax = axes
    elif numDimensions ==2:
        ax = axes[ycoord]
    else:
        ax = axes[xcoord, ycoord]
    return ax

def FunctionPlotter( 
        constructions: list[list[Callable[[int|float],int|float]]] = [[lambda x: x]], 
        customiseFig:Callable[[Figure],None] = _customiseFigDefault_,
        customiseAxes:Callable[[Axes],None] = _customiseAxesDefault_,
        customiseColors:Callable[[None],None] = _customiseColorsDefault_,
        customXValues: list[np.ndarray] | np.ndarray = [np.arange(-5,5,.01)],
        figsize:tuple = (8,5), #TODO: make sure 2 ints in this tuple
)-> None:
    '''
    FunctionPlotter is a function that takes in a list of functions and creates a plot of them.
    There are many custom settings that are implemented as callbacks

    Parameters:
    constructions: A list of functions that will be plotted. Each element is a list of functions that will be plotted on the same graph.
    customiseFig: A function that takes in a matplotlib figure and can customises it e.g fig.set_color
    customiseAxes: A function that takes in ax (plt.subplots second return value iterated over) and can customise the axes e.g ax.set_facecolor
    customiseColors: Should return a color string e.g random.choice(['#abcabc', '#abcdef'])
    customiseXValues: The x values to be used for each graph. Must be either a single nd array or a list of nd arrays with length a factor of constructions' length (e.g constructions length 4 and customXValues length 2)
    figsize: the figsize parameter passed to plt.subplots 

    extra info on fig, axes and figsize found here: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

    Notes on the graphs:
        - The minimum number of graphs plotted is 4 in an arrangement of (2,2)
        - The plot colors are random
    '''
    #TODO: *args to make a list, a debug mode as well
    
    constructions = formatConstructions(constructions)
    customXValues = formatCustomXvalues(customXValues, constructions)

    numDimensions = len(constructions)
    x, y = calculateDimensions(numDimensions)

    fig, axes = genFigAndAxes(numDimensions, figsize, x, y)
        
    customiseFig(fig)


    for index, graph in enumerate(constructions):

        xValues = customXValues[index]

        isGraphAList = type(graph) == type([])
        if not isGraphAList:
            raise invalidInputsException(f"Graph {graph} is not a list")
        
        
        xcoord, ycoord = getCoordinates(x, y,index)

        ax = generateEachGraphAxes(numDimensions, axes, xcoord, ycoord) 

        customiseAxes(ax)

        for plottingFunction in graph: 

            isplottingFunctionActuallyAFunction = type(plottingFunction) == type(lambda x: None)
            if not isplottingFunctionActuallyAFunction:
                raise invalidInputsException(f"{plottingFunction} is not a function") 
            
            yValues = mapToNPArray(xValues, plottingFunction) 
            ax.plot(xValues, yValues, color=customiseColors()) 

    plt.show()

