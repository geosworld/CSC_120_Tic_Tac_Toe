def PrintTheBoard(arr):
    print("Printing board..")
    for i in range(3):
        print(arr[i])

def draw(arr):
    for row in arr:
        if '-' in row:
            return False
    print("Draw")
    return True

def winning(arr):
    for row in range(3):
        if arr[row][0]==arr[row][1] and arr[row][1]==arr[row][2] and arr[row][2]=='O':
            print("Player 1 Wins")
            return True
        elif arr[row][0]==arr[row][1] and arr[row][1]==arr[row][2] and arr[row][2]=='X':
            print("Player 2 Wins")
            return True
    for col in range(3):
        if arr[0][col]==arr[1][col] and arr[1][col]==arr[2][col] and arr[2][col]=='O':
            print("Player 1 Wins")
            return True
        elif arr[0][col]==arr[1][col] and arr[1][col]==arr[2][col] and arr[2][col]=='X':
            print("Player 2 Wins")
            return True


    if arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2] and arr[2][2]=='O':
        print("Player 1 Wins")
        return True
    elif arr[0][0]==arr[1][1] and arr[1][1]==arr[2][2] and arr[2][2]=='X':
        print("Player 2 Wins")
        return True
    elif arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0] and arr[2][0]=='O':
        print("Player 1 Wins")
        return True
    elif arr[0][2]==arr[1][1] and arr[1][1]==arr[2][0] and arr[2][0]=='X':
        print("Player 2 Wins")
        return True

    return False

if __name__ == "__main__":
    arr = [['-' for i in range(3)] for j in range(3)]
    PrintTheBoard(arr)
    player=1
    while(True):
        if player==1:
            row=int(input("Player "+str(player)+" row: "))
            col=int(input("Player "+str(player)+" col: "))
            if row in range(3) and col in range(3):
                if arr[row][col]=='-':
                    arr[row][col]='O'
                    PrintTheBoard(arr)
                    player=2
                    if winning(arr) or draw(arr):
                        break
                else:
                    print("Location is not empty")
            else:
                print("Invalid Location")
        else:
            row=int(input("Player "+str(player)+" row: "))
            col=int(input("Player "+str(player)+" col: "))
            if row in range(3) and col in range(3):
                if arr[row][col]=='-':
                    arr[row][col]='X'
                    PrintTheBoard(arr)
                    player=1
                    if winning(arr) or draw(arr):
                        break
                else:
                    print("Location is not empty")
            else:
                print("Invalid Location")

