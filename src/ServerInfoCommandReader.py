from ServerInfo import *

import json

class ServerInfoCommandReader:
    def __init__(self, serverDataFile):
        self.__serverDataFile = serverDataFile
        self.__servers = []

    def getAllInfo(self):
        """
        Retrieve the information from a set of servers
        :return: String  The formatted information from all servers
        """
        self.__readServerData()
        return self.__formatServerDataSet()

    def __formatServerDataSet(self):
        """
        Format the set of server data objects into a single string
        :return: String  The formatted data
        """
        msg = ""
        games = []
        for server in self.__servers:
            """
            Currently, order matters in the .json data files. Games will be displayed in the order they are stored,
            and if games of the same type are not next to one another, they will not be properly sorted.
            """
            # TODO: fix that
            if server.getGame() not in games:
                games.append(server.getGame())
                msg += "\n**__" + str(server.getGame().upper()) + " SERVERS__**\n\n"
            msg += str(server) + "\n\n"
        return msg

    def __readServerData(self):
        """
        Read in the .json file of server data
        :return:
        """
        with open(self.__serverDataFile) as serverData:
            data = json.load(serverData)
            for server in data["Server Data"]:
                # create an appropriate ServerInfo object for the data.
                # Default to ServerInfo class if game does not have it's own ServerInfo subclass
                serverInfoObject = ServerInfo  # default ServerInfo type
                for gameType in serverInfoTypes:
                    if server["Game"] == gameType.getGameName():
                        serverInfoObject = gameType
                        break
                self.__servers.append(serverInfoObject(server))