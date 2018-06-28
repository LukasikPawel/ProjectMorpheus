import random


def create_assignments():
    """
    Function creates Cru and SPOE assignments for given list of developers.
    Devs with level Low are not assigned and those with level High can be assigned twice.
    Assigned people always have level different than dev and can't be assigned to both functions at the same time.
    """

    assignment = [
        ['PG', 'H', ],
        ['PL', 'H', ],
        ['MB', 'H', ],
        ['KK', 'H', ],
        ['MI', 'M', ],
        ['MM', 'M', ],
        ['PS', 'M', ],
        ['DF', 'M', ],
        ['JS', 'L', ],
        ['JO', 'L', ],
    ]

    for entry in assignment:  # Add dummy entries as placeholders
        entry.append("CRU")
        entry.append("SPOE")

    for index in range(2):  # Cru is assigned first, then SPOE
        random_list = random.sample(assignment, len(assignment))
        for developer in assignment:
            for someone in random_list:
                already_taken = [x[index+2] for x in assignment]
                if (someone[0] != developer[0] and      # Someone's name different than dev's name
                    someone[0] != developer[2] and      # Someone isn't added as Cru already
                    someone[1] != developer[1] and      # Someone's level different than dev's level
                    someone[1] != 'L' and               # Someone's level isn't Low
                    someone[0] not in already_taken):   # Someone isn't assigned to anyone else yet
                    # Assign someone to current developer
                    developer[index+2] = someone[0]
                    break
        for developer in assignment:  # Second loop to assign High level devs into missing places
            if developer[index+2] in ("CRU", "SPOE"):
                for someone in [x for x in random_list if x[1] == "H"]:
                    already_taken = [x[index+2] for x in assignment]
                    if someone[0] != developer[2] and already_taken.count(someone[0]) < 2:
                        # Assign someone to current developer
                        developer[index+2] = someone[0]
                        break
    return assignment


def print_results(assignment):
    # Print results in a nice table format :)
    print(" ------------------")
    print("| Dev | Cru | SPOE |")
    print(" ------------------")
    for developer in assignment:
        print("| {}: | {}  |  {}  |".format(developer[0], developer[2], developer[3]))
    print(" ------------------")


while True:
    print_results(create_assignments())
    input("Press enter to generate again: ")
