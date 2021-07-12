import json

class GamerTracker():
    """
    Keep track of people who have used the "gaming" command
    """
    def __init__(self, gamerJson):
        self.__gamerJson = gamerJson
        with open(self.__gamerJson) as jsonFile:
            self.__gamers = json.load(jsonFile)

    def getGamers(self):
        return self.__gamers

    def addGamer(self, newGamer):
        """
        Update the gamers dict with the new offender
        :param newGamer:  the id of the user who gamed
        """
        isRepeatOffender = False
        for gamer in self.__gamers.keys():
            if str(newGamer) == gamer:
                self.__gamers[str(newGamer)] += 1
                isRepeatOffender = True
        if not isRepeatOffender:
            self.__gamers[str(newGamer)] = 1

        self.__saveGamers()

    def punish(self):
        """
        Punish Gamers
        """
        gamerAts = []
        for gamer in self.__gamers.keys():
            gamerAts.append("<@" + gamer + ">\n")
        return gamerAts


    def __saveGamers(self):
        """
        Save the dict of gamers to a .json file
        This method name does not imply gamers ought to be saved.
        :param outputFile:  the path of the gamers .json file
        """
        with open(self.__gamerJson, "w") as outfile:
            json.dump(self.__gamers, outfile)
            outfile.close()