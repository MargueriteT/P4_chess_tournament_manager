import datetime


class Commands:
    """ This class define three methods to help display the data and manage
    the user commands.
    """

    @staticmethod
    def display_message(message):
        """ Display the any text passed as an argument. """
        print(message)

    @staticmethod
    def check_command(commands):
        """ Allows the user to enter an input and check is validity before
        returned command.
        """
        command = input("\t Please enter your command")

        while command not in commands:
            print("The command is invalid, please try again")
            command = input("Enter your new command")
        return commands[command]

    def valid_action(self):
        """ This function validate a user' action. """
        self.display_message("Do you want to validate ?  \n\n"
                             "\t\t 1 - Yes \n"
                             "\t\t 2 - No \n")
        commands = {"1": "yes", "2": "no"}
        command = input("Please enter your command")

        while command not in commands:
            print("The command is invalid, please try again")
            command = input("Please enter your command")
        return commands[command]


class TournamentInputChecker:
    """ This class define several methods that verify if the user input is
    valid and return the checked data on tournament.
    """
    @staticmethod
    def check_name():
        """This method checks the validity of the input name """

        name = input("Enter the name (2 to 20 characters) \n")
        while not 2 < len(name) < 20:
            print("The input is not valid, please enter a valid name")
            name = input("Enter the name (2 to 20 characters) \n")
        return name.capitalize()

    @staticmethod
    def check_location():
        """This method checks the validity of the input location """

        location = input("Enter the location of the tournament (2 to 20 "
                         "characters) \n")
        while not 2 < len(location) < 20:
            print("The input is not valid, please enter a valid location")
            location = input("Enter the location of the tournament (2 to 20 "
                             "characters) \n")
        return location.capitalize()

    @staticmethod
    def check_starting_date():
        """This method checks the validity of the input date """

        date = input("Enter the starting date as yyyy/mm/dd \n")
        while True:
            try:
                year, month, day = map(int, date.split('/'))
                starting_date = datetime.date(year, month, day)
                return starting_date

            except ValueError:
                print("This date is not valid. Please try again")
                date = input("Enter the starting date as yyyy/mm/dd \n")

    @staticmethod
    def check_ending_date(starting_date):
        """This method checks the validity of the input date and return it.
        If no ending date is enter then it sets the ending date equal to
        the beginning date.
        """
        date = input("Enter the ending date as yyyy/mm/dd \n")
        if date == "":
            date = starting_date
            return date
        else:
            while True:
                try:
                    year, month, day = map(int, date.split('/'))
                    ending_date = datetime.date(year, month, day)
                    return ending_date

                except ValueError:
                    print("This date is not valid. Please try again")
                    date = input("Enter the ending date as yyyy/mm/dd \n")

    @staticmethod
    def check_number_of_players():
        """This method checks the validity of the input number of players and
        sets it to 8 by default if no input.
        """
        number_of_players = input("Enter the number of players \n")
        if number_of_players == "":
            number_of_players = 8
            return number_of_players
        else:
            while True:
                try:
                    number_of_players = int(number_of_players)
                    return number_of_players
                except ValueError:
                    print("This is not a valid number. Please try again")
                    number_of_players = input("Enter the number of players \n")

    @staticmethod
    def check_number_of_rounds():
        """This method checks the validity of the input number of rounds and
        sets it to 4 by default if no input.
        """
        number_of_rounds = input("Enter the number of rounds \n")
        if number_of_rounds == "":
            number_of_rounds = 4
            return number_of_rounds
        else:
            while True:
                try:
                    number_of_rounds = int(number_of_rounds)
                    return number_of_rounds
                except ValueError:
                    print("This is not a valid number. Please try again")
                    number_of_rounds = input("Enter the number of rounds \n")

    @staticmethod
    def check_type_of_game():
        """This method return the type of game choose by the user."""

        Commands.display_message("Choose the type of game \n\n"
                                 "\t\t 1 - Blitz \n"
                                 "\t\t 2 - Bullets \n"
                                 "\t\t 3 - Coup rapide \n")

        commands = {"1": "Blitz", "2": "Bullets", "3": "Coup rapide"}
        type_of_game = Commands.check_command(commands)
        return type_of_game


class PlayerInputChecker:
    """ This class define several methods that verify if the user input is
    valid and return the checked data on player.
    """

    @staticmethod
    def check_first_name():
        """This method checks the validity of the input first name and
        return it.
        """
        first_name = input("Enter the first name (2 to 20 characters) \n")
        while not 2 < len(first_name) < 20:
            print("The input is not valid, please enter a valid first name")
            first_name = input("Enter the first name (2 to 20 characters) \n")
        return first_name.capitalize()

    @staticmethod
    def check_last_name():
        """This method checks the validity of the input last name and
        return it.
        """
        last_name = input("Enter the last name (2 to 20 characters) \n")
        while not 2 < len(last_name) < 20:
            print("The input is not valid, please enter a valid last name")
            last_name = input("Enter the last name (2 to 20 characters) \n")
        return last_name.capitalize()

    @staticmethod
    def check_birthday():
        """This method checks the validity of the input birthday and
        return it.
        """
        birthday = input("Enter the birthday as yyyy/mm/dd \n")
        while True:
            try:
                year, month, day = map(int, birthday.split('/'))
                birthday = datetime.date(year, month, day)
                return birthday

            except ValueError:
                print("This date is not valid. Please try again")
                birthday = input("Enter the birthday as yyyy/mm/dd \n")

    @staticmethod
    def check_gender():
        """This method return the gender choose by the user"""
        Commands.display_message("Choose gender \n\n"
                                 "\t\t 1 - Man \n"
                                 "\t\t 2 - Woman \n")
        commands = {"1": "Man", "2": "Woman"}
        gender = Commands.check_command(commands)
        return gender

    @staticmethod
    def check_rank():
        """This method checks the validity of the input rank and
        return it.
        """
        rank = input("Enter the rank \n")
        while True:
            try:
                rank = int(rank)
                return rank
            except ValueError:
                print("This is not a valid number. Please try again")
                rank = input("Enter the rank \n")


class RoundInputChecker:
    """ This class define several methods that verify if the user input is
    valid and return the checked data on round.
    """

    @staticmethod
    def check_the_round_name():
        """ This function check the len of the round name and ask the user
        until the input is correct and then return the name capitalized.
        """

        round_name = input("Enter the round name's (2 to 20 characters)\n")
        while not 2 < len(round_name) < 20:
            print("The input is not valid, please enter a valid name for the "
                  "round")
            round_name = input("Enter the name of the round (2 to 20 "
                               "characters) \n")
        return round_name.capitalize()

    @staticmethod
    def check_time_round():
        """ This method return time and date. """

        time = datetime.datetime.now()
        return time

    @staticmethod
    def check_match(match, matches):
        """ This method checks if a match as already been played between
        two players and return if it had or not.
        """

        if [match[0], match[1]] in matches:
            return "match_exist"
        elif [match[1], match[0]] in matches:
            return "match_exist"
        else:
            return "not"

    @staticmethod
    def check_score():
        """ This method allows a user to choose if a player had lost,
        won or been in a draw and return the corresponding value.
        """
        Commands.display_message("Choose : \n\n"
                                 "\t\t 1 - Won \n"
                                 "\t\t 2 - Lost \n"
                                 "\t\t 3 - Draw \n")
        commands = {"1": 1, "2": 0, "3": 0.5}
        score = Commands.check_command(commands)
        return score
