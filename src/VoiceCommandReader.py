import random
import json
import re
from StringTuple import StringTuple
from Voice import Voice

class VoiceCommandReader:
    """
    Class to handle the parsing of all voice commands
    """
    def __init__(self, voicePaths, specialResponsePaths, commandPaths):
        self.__message = None
        self.__author = None
        self.__authorID = None
        self.__command = None

        self.__voice = ""
        self.__target = ""

        self.__voices = []
        self.__loadVoiceLines(voicePaths)

        self.__specialResponses = self.__loadSpecialResponses(specialResponsePaths)

        self.__commandPaths = commandPaths

    def getVoices(self):
        return self.__voices

    def parseCommand(self, message, command):
        self.__message = message
        self.__author = message.author
        self.__authorID = message.author.id
        self.__command = self.__generalizeCommand(command, self.__commandPaths)
        msg = ""
        self.__extractVoiceAndTarget()

        if self.__isSpecialResponseName(self.__target):
            msg = self.__getSpecialResponse(self.__target, self.__command)

        else:
            if self.__target != "":  # append target
                msg = self.__target + ", "
            # append voice line
            if isinstance(self.__voice, Voice):
                line = (self.__voice.getResponse(self.__command) if msg != "" else
                        self.__voice.getResponse(self.__command).capitalize())
                msg += line
            else:
                responseVoice = random.choice(self.__voices)
                line = (responseVoice.getResponse(self.__command) if msg != "" else
                        responseVoice.getResponse(self.__command).capitalize())
                msg += line

        # reset the target and voice
        self.__target = ""
        self.__voice = ""

        return msg

    def __loadVoiceLines(self, voicePaths):
        """
        read the configs of voice lines
        :param voicePaths:
        :return:
        """
        voices = []
        for voicePath in voicePaths.values():
            voices.append(Voice(voicePath))
        self.__voices = voices

    def __loadSpecialResponses(self, specialResponseJson):
        """
        read the .json file that specifies special response names and the lines to respond to those names with
        :param specialResponseJson:  the .json file with special response data
        :return:  a dictionary with names as keys and responses as values
        """
        specialResponseDict = {}
        with open(specialResponseJson) as responseJson:
            data = json.load(responseJson)
            for name in data["Special Names"].keys():
                specialResponseDict[StringTuple(name).getTuple()] = data["Special Names"][name]
        return specialResponseDict

    def __generalizeCommand(self, command, commandPath):
        """
        Map the command given to it's generalized name as specified in the VoiceCommands.json file
        :return: String of the global command name
        """
        with open(commandPath) as generalizedCommandJson:
            data = json.load(generalizedCommandJson)
            for cmd in data["public"]:
                if command in data["public"][cmd]:
                    return cmd

            for cmd in data["hidden"]:
                if command in data["hidden"][cmd]:
                    return cmd

        return command

    def __extractVoiceAndTarget(self):
        """
        Parse the voice command to extract the target name and desired voice
        """
        if len(self.__message.content.lower().split()) > 1:  # if more than the base command is provided
            for voice in self.__voices:  # get the voice
                if self.__message.content.lower().split()[1] in voice.getVoiceNames():
                    self.__voice = voice
                    break

            self.__target = (self.__message.content.split()[1:] if self.__voice == "" else
                             self.__message.content.split()[2:])
            self.__target = " ".join(self.__target).strip()  # change target from list of strings into single string

            # check if command is targeting the person who sent the command
            # when a user is @ mentioned, BirbBot reads it in the form: <@!333333333333333333>
            # Grab the numbers in the middle
            possibleID = re.search("(\d{17})\d*", self.__target)
            if possibleID == None:
                possibleID = ""
            else:
                possibleID = possibleID.group()

            if possibleID == str(self.__authorID):
                self.__target = "<<self>>"


    def __isSpecialResponseName(self, name):
        """
        Check if a provided name is a special response name
        :param name:  the name to check
        :return:  boolean
        """
        possibleID = re.search("(\d{17})\d*", name.lower())
        if possibleID == None:
            possibleID = "//////////"
        else:
            possibleID = possibleID.group()

        for names in self.__specialResponses.keys():
            if name.lower() in names or possibleID in names:  # check for user ids
                return True
        return False

    def __getSpecialResponse(self, name, command):
        """
        Get the appropriate special response line for the provided name
        :param name:     the name to fetch the line for
        :param command:  the command the name was intended for
        :return:         the special response line
        """
        possibleID = re.search("(\d{17})\d*", name.lower())
        if possibleID == None:
            possibleID = "//////////"
        else:
            possibleID = possibleID.group()

        for names in self.__specialResponses.keys():
            if name.lower() in names or possibleID in names:
                return random.choice(self.__specialResponses[names][command])
