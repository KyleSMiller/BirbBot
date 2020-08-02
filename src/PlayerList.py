from voiceLines import NoOneHere, Sorry


class PlayerList:

    def __init__(self, players):
        self.__players = players
        self.__playerList = "__**PLAYER LIST:**__\n"
        self.__formatPlayerList()

    def __str__(self):
        return self.__playerList

    def getPlayers(self):
        return self.__players

    def checkFor(self, player):
        # check if player is in the player list
        return player in self.__players

    def __formatPlayerList(self):
        if len(self.__players) == 0:  # player list is empty
            self.__playerList += NoOneHere().getResponse()
        else:  # player list is populated
            for playerNum, player in enumerate(self.__players):
                if playerNum % 4 == 0 and playerNum != 0:
                    self.__playerList += "\n"
                self.__playerList += player + "  |  "