# input
n = int(input("Enter value of n: "))
# vars
num = 1             # starting number
sq = n*n            # ending number
# list init
l = []
for _ in range(0,n):
    l.append([None]*n)

row,col = 0,0
dir = [[0,1],[1,0],[0,-1],[-1,0]]
movement = 0

while num <= sq:
    l[row][col] = num

    trow = row + dir[movement][0]
    tcol = col + dir[movement][1]
    
    # if current pos is empty and in list range
    if 0 <= trow < n and 0 <= tcol < n and l[trow][tcol] == None:
        row = trow
        col = tcol
        
    else:
        movement = (movement + 1) % 4    # change dir
        row += dir[movement][0]
        col += dir[movement][1]

    num += 1

for i in l:
    for j in i:
        print(j,end=" ")
    print()



