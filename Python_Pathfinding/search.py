import pandas as pd
import numpy as np
import sys
import queue as Q
import heapq
import time


##:::::::::::::::::::::##
##::::::CMD ARGS:::::::##
##:::::::::::::::::::::##
if len(sys.argv) < 7:
    print("Args\n<map.txt> <startX> <startY> <goalX> <goalY> <search stratagy>")
    sys.exit()

file = sys.argv[1]
start = tuple((int(i) for i in sys.argv[2:4]))
goal = tuple((int(i) for i in sys.argv[4:6]))
search = sys.argv[6]



##:::::::::::::::::::::##
##::::read in files::::##
##:::::::::::::::::::::##
df=pd.read_csv(file)
cols,rows = str(df.columns[0]).split(" ")
cols = int(cols)
rows = int(rows)
map = df[df.columns[0]].str.split("",expand=True).values[:,1:-1]

start_time = time.time()

##:::::::::::::::::::::##
##::::Graph classes::::##
##:::::::::::::::::::::##
class Graph:

    class Node:
        def __init__(self, Graph, x_y, parent, path_cost, depth):
            self.selfGraph = Graph
            self.state = x_y
            self.parent = parent
            self.path_cost = path_cost
            self.depth = depth
            self.comparitor = self.selfGraph.comparitor

        def __lt__(self,other):
            return self.comparitor(self,other)


        def __str__(self):
            return "X,Y:{}   pathCost:{}   Depth:{}".format(self.state,self.path_cost,self.depth)

    #breath First Search
    def __init__(self,start,goal,mapSize,comparitor):
        self.start = start
        self.goal = goal
        self.mapSize = mapSize
        self.state_visited = 0
        self.comparitor = comparitor

        self.goal_Node = None
        
    def expand_function(self, node_to_expand:Node):
        x,y = node_to_expand.state
        
        newNodes_xy = []
        
        #up
        if (x,y+1) not in self.explored:
            if y + 1 < self.mapSize[1]:
                if cost_func(x,y+1) != -1:
                    newNodes_xy.append((x,y+1))

        #right
        if (x+1,y) not in self.explored:
            if x+1 < self.mapSize[0]:
                if cost_func(x+1,y) != -1:
                    newNodes_xy.append((x+1,y))


        #down
        if (x,y-1) not in self.explored:
            if y - 1 > 0:
                if cost_func(x,y-1) != -1:
                    newNodes_xy.append((x,y-1))


        #left  
        if (x-1,y) not in self.explored:
            if x - 1 > 0:
                if cost_func(x-1,y) != -1:
                    newNodes_xy.append((x-1,y))


        newNodes = []         
        for x_y in newNodes_xy:
            cost = cost_func(x_y[0],x_y[1])

            
            #print(node_to_expand)
            try:
                full_path_cost = node_to_expand.path_cost + cost
            except:
                print(node_to_expand)
                print(x_y)
                print(cost)
                full_path_cost = node_to_expand.path_cost + cost
                
            depth = node_to_expand.depth + 1
            newNodes.append(self.Node(self,x_y,node_to_expand,full_path_cost,depth))

        return newNodes

    def uniform_cost_search(self):
        start_node = self.Node(Graph=self,x_y=self.start,parent=None,path_cost= 0,depth=0)
        
        #q=beamSearchQueue(10)
        q=Q.PriorityQueue()
        q.put(start_node)

        self.explored = set()
        self.explored.add(start_node.state)
        
        while not q.empty():
            node = q.get()
            self.state_visited +=1
            
            ###
            #print(node)
            ###
            if node.state == self.goal:
                self.goal_Node = node
                return

            

            children = self.expand_function(node)
            
            for child in children:
                q.put(child)
                self.explored.add(child.state)
                    
        # self.goal_Node = node
        print("failed to find path")
        return

    def printPath(self):
        if self.goal_Node is None:
            print("Please run uniformed_cost_search")
            return
        
        pathMap = map.copy()

        for cord in self.explored:
            pathMap[cord[1]][cord[0]] = map[cord[1]][cord[0]]+'▒'

        temp = self.goal_Node
        pathLength = 0

        while temp is not None:
            pathLength += 1
            pathMap[temp.state[1]][temp.state[0]] = map[temp.state[1]][temp.state[0]]+'█'
            temp = temp.parent




        stringMap = '\n'.join(["  ".join(row)  for row in pathMap.tolist()])
        stringMap = stringMap.replace('█ ','█')
        stringMap = stringMap.replace('▒ ','▒')
        header = "State Visitied: {}\n".format(self.state_visited)
        header += "Path Length: {}\n".format(pathLength)
        header += "Path Cost: {}\n".format((self.goal_Node.path_cost))
        header += "Runtime: {}\n".format((time.time() - start_time))

        

        with open("out.txt", "w") as text_file:
            text_file.write(header + stringMap)

        print(header)
        print(stringMap)
        return

