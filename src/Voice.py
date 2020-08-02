import random
import json

from InputOutput import InputOutput
from StringTuple import StringTuple

class Voice:
    """
    A voice is paired with a set of voice lines. Calling a voice will select a response from its list of lines
    """
    def __init__(self, voiceJson):
        self.__voiceJson = voiceJson
        self.__voiceNames = []
        self.__voiceLines = InputOutput(voiceJson)
        self.__parseVoiceFile()

    def getVoiceJson(self):
        """
        :return:  The path to the .json voice file
        """
        return self.__voiceJson

    def getVoiceNames(self):
        """
        :return:  list of names that can be used to call the voice
        """
        return self.__voiceNames

    def getResponse(self, command):
        """
        :param command:  the command the user is invoking
        :return: String  a voice line matching the command invoked
        """
        return self.__voiceLines.getResponse(command)

    def getVoiceLines(self):
        """
        :return:  The InputOutput object of all the voice's commands and lines
        """
        return self.__voiceLines

    def __parseVoiceFile(self):
        """
        parse the .json voice line file to extract the voice names
        """
        with open(self.__voiceJson) as voiceFile:
            data = json.load(voiceFile)
            for name in data["Character Names"]:
                self.__voiceNames.append(name)
