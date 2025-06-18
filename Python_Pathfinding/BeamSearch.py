def searchAlgorithm(grid, start, goal):
    MAX_Q = 200
    # Create a queue using a list
    queue = []
    
    #add the start to the queue to begin the algorithm
    queue.append(start) 
    
    # Create a dictionary to store the distance to each node
    distance = {}
    distance[start] = 0
    
    # Create Disctionary for Parent Nodes
    parent = {}
    parent[start] = None
    
    # Create a set to store the visited nodes
    visited = set()
    
    def mysort(self):
        return distance[self]
    
    # While there are nodes in the queue do these steps
    while queue:
        # Get the next node
        current = queue.pop(0)
        
        # If the current node is the goal, we are done
        if current == goal:
            return path(parent, goal)
        
        if current in visited:
            continue
        
        # Mark the current node as visited and increment states
        visited.add(current)
        
        # Get the neighbors of the current node
        for next_node in neighbors(grid, current):
            # Skip visited nodes
            if next_node in visited:
                continue
            
            # Add the next node to the queue
            queue.append(next_node)
            
            # Update the distance to the next node
            distance[next_node] = distance[current] + 1
            
            # Update the parent Dictionary
            parent[next_node] = current
        if len(queue) > MAX_Q:
            wqueue = []
            queue.sort(key = mysort)
            num = 0
            for i in queue:
                wqueue.append(queue[num])
                num += 1
                if num == MAX_Q:
                    break
            for node in wqueue:
                # Get the next node
                current = wqueue.pop(0)
        
                # If the current node is the goal, we are done
                if current == goal:
                    return path(parent, goal)
        
                if current in visited:
                    continue
        
        # Mark the current node as visited and increment states
                visited.add(current)
        
        # Get the neighbors of the current node
                for next_node in neighbors(grid, current):
            # Skip visited nodes
                    if next_node in visited:
                        continue
            
            # Add the next node to the queue
                    queue.append(next_node)
            
            # Update the distance to the next node
                    distance[next_node] = distance[current] + 1
            
            # Update the parent Dictionary
                    parent[next_node] = current
                
                
            
            
    return path(parent, goal)



# This code generously provided by ChatGPT, credit goes to OpenAI for making such a good chat bot.
def neighbors(grid, node):
    x, y = node
    results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
    results = filter(lambda x: 0 <= x[0] < len(grid[0]) and 0 <= x[1] < len(grid), results)
    return results


def path(parents, goal):
    path = [goal]
    current = goal
    while current in parents:
        current = parents[current]
        path.append(current)
    path.pop
    return list(reversed(path))