# BirbBot
# Discord bot for the Moorland Skirmishers: Gracious Welcome server
# Work with Python 3.5

import discord
import logging

import json

from InputOutput import InputOutput
from VoiceCommandReader import VoiceCommandReader
from ServerInfoCommandReader import ServerInfoCommandReader

logging.basicConfig(level=logging.INFO)

class BirbBot(discord.Client):
    def __init__(self, configFilePath):
        super().__init__()
        with open(configFilePath) as configFile:
            data = json.load(configFile)
            # TODO: make this a relative path
            tokenText = open("C:\\users\\raysp\\Desktop\\Python\\Personal\\BirbBot2\\resources\\botToken.txt")
            self.__token = tokenText.readline()
            self.__commandSymbol = data["Command Symbol"]
            self.__adminPassword = data["Admin Password"]
            self.__botDescription = data["Bot Description"]

            self.__dmCommands = InputOutput(data["IO Paths"]["DM Commands"])
            self.__publicCommands = InputOutput(data["IO Paths"]["Public Commands"])
            self.__hiddenCommands = InputOutput(data["IO Paths"]["Hidden Commands"])

            self.__serverCommands = ServerInfoCommandReader(data["IO Paths"]["Server Constructors"],
                                                            data["IO Paths"]["Server Data"])
            self.__voiceCommands = VoiceCommandReader(data["Voice Line Paths"],
                                                      data["IO Paths"]["Special Responses"],
                                                      data["IO Paths"]["Voice Commands"])


    def getToken(self):
        return self.__token

    def getCommandSymbol(self):
        return self.__commandSymbol

    def getDmCommands(self):
        return self.__dmCommands

    def getPublicCommands(self):
        return self.__publicCommands

    def getHiddenCommands(self):
        return self.__hiddenCommands

    def getServerCommands(self):
        return self.__serverCommands

    def getVoiceCommands(self):
        return self.__voiceCommands


    # def getSpecialNames(self):
    #     return self.__specialNames
    #
    # def getVoices(self):
    #     return self.__voices

    def parseVoiceCommand(self, message, command):
        return self.__voiceCommands.parseCommand(message, command)

    def isVoiceCommand(self, cmd):
        for voice in self.__voiceCommands.getVoices():
            if voice.getVoiceLines().isValidInput(cmd):
                return True
        return False

    def isServerCommand(self, cmd):
        for command in self.__serverCommands.getCommands():
            if cmd == command:
                return True
        return False


    def __loadIO(self, ioPath):
        IoDict = {}
        with open(ioPath) as IoFile:
            data = json.load(IoFile)
            IoDict = data["InputOutput"]
        return IoDict

birbBotConfig = "C:\\Users\\raysp\\Desktop\\Python\\Personal\\BirbBot2\\resources\\BirbBotConfig.json"
birbBot = BirbBot(birbBotConfig)

@birbBot.event
async def on_message(message):
    global birbBot
    if message.author == birbBot.user:  # prevent the bot from replying to itself
        return

    authorName = str(message.author.display_name)
    authorID = "<@" + str(message.author.id) + ">"
    msg = ""

    if message.content.startswith(birbBot.getCommandSymbol()):
        cmd = message.content.lower().split()[0][len(birbBot.getCommandSymbol()):]  # get the first word and remove command symbol

        # commands retrieved from birbBot.[[IO_Object]].getCommands() are formatted as a list of tuples

        if any(cmd in i for i in birbBot.getDmCommands().getCommands()):
            msg = birbBot.getDmCommands().getResponse(cmd)
            try:
                await message.author.send(msg.format(message))
            except KeyError:  # if message contains text between {braces} that causes errors with .format()
                await message.author.send(msg)

        elif any(cmd in i for i in birbBot.getPublicCommands().getCommands()):
            msg = birbBot.getPublicCommands().getResponse(cmd)
            try:
                await message.channel.send(msg.format(message))
            except KeyError:  # if message contains text between {braces} that causes errors with .format()
                await message.channel.send(msg)

        elif birbBot.isVoiceCommand(cmd):
            msg = birbBot.parseVoiceCommand(message, cmd)
            try:
                await message.channel.send(msg.format(message))
            except KeyError:  # if message contains text between {braces} that causes errors with .format()
                await message.channel.send(msg)

        elif birbBot.isServerCommand(cmd):
            msg = birbBot.getServerCommands().getAllInfo(cmd)
            try:
                await message.channel.send(msg.format(message))
            except KeyError:  # if message contains text between {braces} that causes errors with .format()
                await message.channel.send(msg)

    if message.content in birbBot.getHiddenCommands().getCommands():
        msg = birbBot.getHiddenCommands().getResponse(message.content)
        try:
            await message.channel.send(msg.format(message))
        except KeyError:  # if message contains text between {braces} that causes errors with .format()
            await message.channel.send(msg)

    elif birbBot.isVoiceCommand(message.content):
        cmd = message.content.lower().split()[0]
        msg = birbBot.parseVoiceCommand(message, cmd)
        try:
            await message.channel.send(msg.format(message))
        except KeyError:  # if message contains text between {braces} that causes errors with .format()
            await message.channel.send(msg)

    # if message.content == "!reload":
    #     birbBot = BirbBot("C:\\Users\\raysp\\Desktop\\Python\\Personal\\BirbBot\\resources\\BirbBotConfig.json")


@birbBot.event
async def on_ready():
    print('Logged in as')
    print(birbBot.user.name)
    print(birbBot.user.id)
    print('------')

birbBot.run(birbBot.getToken())