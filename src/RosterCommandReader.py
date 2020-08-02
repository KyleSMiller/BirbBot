def openRoster():
    # create roster from saved rosters
    savedRosters = open("savedRosters.txt")

    playerData = []
    name = ""
    size = 0
    admin = "Raysparks#1042"

    rosterCount = 0
    rosterList = []

    # count the number of rosters in the file
    for line in savedRosters:
        if line == "":  # ignore empty file
            return
        elif line.startswith("__end__"):
            rosterList.append([])

    savedRosters.close()
    savedRosters = open("savedRosters.txt")

    currentRoster = 0

    # store read data in a multidimensional list
    for line in savedRosters:
        if line[:5] == "name=":
            name = line.split("=")[1].strip()
            rosterList[currentRoster].append(name)
        elif line[:5] == "size=":
            size = int(line.split("=")[1])
            rosterList[currentRoster].append(size)
        elif line[:6] == "admin=":
            admin = line.split("=")[1].strip()
            rosterList[currentRoster].append(admin)
        elif line[:3] == (":-:"):
            playerName = line.split(",")[0][3:]
            playerID = line.split(",")[1].strip()
            playerData = [[playerName, playerID]]
            rosterList[currentRoster].append(playerData)
        elif line[:7] == "__end__":
            currentRoster += 1

    savedRosters.close()

    # create roster objects from read data
    for newRoster in rosterList:
        recognizedInput.rosters[newRoster[0].lower()] = roster.Roster(newRoster[0], newRoster[1], newRoster[2])
        for player in newRoster[3]:
            recognizedInput.rosters[newRoster[0].lower()].registerPlayer(player[0], player[1])


def saveRosters():
    # save all relevant roster data to .txt file
    rosterSaveFile = open("savedRosters.txt", "w")

    for rosterToSave in recognizedInput.rosters.values():
        try:
            if type(rosterToSave) == str or type(rosterToSave) == None:  # ignore __default__ roster
                continue
            name = rosterToSave.getName()
            size = int(rosterToSave.getSlots())
            admin = rosterToSave.getAdmin()
            playerName = rosterToSave.getPlaySlots()
            playerID = rosterToSave.getIDs()

            rosterSaveFile.write("name=" + str(name) + "\n")
            rosterSaveFile.write("size=" + str(size) + "\n")
            rosterSaveFile.write("admin=" + str(admin) + "\n")
            for i in range(len(playerName)):
                rosterSaveFile.write(":-:" + str(playerName[i]) + "," + str(playerID[i]) + "\n")
            rosterSaveFile.write("__end__\n")
        except:  # ignore empty files
            pass

    rosterSaveFile.close()


def createRoster(message, author):
    rosterSize = int(message.content.lower().split()[1])
    newRosterName = message.content.split()[2]

    # construct a new roster
    if newRosterName not in recognizedInput.rosters:
        recognizedInput.rosters[newRosterName.lower()] = roster.Roster(newRosterName, rosterSize, author)

        # track the most recently created roster as the default
        msg = recognizedInput.rosters[newRosterName.lower()].displayPlayers()
        recognizedInput.rosters["__default__"] = newRosterName.lower()

        # check that the roster is valid
        if recognizedInput.rosters[newRosterName.lower()].validRoster == "Name error":
            del recognizedInput.rosters[newRosterName.lower()]
            msg = "You cannot use a name that is already reserved for another command!"
        elif recognizedInput.rosters[newRosterName.lower()].validRoster == "Size error":
            msg = ("Roster must be between size 2 and 20 -- **creating your roster with default size 10.**"
                   " Use setSlot if you want to change size after initial roster creation.\n"
                   "ex: !exampleRoster setSlots 5")
        elif recognizedInput.rosters[newRosterName.lower()].validRoster == ">:(":
            del recognizedInput.rosters[newRosterName.lower()]
            msg = "You aren't as clever as you think, {0.author.mention}"

    else:
        msg = ("roster \"" + str(newRosterName) + "\" already exists! Please try again with a different "
                                                  "name, or use \"!" + str(
            newRosterName) + " delete\" to delete an unwanted roster")
    return msg


def processRosterCommand(message, author, authorID, roster):
    rosterName = message.content.split()[0]
    cmd = message.content.lower().split()[1]  # change command to 2nd word typed, as 1st is the roster name
    msg = ""
    reaction = ""

    if cmd == "setslots":
        if roster.isAdmin(str(author)):
            try:
                setSlot = roster.setSlots(int(message.content.lower().split()[2]))
                if setSlot:
                    reaction = "R"
                else:
                    reaction = "X"
                    msg = "Roster size must be at least 2 and at most 20"
            except:
                msg = "invalid slot count. Must be a positive integer between 2 and 20"
        else:
            msg = ("You must be the roster's creator to use this command!")

    elif cmd == "show" or cmd == "display":
        msg = roster.displayPlayers()

    elif cmd == "alert":
        if roster.isAdmin(str(author)):
            msg = roster.alertPlayers()
        else:
            msg = "You must be the roster's creator to use this command! If you wanted to view the roster, use !" + \
                  str(rosterName) + " show"

    elif cmd == "join":
        reaction = roster.attemptRegistery(player=author.display_name, playerID=authorID)

    elif cmd == "register":
        if roster.isAdmin(str(author)):
            # check the order of the name, ID arguments so it accepts them both ways
            if message.content.split()[2].startswith("<@"):
                playerID = message.content.split()[2]
                try:
                    playerName = message.content.split()[3]
                    reaction = roster.attemptRegistery(player=playerName, playerID=playerID)
                    if reaction == ">:(":
                        msg = "You aren't as clever as you think, {0.author.mention}"
                except:
                    msg = ("You must provide a plaintext name for the player, or else they will be alerted every time the "
                           "roster is viewed! ex: !" + rosterName + " register @Alan#1234 Alan")
            else:
                try:
                    if message.content.split()[3].startswith("<@"):
                        playerName = message.content.split()[2]
                        playerID = message.content.split()[3]
                        reaction = roster.attemptRegistery(player=playerName, playerID=playerID)
                        if reaction == ">:(":
                            msg = "You aren't as clever as you think, {0.author.mention}"
                    else:
                        msg = ("You must provide a vaild @ with the name. ex: !" + rosterName + " register @Alan#1234 Alan")
                except:
                    # runs if no ID is given, in which case the Name will be used as the ID
                    playerName = message.content.split()[2]
                    reaction = roster.attemptRegistery(player=playerName, playerID="")
                    if reaction == ">:(":
                        msg = "I'm going to assume that was a mistake, {0.author.mention} >:("
        else:
            msg = ("You must be the roster's creator to use this command! If you wish to register yourself, use !"
                   + rosterName + " join")

    elif cmd == "remove":
        if roster.isAdmin(str(author)):
            playerName = message.content.split()[2]
            left = roster.removePlayer(playerName)
            if left:
                reaction = "R"
            else:
                reaction = "X"
        else:
            msg = ("You must be the roster's creator to use this command! If you wish to register yourself, use !"
             + rosterName + " join")

    elif cmd == "leave":
        left = roster.removePlayer(str(author)[:-5])
        if left:
            reaction = "R"
        else:
            reaction = "X"

    elif cmd == "delete":
        if roster.isAdmin(str(author)):
            for key in list(recognizedInput.rosters.keys()):
                if recognizedInput.rosters[key] == roster:
                    del recognizedInput.rosters[key]
                    reaction = "R"
        else:
            reaction = "X"
            msg = "You must be the roster's creator to use this command!"

    saveRosters()
    return (msg, reaction)



# read from the roster save file and open all existing rosters
openRoster()