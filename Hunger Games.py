#####################################################################
# Hunger Games
#####################################################################
import sys

def main():
    print("test1")
    playerList = initGame(1)

    print(playerList)
    pass

def initGame(numOfDistricts=12):
    districtNum = 1
    playerList = []
    print("test")
    while (districtNum <= numOfDistricts):
        print("District",districtNum)
        player1 = input("Enter your first volunteer:  ")
        player2 = input("Enter your second volunteer: ")
        print(player1, "and", player2, "have been entered into District", districtNum)
        print("\n")
        
        # Add the district to the playerList
        playerList.append([player1, player2])

        districtNum += districtNum
    
    return playerList

class Player:
    def __init__(self):
        pass

if __name__ == "__main__":
    main()