# store lists of recognized input and other lists birbBot checks but doesn't say (mostly)

import voiceLines
import ServerInfo

birbBotNames = [
    "birbbot",
    "birb bot",
    "birb_bot",
    "<@511403822418231296>"
    ]


rosters = {
    # random characters to prevent it from being used by other users
    "__default__": ""  # will store the default roster used in !join

}


voices = {
    "agathaarcher": voiceLines.AgathaArcher(),
    "agathamaa": voiceLines.AgathaManAtArms(),
    "agathavan": voiceLines.AgathaVanguard(),
    "agathavanguard": voiceLines.AgathaVanguard(),
    "agathaknight": voiceLines.AgathaKnight(),
    "masonarcher": voiceLines.MasonArcher(),
    "masonmaa": voiceLines.MasonManAtArms(),
    "masonvan": voiceLines.MasonVanguard(),
    "masonvanguard": voiceLines.MasonVanguard(),
    "masonknight": voiceLines.MasonKnight(),
    "unused": voiceLines.UnusedVoice(),
    "barbarian": voiceLines.Barbarian(),
    "commoner": voiceLines.Commoner(),
    "cruel": voiceLines.Cruel(),
    "eager": voiceLines.Eager(),
    "foppish": voiceLines.Foppish(),
    "knight": voiceLines.Knight(),
    "plain": voiceLines.Plain(),
    "raider": voiceLines.Raider(),
    "young": voiceLines.Young()
}


feintLines = [
    "feinted me",
    "i was feinted",
    "feints suck",
    "fuck feints",
    "feints are bullshit",
    "feints are fucking bullshit",
    "don't like feints",
    "hate feints",
    "feints are an exploit",
    "feint me"
    ]

# names birb bot is not allowed to say
forbiddenNames = [
    "hitler",
    "adolf",
    "adolf hitler",
    "adolfhitler",
    "stalin",
    "joseph stalin",
    "josephstalin",
    "pol pot",
    "polpot",
    "mao",
    "ben shapiro",
    "benshapiro",
    "donald trump",
    "trump",
    "donaldtrump",
    "realdonaldtrump",
    "jordan peterson",
    "jordanpeterston",
    "jordan_peterson"
]


specialResponseNames = {
    "birbbot": {"taunt": voiceLines.BirbBotSnark(),
                "respect": "Thank you, {0.author.mention} :hearts:",
                "thank": "You are very welcome, {0.author.mention} :hugging:"
                },
    "birb bot": {"taunt": voiceLines.BirbBotSnark(),
                 "respect": "Thank you, {0.author.mention} :hearts:",
                 "thank": "You are very welcome, {0.author.mention} :hugging:"
                 },
    "birb_bot": {"taunt": voiceLines.BirbBotSnark(),
                 "respect": "Thank you, {0.author.mention} :hearts:",
                 "thank": "You are very welcome, {0.author.mention} :hugging:"
                 },

    "birdbot":  {"taunt": "That's not my name, {0.author.mention}, but regardless, >:(",
                 "respect": "That's not my name, {0.author.mention}, but regardless, :hearts:",
                 "thank": "That's not my name, {0.author.mention}, but regardless, :hugging:"
                 },

    "bird bot":  {"taunt": "That's not my name, {0.author.mention}, but regardless, >:(",
                 "respect": "That's not my name, {0.author.mention}, but regardless, :hearts:",
                 "thank": "That's not my name, {0.author.mention}, but regardless, :hugging:"
                 },

    "bird_bot":  {"taunt": "That's not my name, {0.author.mention}, but regardless, >:(",
                 "respect": "That's not my name, {0.author.mention}, but regardless, :hearts:",
                 "thank": "That's not my name, {0.author.mention}, but regardless, :hugging:"
                 },

    "<@511403822418231296>": {"taunt": voiceLines.BirbBotSnark(),
                              "respect": "Thank you, {0.author.mention} :hearts:",
                              "thank": "You are very welcome, {0.author.mention} :hugging:"},
    "women": {"taunt": "You're trash, {0.author.mention}, learn some respect.",
              "respect": "https://www.youtube.com/watch?v=dfr4PrFxm0s",
              "thank": "https://www.youtube.com/watch?v=dfr4PrFxm0s"
              },
    "@everyone": {"taunt": "What if instead, everyone taunts you for thinking something this simple would work, {0.author.mention}?",
                  "respect": "We appreciate the sentiment, but this might not be the best way to show it, {0.author.mention}",
                  "thank": "You could better show your thankfulness by writing us each personal thank you letters, don't you think, {0.author.mention}?"
                  },
    "@here": {"taunt": "What if instead everyone taunts you for thinking something this simple would work, {0.author.mention}?",
              "respect": "We appreciate the sentiment, but this might not be the best way to show it, {0.author.mention}",
              "thank": "You could better show your thankfulness by writing us each personal thank you letters, don't you think, {0.author.mention}?"
              }
}


