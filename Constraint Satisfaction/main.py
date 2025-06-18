import pandas as pd
import numpy as np
import sys

# Agruments are fun, and actually super simple in python.
if len(sys.argv) < 2:
    print("Args\n<map.txt>")
    sys.exit()
    
    
file = sys.argv[1]
# file = "australia.txt" # USED FOR TESTING
df = pd.read_csv(file, sep=',', header=None)
# print(df.values) # USED FOR TESTING

# Set up Node class (Deprecated)
class Node:
    name = ""
    adjacent = []
    
    def __init__(self, name, adjacent) -> None:
        self.name = name
        self.adjacent = adjacent
        
    def __str__(self) -> str:
        return f"Name: {self.name} Adjactent: {self.adjacent}"
    
    
# Set up a list of locations, used for defining nodes later
locationList = []
for locale in df[0]:
    locationList.append(locale)
   
# Set up a list of nodes
nodeList = []   

# Turn the file into rows of nodes
countRow = 0
for row in df:
    tempListAdjactent = []
    if countRow == 0:
        countRow += 1
        continue
    countColumn = 0
    for column in df[countRow]:
        if countColumn == 0:
            countColumn += 1
            continue
        if df[countRow][countColumn] == '0':
            countColumn += 1
            continue
        elif df[countRow][countColumn] == '1':
            tempListAdjactent.append(locationList[countColumn])
            countColumn += 1
        else:
            print("ERROR IN DEFINING ADJACENT")
            
            
    nodeList.append(Node(str(df[countRow][0]), tempListAdjactent))
    tempListAdjactent.clear
    countRow += 1

# Turn the list of ndoes into a dictionary, super simple change due to the node class. 
graph = {}
for i in nodeList:
    graph[i.name] = set(i.adjacent)
    

####################################
####################################
# ----- FINISHED WITH SET UP ----- #
####################################
####################################


color_map = {}

def color_node(node, color):
    # check if any of the neighbors have the same color
    for neighbor in graph[node]:
        neighbor_color = color_map.get(neighbor)
        if neighbor_color == color:
            return False
    # if none of the neighbors have the same color, color the node and return True
    color_map[node] = color
    return True

# Finds the least number of colors needed to color the graph
def find_least_colors():
    # define a dictionary to store the locations associated with each color
    color_locations = {}
    
    # define a list of colors to use (Swapped colors for numbers so output looks the same as in assignment)
    colors = ['1', '2', '3', '4', '5', '6']
    
    # iterate over the nodes and color them
    for node in graph:
        # try to color the node with each color in the list until successful
        for color in colors:
            if color_node(node, color):
                # add the location to the list of locations associated with the color
                color_locations.setdefault(color, []).append(node)
                break
            
    # return the number of distinct colors used and the color locations
    return len(set(color_map.values())), color_locations

# call the function to find the least number of colors needed to color the graph and the associated locations
least_colors, color_locations = find_least_colors()


# print the result
print("=======")

print(f"The least number of colors needed to color the graph is {least_colors}")
for color, locations in color_locations.items():
    print(f"{color} : {', '.join(locations)}")

print("=======")