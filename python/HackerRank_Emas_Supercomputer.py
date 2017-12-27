# Python Program HackerRank Problem Ema's SuperComputer.
# Code started on 24/12/2017
# Last Edit on 24/12/2017
# Code written by Nabeel Ahmad Khan

import random

# read a line from STDIN
#print("Enter the dimension of the matrix")
input = raw_input()
input_list = [int(n) for n in input.split()]

#print("string entered is ",input)

#for i in input_list:
#    print(i)

grid = []

for i in range(input_list[0]):
    temp = raw_input()
    grid.append(temp)

def checkOverlap(baseX, baseY, area):
    k = 1
    flag = 0
    maxArea = 1
    check = True
    global colorGrid
    if area > 0:
        while (check == True):
            x = baseX
            y = baseY
            if ((colorGrid[baseX - k][baseY] == 0) and (colorGrid[baseX + k][baseY] == 0) and (colorGrid[baseX][baseY + k] == 0) and (colorGrid[baseX][baseY - k] == 0)):
                colorGrid[x][y] = 1
                colorGrid[baseX - k][baseY] = 1
                colorGrid[baseX + k][baseY] = 1
                colorGrid[baseX][baseY + k] = 1
                colorGrid[baseX][baseY - k] = 1
                # print("basex and basey ",x,y)
            else:
                check = False
                flag = 1
            k += 1
            if k > area:
                check = False

        if flag == 0:
            area = 1 + 4 * area
            # print("area is ", area)
            maxArea *= area
    return maxArea


#
# input_list = [5, 6]
# grid = []
# grid.append("GGGGGG")
# grid.append("GBBBGB")
# grid.append("GGGGGG")
# grid.append("GGBBGB")
# grid.append("GGGGGG")

# input_list = [6, 6]
# grid = []
# grid.append("BGBBGB")
# grid.append("GGGGGG")
# grid.append("BGBBGB")
# grid.append("GGGGGG")
# grid.append("BGBBGB")
# grid.append("BGBBGB")

#print(" *** GRID *** ")
## print(grid)

colorGrid = []
for i in range(input_list[0]):
    temp2 = []
    for j in range(input_list[1]):
        temp2.append(0)
    colorGrid.append(temp2)

#print(colorGrid)
maxArea = 1
plus = list()
plusDictionary = {}

for i in range(1,input_list[0] - 1):
    for j in range(1, input_list[1] - 1):
        check = True
        baseX = i
        baseY = j
        k = 1
        count = 0
        while(check == True):
            if(((baseX - k) >= 0) and ((baseX + k) < input_list[0])):
                if( (grid[baseX - k][baseY] == grid[baseX + k][baseY]) and (grid[baseX][baseY] ==  grid[baseX - k][baseY]) ):
                    #print("__1__")
                    count += 1
                    k += 1
                else:
                    check = False
            else:
                check = False

            #print("__4__")
        check = True
        baseX = i
        baseY = j
        k = 1
        count2 = 0
        #print("__2__")
        while(check == True):
            if(((baseY - k) >= 0) and ((baseY + k) < input_list[1])):
                if( (grid[baseX][baseY - k] == grid[baseX][baseY + k]) and (grid[baseX][baseY] == grid[baseX][baseY - k]) ):
                    #print("__3__")
                    count2 += 1
                    k += 1
                else:
                    check = False
            else:
                check = False

        area = min(count, count2)
        #print("area is ", area, baseX, baseY)
        tempArea = 1 + 4 * area
        check = True
        flag2 = 0
        if area>0:
            l = 0
            while(l < len(plus)):
                if area > plus[l][2]:
                    plus.insert(l+1, [baseX, baseY, area])
                    flag2 = 1
                l += 1
            if flag2 == 0:
                plus.append([baseX, baseY, area])

#print("PLUS IS ",plus)

finalArea = 0
loop = 0
while(loop < len(plus)):
    for i in range(len(plus)):
        #print(tempvalue[0], tempvalue[1], plus[i])
        result = checkOverlap(plus[i][0], plus[i][1], plus[i][2])
        #print("in the loop 2")
        if result>1:
            maxArea *= result
    if maxArea > finalArea:
        finalArea = maxArea
    #print("in the loop")
    random.shuffle(plus)
    loop += 1


#print("All the pair are ",plusDictionary)
print(finalArea)