selfResponseDict = {
    "taunt": "Are you feeling okay, {0.author.mention}?",
    "thank": "Don't flatter yourself, {0.author.mention}",
    "respect": "I would, but the chat is too full of your ego for me to send a message right now, {0.author.mention}",
    "forbiddenName": "No"
}


voiceLineCommands = [
    "taunt",
    "xx3",
    "x8",
    "respect",
    "xx1",
    "x0",
    "thank",
    "x5",
    "xx6",
    "c4",
    "cc3",
    "ccc4"
]

allInfoCommands = [  # commands that will return all server info
    "ms"
]

checkForCommands = [  # commands that will activate the checkfor feature
    "checkfor",
]

messageCommands = {  # general one-response commands
    "goodnight": "Goodnight, {0.author.mention}",
    "scream": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "screm": ":screm:",
    "kiss": ":kissing_heart:",
    "arrest": ":police_car::police_car::police_car::police_car::police_car::police_car:",
    "f10": "I'm calling the police, {0.author.mention}",
    "c": "AAAARRRRRRRRRRRGGGGGGGGGGGGGGG",
    "quadfeint": "Sorry, this move is usable only by god himself",
    "sheildjump": "Reported for hacks",
    "flourish": "*twirls*",
    "comeatme": "GIVE ME A HUG!",
    "hug": ":hugging:"
    # "help": "Documentation has been sent to you. If you did not receive it, please make your DM's public"
}

dmCommands = {  # commands that will result in a DM response
    "help": "__**BIRB BOT COMMAND DOCUMENTATION**__\n"
            "<> : signifies optional parameter\n"
            "[]: signifies required parameter\n"
            "__*Do not include brackets when entering command*__\n\n"

            "```Command                    | Result\n"
            "--------------------------------------------------------\n"
            "!hello                     | Say hello\n"
            "!ms                        | Return info from all Moorland Skirmishers servers\n"

            "!taunt <class> <name>      | Say a taunt line\n"
            "!respect <class> <name>    | Say a respect line\n"
            "!thank <class> <name>      | Say a thanks line\n"
            "!x<number 0 - 9>           | Say a chivalry voice line\n"
            "!z<number 0 - 9>           | Say a chivalry tactical line\n"
            "```"

            "\n__**Class Names**__\n"
            "agathaMAA\n"
            "agathaArcher\n"
            "agathaVan\n"
            "agathaKnight\n"
            "masonMAA\n"
            "masonArcher\n"
            "masonVan\n"
            "masonKnight\n"
            "barbarian\n"
            "commoner\n"
            "cruel\n"
            "eager\n"
            "foppish\n"
            "knight\n"
            "plain\n"
            "raider\n"
            "young\n"

            "\n__**Notes**__\n"
            "Capitalization does not matter\n"
            "The x and z voice commands can be \"flipped\" like in chiv. x9 == xx2\n"
            "BirbBot has a large number of commands not listed in documentation, some of which are not triggered with \"![command]\". They will likely reveal themselves in time\n"
            "Report any bugs found to Raysparks\n"

            "\n__**Examples**__\n"
            "!ms   --->   \"Mooland Skirmishers: Gracious Welcome is playing aocffa-moor_p with a population... \"\n"
            "!taunt  --->   \"Your wife is a hobby horse!\"\n"
            "!thank Malric   --->   \"Malric, thank you brother!\"\n"
            "!respect agathaVan Baron Von Moorland    --->   \"Baron Von Moorland, I dare say you matched even my own skills\"\n"
            "xx2   --->   \"HA HA HA!\"\n\n"
            "Final Note: Roster and checkfor commands and have been depreciated at this time and will not function. Let Raysparks know if you want to see their return",

    # "rosterhelp": "__**THESE COMMANDS HAVE BEEN DEPRECIATED DUE TO GENERAL BUGGINESS AND LACK OF USE**__\n\n"
    #               "__**BIRB BOT ROSTER COMMAND DOCUMENTATION**__\n"
    #               "<> : signifies optional parameter\n"
    #               "[]: signifies required parameter\n"
    #               "__*Do not include brackets when entering command*__\n\n"
    #
    #               "**__BASIC COMMANDS__**\n"
    #               "```Command                          | Result\n"
    #               "--------------------------------------------------------\n"
    #               "!<rosterName> join               | Join the most recent roster. Specify name to join a specific roster\n"
    #               "!<rosterName> leave              | Leave the most recent roster. Specify name to join a specific roster```\n\n"
    #
    #               "**__CREATOR COMMANDS__**\n"
    #               "```Command                       | Result\n"
    #               "--------------------------------------------------------\n"
    #               "!newRoster [size] [name]         | Create a new roster of the specified size with the specified name\n"
    #               "![rosterName] show               | Display the specified roster\n"
    #               "![rosterName] alert              | Alert all members of the specified roster\n"
    #               "CREATOR-ONLY COMMANDS            | These commands cannot be used by anyone but the person who created the roster\n"
    #               "![rosterName] setSlots [size]    | Change the roster size to the newly specified size\n"
    #               "![rosterName] register [@][name] | Register a new member that is not yourself. An [@] must be provided for \"!alert\" to alert them\n"
    #               "![rosterName] remove [@]||[name] | Remove a member that is not yourself. Name or [@] is accepted\n"
    #               "![rosterName] delete             | Permanently delete the specified roster\n\n```"
    #
    #               "\n**Examples:**\n"
    #               "!newRoster 5 exampleRoster   --->   creates a new roster named \"exampleRoster\" of size 5\n"
    #               "!newRoster join   --->   join newRoster\n"
    #               "!exampleRoster register Birb @birb#1234   --->   registers a new member named Birb with an @ of @birb#1234\n"
    #               "!exampleRoster register Birb   --->   registers a new member named Birb that will not be alerted\n"
    #               "!exampleRoster remove Birb   --->   removes Birb from the roster. Also works provided the @\n"
    #               "!exampleRoster setSlots 10   --->   changes the roster size to 10 with 5 waiting list slots"
}

