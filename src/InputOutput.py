import random
import json

from StringTuple import StringTuple

class InputOutput:
    """
    Contains input-output pairs for a discord bot
    Inputs are all tuple objects, even if there is only one input
    """
    def __init__(self, ioJson):
        self.__ioJson = ioJson
        self.__inputOutput = {}
        self.__parseIOFile()

    def getIOJson(self):
        """
        :return:  The path to the .json voice file
        """
        return self.__ioJson

    def getInputOutput(self):
        """
        :return:  The dictionary of all voice lines and line types
        """
        return self.__inputOutput

    def getCommands(self):
        """
        :return:  A list of all the commands listed in the io file
        """
        return list(self.__inputOutput.keys())

    def isValidInput(self, command):
        """
        Check if a provided command is one of the InputOutput's input values
        :param command:  the command to check
        :return:         Boolean
        """
        for commandTuple in self.__inputOutput.keys():
            if command in commandTuple:
                return True
        return False

    def getResponse(self, command):
        """
        :return: String  A response for the given command
        """
        for commands in self.__inputOutput:
            if command in commands:
                return random.choice(self.__inputOutput[commands])

    def __parseIOFile(self):
        """
        parse the .json voice line file
        """
        with open(self.__ioJson) as voiceFile:
            data = json.load(voiceFile)
            # parse voice lines
            for commands in data["InputOutput"].keys():
                commandsTuple = StringTuple(commands)
                # if commands in self.__inputOutput:
                #     raise KeyError("The command " + str(commands) + " is already defined in " + str(self.__ioJson))
                # else:
                self.__inputOutput[commandsTuple.getTuple()] = data["InputOutput"][commands]
