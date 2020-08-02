from resources.passwords import queryLoginUsername, queryLoginPassword
from PlayerList import PlayerList

import json

# Gracious Welcome:  66.151.138.224:3170  "http://refactor.jp/chivalry/?serverId=1194830"
# Gracious Map Votes:  66.151.138.198:6000  "http://refactor.jp/chivalry/?serverId=1301262"

class ServerInfo:

    def __init__(self, dataDict):
        """
        Gather all provided data from the passed in dictionary, filling in the gaps when necessary
        :param dataDict:  dictionary of server data
        """
        if "Status" in dataDict.keys():
            self.__status = dataDict["Status"]
        else:
            self.__status = "Unknown Status"
        if "IP" in dataDict.keys():
            self.__ip = dataDict["IP"]
        else:
            self.__ip = "Unknown IP"
        if "Name" in dataDict.keys():
            self.__name = dataDict["Name"]
        else:
            self.__name = "Unknown Server"
        if "Game" in dataDict.keys():
            self.__game = dataDict["Game"]
        else:
            self.__game = "Unknown Game"
        if "Game Type" in dataDict.keys():
            self.__gameType = dataDict["Game Type"]
        else:
            self.__gameType = ""
        if "Map" in dataDict.keys():
            self.__map = dataDict["Map"]
        else:
            self.__map = "Unknown Map"
        if "Population" in dataDict.keys():
            self.__population = dataDict["Population"]
        else:
            self.__population = "?/?"
        if "Player List" in dataDict.keys():
            self.__playerList = PlayerList(dataDict["Player List"])
        else:
            self.__playerList = PlayerList("SKIP")

        self.__admins = [
            "Baron voŋ Moorland",
            "Raysparks",
            "Sir Boring",
            "Herbanator",
            "Jalen♡",
            "The Flying Flail",
            "Rosy",
            "ZedHead",
            "SomeDuke",
            "J",
            "Beständig",
            "bone",
            "flask",
            "『Sushiki』",
            "Walkin",
            "Eggplant",
            "Tez",
            "[FOR] Reason",
            "Goog",
            "ducksauce",
            "P",
            "Thaedius",
            "Marlop",
            "ムgòn Đominus"
        ]


    def getStatus(self):
        return self.__status

    def getIP(self):
        return self.__ip

    def getName(self):
        return self.__name

    def getGame(self):
        return self.__game

    def getGameType(self):
        return self.__gameType

    def getMap(self):
        return self.__map

    def getPopulation(self):
        return self.__population

    def getPlayerList(self):
        return self.__playerList


    def __str__(self):
        """
        Gather server name, map, population, gameType, and playerList and return it in a formatted string
        :return:  Formatted string of server info
        """
        return self.__formatInfo()

    def isInServer(self, player):
        """
        Check the server for a specific player
        :param player  The player to check the server for
        :return        True if player is currently connected to server, False if not currently connected
        """
        if "•҉" in player:  # remove the moorlands flowery from name
            floweryPosition = player.find("҉")
            strippedPlayer = player[:floweryPosition] + player[floweryPosition + 1:]
            return self.__playerList.checkFor(strippedPlayer)
        if "❊" in player:  # remove mordhau flowery from name
            floweryPosition = player.find("❊")
            strippedPlayer = player[:floweryPosition] + player[floweryPosition + 1:]
            return self.__playerList.checkFor(strippedPlayer)

    def isAdminInServer(self):
        """
        Check the server for an administrator
        :return  True if an admin is currently connected, False if none are currently connected
        """
        for admin in self.__admins:
            if self.__playerList.checkFor(admin):
                return True
        return False

    def __getCurrentPlayers(self):
        """
        Get the number of players currently on the server
        :return  int of current players
        """
        currentPlayers = self.__population.split("/")[0]
        return int(currentPlayers)

    def __getMaxPlayers(self):
        """
        Get the maximum number of players the server supports
        :return  int of maximum players allowed on the server
        """
        playerCountRaw = self.__population
        maxPlayers = playerCountRaw.split("/")[1]
        return int(maxPlayers)

    def __formatInfo(self):
        """
        Format all the retrieved server info into a response for BirbBot
        :return String     the formatted server info response that BirbBot will present
        """
        if self.__status == "Offline":
            return "**" + str(self.__name) + "** appears to be offline!"
        formattedInfo = ("**" + str(self.__name) + "** is playing **"
                         + str(self.__gameType) + str(self.__map) + "** with a population of **"
                         + "(" + str(self.__population) + ")**")
        formattedInfo += "\n" + str(self.__playerList)
        return formattedInfo



class ChivalryServerInfo(ServerInfo):
    def __init__(self, dataDict):
        super(ChivalryServerInfo, self).__init__(dataDict)

    @staticmethod
    def getGameName():
        """
        :return: String  The name of the game this ServerInfo class is designed for
        """
        return "Chivalry: Medieval Warfare"

    def __str__(self):
        return self.__formatInfo()

    def __formatInfo(self):
        """
        Format all the retrieved server info into a response for BirbBot
        :return String     the formatted server info response that BirbBot will present
        """
        if self.getStatus() == "Offline":
            return "**" + str(self.getName()) + "** appears to be offline!"
        formattedInfo = ("**" + str(self.getName()) + "** is playing **"
                         + str(self.getMap()) + "** with a population of **"
                         + "(" + str(self.getPopulation()) + ")**")
        formattedInfo += "\n" + str(self.getPlayerList())
        return formattedInfo



class MordhauServerInfo(ServerInfo):
    def __init__(self, dataDict):
        super(MordhauServerInfo, self).__init__(dataDict)

    @staticmethod
    def getGameName():
        """
        :return: String  The name of the game this ServerInfo class is designed for
        """
        return "Mordhau"

    def __str__(self):
        return self.__formatInfo()

    def __formatInfo(self):
        """
        Format all the retrieved server info into a response for BirbBot
        :return String     the formatted server info response that BirbBot will present
        """
        if self.getStatus() == "Offline":
            return "**" + str(self.getName()) + "** appears to be offline!"
        formattedInfo = ("**" + str(self.getName()) + "** is playing **"
                         + str(self.getGameType()) + str(self.getMap()) + "** with a population of **"
                         + "(" + str(self.getPopulation()) + ")**")
        formattedInfo += "\nJoin it with **open " + str(self.getIP()) + "**"
        return formattedInfo



serverInfoTypes = [ChivalryServerInfo, MordhauServerInfo]