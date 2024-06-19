def row_winner(d):
    y = 0
    for i in range(1,grid*grid + 1, grid):
        flag = True
        for j in range(grid):
            y+=1
            if d[y]!=d[i] or d[y]=='-':
                flag = False
                break
        if flag:
            return True
    return False

def col_winner(d):
    for j in range(1, grid+1):
        flag = True
        for i in range(j, grid* grid + 1, grid):
            if d[i]!=d[j] or d[j] == '-':
                flag = False
                break
        if flag:
            return True
    return False
def dia_winner(d):
    flag = True
    for i in range(1,grid*grid + 1 , grid+1):
        if d[i]!=d[1] or d[1]=='-':
            flag = False
            break
    if flag:
        return True
    flag = True
    for j in range(grid,grid*grid - (grid-2) , grid-1):
        if d[j]!= d[grid] or d[grid]=='-':
           flag = False
           break
    if flag:
        return True
    else:
        return False



grid = int(input("select grid size:"))
d = {}
for key in range(1,grid*grid+1):
    d[key]= '-'

m = 0
while m < grid*grid:
    player = 'not valid'
    while player != 'valid':
        player = int(input())
        if player not in d or d[player]!='-':
            print('add again')
        else:
            if m %2==0:
                d[player]= 'O'
                
            else:
                d[player]= 'X'
            player= 'valid'
    y = 0
    for i in range(grid):
        for j in range(grid):
            y += 1
            print(d[y],end='')
        print()
    if row_winner(d) or col_winner(d) or dia_winner(d):
        if m %2 == 0:
            print('player1 won')
            break
        else:
            print('player2 won')
            break
    m+=1
    
        

