def PrintTheBoard(arr):
    print("Printing board")
    for i in range(3):
        print(arr[i])

if __name__ == "__main__":
    arr = [['-' for i in range(3)] for j in range(3)]
    PrintTheBoard(arr)
