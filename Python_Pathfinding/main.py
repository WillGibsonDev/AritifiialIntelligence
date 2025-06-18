import BreadthFirstSearch
import BeamSearch
        
# Pretty cool to be able to quickly open the entire file as a 2D List
with open('MapBig.txt') as file:
    cols = file.read(2)
    file.read(1)
    rows = file.read(2)
    grid = [list(line.strip()) for line in file]
    grid.pop(0)

    

start = (0, 0)
end = (int(cols)-1, int(rows)-1)

path = BeamSearch.searchAlgorithm(grid, start, end)
path.pop(0)

for coord in path:
    x, y = coord
    grid[y][x] = "."
    
    
for row in grid:
    print(row)


print("")
print(path)

