################################################### Functions Definitions ##################################################

def showMaze(Arr):                                                                  # Temporary Maze Display function
    print("\nThe maze is as follows:")
    print("_" * (len(Arr[0]) + 4))
    print("| " + " " * len(Arr[0]) + " |")
    for disp in Arr:
        print("| " + disp + " |")
    print("|_" + "_" * len(Arr[0]) + "_|")
    print("\n")
    return

####################################################### Main Program #######################################################

# Initializing variables
initial = -1

# Inputting the file location and serial number of maze to be solved from user
fileDirect = str(input("\nEnter the file location of the maze: "))
mazeNum = int(input("Enter the serial number of the maze that needs to be solved: "))
print("\n")

# Opening file in read mode
if(fileDirect == "") or (fileDirect == " "):
    mazeFile = open("maze1.txt", "r")
else:
    mazeFile = open(fileDirect, "r")

# Reading the maze from the file and inputting into an array for program
mazeArr = mazeFile.readlines()

for r in range(0, len(mazeArr), 1):                                                 # Only including the mazeNum-th maze in the file
    if(mazeArr[r] == str(mazeNum) + "\n"):
        initial = r+1
    elif((mazeArr[r] == '\n') or (mazeArr[r] == '')) and (initial > -1):            # Stops the matrix slicing if there is 1 or 2 extra newline characters after last maze
        mazeArr = mazeArr[initial:r]
        break
    elif(r == len(mazeArr)-1):                                                      # Stops the matrix slicing if last line in text file is reached
        mazeArr = mazeArr[initial:r+1]

for i in range(0, len(mazeArr), 1):
    if(mazeArr[i][-1] == '\n'):                                                     # Removes the trailing '\n' from each row in the maze
        mazeArr[i] = mazeArr[i][:-1]
    if(i > 0) and (len(mazeArr[i]) != len(mazeArr[i-1])):                           # Checks if all rows of the maze are equal in length one by one
        print("ERROR: Maze not of equal sized rows\n")
        quit()

showMaze(mazeArr)

mazeFile.close()