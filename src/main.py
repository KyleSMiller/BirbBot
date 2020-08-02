# BirbBot
# Discord bot for the Moorland Skirmishers: Gracious Welcome server
# Work with Python 3.5

import discord
import recognizedInput
from VoiceCommandReader import VoiceCommandReader
from ServerInfoCommandReader import ServerInfoCommandReader
from voiceLines import SimpleVoice, Voice

from resources.passwords import adminPassword

botTokentxt = open("botToken.txt")
TOKEN = botTokentxt.readline().strip()

client = discord.Client()


COMMAND_SYMBOL = "!"  # character that signifies the start of a BirbBot command


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    msgAuthor = str(message.author.display_name)
    msgAuthorID = "<@" + message.author.id + ">"

    # direct message commands
    if str(message.channel.type) == "private":
        if message.content.startswith("!shutdown " + str(adminPassword)):
            await client.send_message(message.author, "shutting down")
            print("BirbBot shut down by remote command")
            exit(9473)
        if message.content.startswith("!say") and message.author.id == "296335824427941888":
            targetChannelName = message.content.split(" ")[1]
            if targetChannelName in recognizedInput.recognizedChannels:
                try:
                    targetChannel = recognizedInput.recognizedChannels[targetChannelName]
                    msgList = message.content.split(" ")[2:]
                    msg = " ".join(msgList)
                    whisperChannel = client.get_channel(targetChannel)
                    await client.send_message(whisperChannel, msg)
                except:
                    await client.send_message(message.author, "Something went wrong. "
                                                              "I probably don't have access to that channel")
            else:
                await client.send_message(message.author, "I don't recognize that channel")


    if message.content.startswith(COMMAND_SYMBOL):
        cmd = message.content.lower().split()[0][len(COMMAND_SYMBOL):]  # get the first word and remove COMMAND_SYMBOL
        msg = ""

        if cmd in recognizedInput.voiceLineCommands:
            voiceCommandReader = VoiceCommandReader(message, msgAuthor, msgAuthorID, cmd)
            msg = voiceCommandReader.retrieveVoiceCommand(recognizedInput.voices)

        # elif cmd in recognizedInput.recognizedServers:
        #     msg = ServerInfoCommandReader.retrieveServerInfo(cmd)

        elif cmd in recognizedInput.allInfoCommands:
            await client.add_reaction(message, "⌛")
            serverCommandReader = ServerInfoCommandReader("C:\\Users\\raysp\\Desktop\\Python\\Personal\\SteamServerQuerier\\src\\ServerQueryData.json")
            msg = serverCommandReader.getAllInfo()
            await client.remove_reaction(message, "⌛", client.user)

        # elif cmd in recognizedInput.checkForCommands:
        #     msg = ServerInfoCommandReader.checkFor(message)

        elif cmd in recognizedInput.messageCommands:
            msg = recognizedInput.messageCommands[cmd]

        elif cmd in recognizedInput.multiResponseCommands:
            msg = recognizedInput.multiResponseCommands[cmd].getResponse()

        elif cmd in recognizedInput.dmCommands:
            await client.send_message(message.author, recognizedInput.dmCommands[cmd])


        if msg != "":
            try:
                await client.send_message(message.channel, msg.format(message))
            except KeyError:  # if message contains text between {braces} that causes errors with .format()
                await client.send_message(message.channel, msg)


    # hidden commands
    elif message.content.lower() in recognizedInput.hiddenCommandDict:
        msg = recognizedInput.hiddenCommandDict[message.content.lower()]
        if isinstance(msg, SimpleVoice):
            msg = msg.getResponse()
        if isinstance(msg, Voice):
            voiceCommandReader = VoiceCommandReader(message, msgAuthor, msgAuthorID, message.content)
            msg = voiceCommandReader.retrieveVoiceCommand(recognizedInput.voices)
        try:
            await client.send_message(message.channel, msg.format(message))
        except KeyError:  # if message contains text between {braces} that causes errors with .format()
            await client.send_message(message.channel, msg)

    # feint complaint commands
    elif "feint" in message.content or "feinted" in message.content or "feints" in message.content:
        for i in recognizedInput.feintLines:
            if message.content.find(i) != -1:
                msg = ("Oh no! Have you been feinted in Torn Banner's 2012 action slasher game, "
                       "\"Chivalry: Medieval Warfare\"? Don't worry, you aren't alone, and help *is* out there. "
                       "Please, take the time to talk to someone. http://tornbanner.com/contact/")
                try:
                    await client.send_message(message.channel, msg.format(message))
                except KeyError:  # if message contains text between {braces} that causes errors with .format()
                    await client.send_message(message.channel, msg)








@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)