def cost_func(x,y=None):
    
    if y is None:
        letter = x
    else:
        letter = map[y,x]

    if letter == 'R':
        return 1
    if letter == 'f':
        return 2
    if letter == 'F':
        return 4
    if letter == 'h':
        return 5
    if letter == 'r':
        return 7
    if letter == 'M':
        return 10
    if letter == 'W':
        return -1

#see line 122 to enable/disable
class beamSearchQueue:
    def __init__(self,max_size=5):
        self.max_size = max_size
        self.Q = []
        heapq.heapify(self.Q)

    def put(self, element):
        if len(self.Q) < self.max_size:
            heapq.heappush(self.Q, element)
        else:
            heapq.heappush(self.Q, element)
            self.Q = heapq.nsmallest(self.max_size,self.Q)


    def get(self):
        return heapq.heappop(self.Q)

    def empty(self):
        return len(self.Q) == 0

#dijktras
def BestFirstSearch(self, other):
    return self.path_cost < other.path_cost

#DFS
def DepthFirstSearch(self,other):
    return self.depth > other.depth

#BFS
def BreathFirstSearch(self,other):
    return self.depth < other.depth

#h(s) = manhaten distance
def AStarSearch(self,other):
    gn1 = self.path_cost
    gn2 = other.path_cost

    #manhatten a* distance
    
    hn1 = ((cols - self.state[0]) + (rows - self.state[1]))
    hn2 = ((cols - other.state[0]) + (rows - other.state[1]))


    return gn1 + hn1 < gn2 + hn2

#h(s) = manhaten weights (not optimal)
def AStarSearch3(self,other):
    gn1 = self.path_cost
    gn2 = other.path_cost

    #manhatten a* distance
    weight = 1.2
    hn1 = ((cols - self.state[0]) + (rows - self.state[1]))
    hn2 = ((cols - other.state[0]) + (rows - other.state[1]))


    return gn1 + hn1*weight < gn2 + hn2*weight

#h(s) = weighted A* with manhaten distance 
def AStarSearch2(self,other):
    gn1 = self.path_cost
    gn2 = other.path_cost

    #manhatten a* distance
    lookAhead = 100
    hn1 = ((cols - self.state[0]) + (rows - self.state[1]))*1 
    hn2 = ((cols - other.state[0]) + (rows - other.state[1]))*1 
    
    hn1 += np.vectorize(cost_func)(map[self.state[1],self.state[0]:self.state[0] + lookAhead]).sum() + np.vectorize(cost_func)(map[self.state[1]: self.state[1] + lookAhead,self.state[0]]).sum()
    hn2 += np.vectorize(cost_func)(map[other.state[1],other.state[0]:other.state[0] + lookAhead]).sum() + np.vectorize(cost_func)(map[other.state[1]:other.state[1] + lookAhead,other.state[0]]).sum()

    return gn1 + hn1 < gn2 + hn2


#DO NOT USE THIS IS IT VERY BROKEN STILL (And will probably remain broken on the final submission, because i can't figure this out...)
def BeamSearch(starting, goalPoint):
    found = False
    curr = starting
    if curr == goalPoint:
        found = True
    else:
        x, y = curr
        x += 1


#default is DFS

comparitorFunct = DepthFirstSearch
if search == '-b':
    comparitorFunct = BreathFirstSearch

elif search == '-l':
    comparitorFunct = BestFirstSearch

elif search == '-a1':
    comparitorFunct = AStarSearch

elif search == '-a2':
    comparitorFunct = AStarSearch3

# elif search == '-i':
#     comparitorFunct = DepthFirstSearch
#     #requires additonal changes to the Graph function


# elif search == '-ia':
#     comparitorFunct = DepthFirstSearch
#     #requires additonal changes to the Graph function


start = (0,0)
goal = (cols-1,rows-1)


#now we start running everything
myGraph = Graph(start,goal,(cols,rows),comparitorFunct)

#this is where all the computation happens
myGraph.uniform_cost_search()

#print to console and to out.txt
myGraph.printPath()