hiddenCommandDict = {  # commands that do not begin with "!"
    "come hither": "come hither",
    "good bot": "*happy birb noises*",
    "best bot": "*happy birb noises*",
    "fantastic bot": "*happy birb noises*",
    "amazing bot": "*happy birb noises*",
    "great bot": "*happy birb noises*",
    "what is malric": "a dude!",
    "goodnight birbbot": "goodnight, {0.author.mention}",
    "goodnight birb bot": "goodnight, {0.author.mention}",
    "goodnight birb_bot": "goodnight, {0.author.mention}",
    "goodnight <@511403822418231296>" : "goodnight, {0.author.mention}",
    "goodnight, birbbot": "goodnight, {0.author.mention}",
    "goodnight, birb bot": "goodnight, {0.author.mention}",
    "goodnight, birb_bot": "goodnight, {0.author.mention}",
    "goodnight, <@511403822418231296>" : "goodnight, {0.author.mention}",
    "i love you birbbot": "I love you too, {0.author.mention}",
    "i love you birb bot": "I love you too, {0.author.mention}",
    "i love you birb_bot": "I love you too, {0.author.mention}",
    "i love you <@511403822418231296>": "I love you too, {0.author.mention}",
    "i love you, birbbot": "I love you too, {0.author.mention}",
    "i love you, birb bot": "I love you too, {0.author.mention}",
    "i love you, birb_bot": "I love you too, {0.author.mention}",
    "i love you, <@511403822418231296>": "I love you too, {0.author.mention}",
    "we'regonnaneedthatgrain": "Protect the farm!",
    "weregonnaneedthatgrain": "Protect the farm!",
    "we're gonna need that grain": "Protect the farm!",
    "were gonna need that grain": "Protect the farm!",
    "x1": voiceLines.Yes(),
    "xx0": voiceLines.Yes(),
    "x2": voiceLines.No(),
    "xx9": voiceLines.No(),
    "x3": voiceLines.Help(),
    "xx8": voiceLines.Help(),
    "x4": voiceLines.WithYou(),
    "xx7": voiceLines.WithYou(),
    "x5": voiceLines.Voice(),
    "xx6": voiceLines.Voice(),
    "x6": voiceLines.Welcome(),
    "xx5": voiceLines.Welcome(),
    "x7": voiceLines.Sorry(),
    "xx4": voiceLines.Sorry(),
    "x8": voiceLines.Voice(),
    "xx3": voiceLines.Voice(),
    "x9": voiceLines.Laugh(),
    "xx2": voiceLines.Laugh(),
    "x0": voiceLines.Voice(),
    "xx1": voiceLines.Voice(),
    "z1": voiceLines.Follow(),
    "zz0": voiceLines.Follow(),
    "z2": voiceLines.Forward(),
    "zz9": voiceLines.Forward(),
    "z3": voiceLines.Retreat(),
    "zz8": voiceLines.Retreat(),
    "z4": voiceLines.Archers(),
    "zz7": voiceLines.Archers(),
    "z5": voiceLines.Objective(),
    "zz6": voiceLines.Objective(),
    "z6": voiceLines.Hold(),
    "zz5": voiceLines.Hold(),
    "z7": voiceLines.DefendMe(),
    "zz4": voiceLines.DefendMe(),
    "z8": voiceLines.Incoming(),
    "zz3": voiceLines.Incoming(),
    "z9": voiceLines.BehindUs(),
    "zz2": voiceLines.BehindUs(),
    "z0": voiceLines.NoOneHere(),
    "zz1": voiceLines.NoOneHere(),
    "c1": voiceLines.Yes(),
    "c2": voiceLines.No(),
    "c3": voiceLines.Help(),
    "c4": voiceLines.Voice(),
    "c5": voiceLines.Intimidate(),
    "cc1": voiceLines.Sorry(),
    "cc2": voiceLines.Laugh(),
    "cc3": voiceLines.Voice(),
    "cc4": voiceLines.Friendlies(),
    "cc5": voiceLines.Retreat(),
    "ccc1": voiceLines.Hold(),
    "ccc2": voiceLines.Hello(),
    "ccc3": voiceLines.Follow(),
    "ccc4": voiceLines.Voice(),
    "ccc5": voiceLines.Charge()
}

