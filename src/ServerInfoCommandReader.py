from ServerInfo import *

import json

class ServerInfoCommandReader:
    def __init__(self, serverConstructorFile, serverDataFile):
        self.__serverConstructorFile = serverConstructorFile
        self.__serverDataFile = serverDataFile
        self.__servers = []
        self.__commands = []
        self.__gatherCommands()

    def getAllInfo(self, cmd):
        """
        Retrieve the information from a set of servers
        :param:   the command invoked
        :return:  String  The formatted information from all servers
        """
        self.__readServerData(cmd)
        return self.__formatServerDataSet()

    def getCommands(self):
        """
        :return:  String List  The list of recognized server info commands
        """
        return self.__commands

    def __gatherCommands(self):
        """
        Gather all the server info commands from the constructor file
        """
        self.__commands.clear()
        with open(self.__serverConstructorFile) as serverConstructors:
            data = json.load(serverConstructors)
            for key, value in data.items():
                self.__commands.append(key)

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

    def __readServerData(self, cmd):
        """
        Read in the .json file of server dat
        :param:  The server group to read the data of
        """
        self.__servers.clear()
        with open(self.__serverDataFile) as serverData:
            data = json.load(serverData)
            for serverGroup, servers in data.items():
                if cmd == serverGroup:
                    for server in servers:
                        # create an appropriate ServerInfo object for the data.
                        # Default to ServerInfo class if game does not have it's own ServerInfo subclass
                        serverInfoObject = ServerInfo  # default ServerInfo type
                        for gameType in serverInfoTypes:
                            if server["Game"] == gameType.getGameName():
                                serverInfoObject = gameType
                                break
                        self.__servers.append(serverInfoObject(server))
