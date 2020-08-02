from recognizedInput import messageCommandDict, hiddenCommandDict


class Roster():

    def __init__(self, name, size, admin):

        self.__name = str(name)
        self.__slots = int(size)
        self.__admin = str(admin)

        self.validRoster = self.__processInput(name, size)

        self.__waitListSlots = self.__slots // 2
        self.__registeredPlayers = ["OPEN SLOT"] * (self.__slots + self.__waitListSlots)
        self.__registeredPlayerIDs = ["OPEN SLOT"] * (self.__slots + self.__waitListSlots)


    def getName(self):
        return self.__name

    def getPlaySlots(self):
        return self.__registeredPlayers

    def getSlots(self):
        return self.__slots

    def getWaitSlots(self):
        return self.__waitListSlots

    def getIDs(self):
        return self.__registeredPlayerIDs

    def getAdmin(self):
        return self.__admin

    def isAdmin(self, author):
        if author == self.__admin or author == "Raysparks#1042":
            return True
        return False


    def __processInput(self, name, size):
        if name in list(messageCommandDict.keys()) or name in list(hiddenCommandDict.keys()) or name.lower() == "newroster":
            return "Name error"
        elif int(size) <= 1 or int(size) > 20:
            self.__slots = 10
            return "Size error"
        elif "@everyone" in name or "@here" in name:
            return ">:("
        else:
            return "No error"


    def setSlots(self, newSlots):
        if newSlots >= 2 and newSlots <= 20:
            self.__waitListSlots = ((newSlots + 1) // 2)
            self.__slots = newSlots + self.__waitListSlots

            # add slots
            if self.__slots > len(self.__registeredPlayers):
                for i in range(len(self.__registeredPlayers), self.__slots):
                    self.__registeredPlayers.append("OPEN SLOT")
                    self.__registeredPlayerIDs.append("OPEN SLOT")

            # subtract slots
            elif self.__slots - 1 < len(self.__registeredPlayers):
                slotsToRemove = (len(self.__registeredPlayers) - self.__slots)

                # subtract slots from registered List
                self.__registeredPlayers = self.__registeredPlayers[:slotsToRemove * -1]
                self.__registeredPlayerIDs = self.__registeredPlayerIDs[:slotsToRemove * -1]
            return True
        else:
            return False


    def registerPlayer(self, player, playerID=""):

        # check if player is already registered
        if player in self.__registeredPlayers or playerID in self.__registeredPlayerIDs:
            return False

        for i, j in enumerate(self.__registeredPlayers):
            if j == "OPEN SLOT" and str(player):
                self.__registeredPlayers[i] = player
                if playerID == "":  # no player ID provided
                    self.__registeredPlayerIDs[i] = player
                else:
                    self.__registeredPlayerIDs[i] = str(playerID)
                return True
            continue
        return False


    def attemptRegistery(self, player, playerID=""):
        if "@everyone" in player or "@here" in player:
            return ">:("

        if self.registerPlayer(player, playerID):
            return "R"
        else:
            return "X"


    def removePlayer(self, player):
        if player in self.__registeredPlayers or player in self.__registeredPlayerIDs:
            try:
                playerIndex = self.__registeredPlayers.index(player)
            except:
                playerIndex = self.__registeredPlayerIDs.index(player)
            self.__registeredPlayers.pop(playerIndex)
            self.__registeredPlayerIDs.pop(playerIndex)
            self.__registeredPlayers.append("OPEN SLOT")
            self.__registeredPlayerIDs.append("OPEN SLOT")
            return True

        return False


    def displayPlayers(self):
        # see all registered players without alerting them
        outPut = "**__" + str(self.__name) + "__**\n**REGISTERED**\n"
        for i in range(0, len(self.__registeredPlayers) - self.__waitListSlots):
            outPut += str(self.__registeredPlayers[i]) + "\n"
        outPut += "-------------------------\n**WAITING LIST**\n"
        for i in range(len(self.__registeredPlayers) - self.__waitListSlots, len(self.__registeredPlayers)):
            outPut += str(self.__registeredPlayers[i]) + "\n"
        outPut += "\n**Use \"!" + self.__name + " join\" to add your name to the roster, or use \"!" + self.__name + \
                  " leave\" to remove your name. Use \"!rosterHelp\" to see a full list of roster commands.**"
        return outPut

    def alertPlayers(self):
        # alert all registered players
        outPut = "**__" + str(self.__name) + "__**\n**REGISTERED**\n"
        for i in range(0, len(self.__registeredPlayerIDs) - self.__waitListSlots):
            outPut += str(self.__registeredPlayerIDs[i]) + "\n"
        outPut += "-------------------------\n**WAITING LIST**\n"
        for i in range(len(self.__registeredPlayerIDs) - self.__waitListSlots, len(self.__registeredPlayerIDs)):
            outPut += str(self.__registeredPlayerIDs[i]) + "\n"
        return outPut