multiResponseCommands = {  # commands that have more than one possible response
    "hello": voiceLines.Hello(),
    "x1": voiceLines.Yes(),
    "xx0": voiceLines.Yes(),
    "x2": voiceLines.No(),
    "xx9": voiceLines.No(),
    "x3": voiceLines.Help(),
    "xx8": voiceLines.Help(),
    "x4": voiceLines.WithYou(),
    "xx7": voiceLines.WithYou(),
    "x5": "",
    "xx6": "",
    # x5 and xx6 handled in voiceLines
    "x6": voiceLines.Welcome(),
    "xx5": voiceLines.Welcome(),
    "x7": voiceLines.Sorry(),
    "xx4": voiceLines.Sorry(),
    # x8 and xx3 handled in voiceLines
    "x9": voiceLines.Laugh(),
    "xx2": voiceLines.Laugh(),
    # x0 and xx1 handled in voiceLines
    "z1": voiceLines.Follow(),
    "zz0": voiceLines.Follow(),
    "z2": voiceLines.Forward(),
    "zz9": voiceLines.Forward(),
    "z3": voiceLines.Retreat(),
    "zz8": voiceLines.Retreat(),
    "z4": voiceLines.Archers(),
    "zz7": voiceLines.Archers(),
    "z5": voiceLines.Objective(),
    "zz6": voiceLines.Objective(),
    "z6": voiceLines.Hold(),
    "zz5": voiceLines.Hold(),
    "z7": voiceLines.DefendMe(),
    "zz4": voiceLines.DefendMe(),
    "z8": voiceLines.Incoming(),
    "zz3": voiceLines.Incoming(),
    "z9": voiceLines.BehindUs(),
    "zz2": voiceLines.BehindUs(),
    "z0": voiceLines.NoOneHere(),
    "zz1": voiceLines.NoOneHere(),
    "c1": voiceLines.Yes(),
    "c2": voiceLines.No(),
    "c3": voiceLines.Help(),
    # c4 handled in voiceLines
    "c5": voiceLines.Intimidate(),
    "cc1": voiceLines.Sorry(),
    "cc2": voiceLines.Laugh(),
    # cc3 handled in voiceLines
    "cc4": voiceLines.Friendlies(),
    "cc5": voiceLines.Retreat(),
    "ccc1": voiceLines.Hold(),
    "ccc2": voiceLines.Hello(),
    "ccc3": voiceLines.Follow(),
    # ccc4 handled in voiceLines
    "ccc5": voiceLines.Charge()
}

recognizedChannels = {
    "rules-of-engagement": "454804299596169236",
    "announcements": "517530205750034433",
    "gracious-welcome": "351239360475168768",
    "mordhau": "494183423502581761",
    "events": "494183498769367040",
    "agatha": "312000965765234691",
    "mason": "312000920722341894",
    "server-status": "517530437300518912",
    "moorland-castle": "524294151211319316",
    "common-ground": "269236791196909569",
    "other-games": "551991231333531670",
    "music": "458070110889050123",
    "memes": "494183581497819136",
    "smut-stuff-nsfw": "461067966285611008",

    "documentation": "512750458184531984",
    "public-bot-testing": "512786062150729728",
    "private-bot-testing": "511405757783212069",
    "private-birbbot-usage": "550481595421687810"
}