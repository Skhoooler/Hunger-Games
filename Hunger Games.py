#####################################################################
# Hunger Games
#####################################################################
import sys

def main():
    playerList, numOfPlayers = initGame(1)

    print("###########################################################")
    print("#                                                         #")
    print("#              Let the Hunger Games Begin                 #")
    print("#                                                         #")
    print("###########################################################")
    print("\n")
    dayNum = 1
    while(numOfPlayers > 1):
        deadPlayers = nextDay(dayNum)
        
        dayNum += 1
        numOfPlayers -= deadPlayers


def nextDay(dayNum):
    print("###################  Dawn of Day", dayNum," ######################")
    deadPlayers = 1

    # Stuff here

    return deadPlayers

def initGame(numOfDistricts=12):
    districtNum  = 1
    numOfPlayers = 0
    playerList = []

    while (districtNum <= numOfDistricts):
        print("District",districtNum)
        playerOneName = input("Enter your first volunteer:  ")
        playerTwoName = input("Enter your second volunteer: ")
        
        # Create the players in the district
        player1 = Player(playerOneName, 69)
        player2 = Player(playerTwoName, 420)
        numOfPlayers += 2

        # Make them allies
        player1.setAlly(player2)
        player2.setAlly(player1)

        print(player1.name, "and", player2.name, "have been entered into District", districtNum)
        print("\n")
        
        # Add the district to the playerList
        playerList.append([player1, player2])

        districtNum += 1
    
    return playerList, numOfPlayers

class Player:
    def __init__(self, name, health=5):
        self.name    = name
        self.health  = health
        self.allies  = [] # tried passing this in via the constructor, but it got kind of awkward with setting allies in initGame()
        self.enemies = [] # Players don't have enemies at the start of the game
    
    def setHealth(self, health):
        self.health = health

    def setAlly(self, ally):
        self.allies.append(ally)
    
    def setEnemy(self, enemy):
        self.enemies.append(enemy)

if __name__ == "__main__":
    main()