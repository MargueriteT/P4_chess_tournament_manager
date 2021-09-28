from models.check_function import Commands, TournamentInputChecker, \
    PlayerInputChecker, RoundInputChecker


class MainViews:
    def __init__(self):
        self.commands = Commands()
        self.check_tournament = TournamentInputChecker()
        self.check_player = PlayerInputChecker()
        self.check_round = RoundInputChecker()

    """ Main view """

    def main_menu_views(self, commands):
        """This function display the main menu and return the user commands."""

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n "
            "\t What do you want to do ? \n "
            "\t\t 1 - Create a new tournament \n"
            "\t\t 2 - Resume a tournament \n"
            "\t\t 3 - Display all tournaments \n"
            "\t\t 4 - Display all players \n"
            "\t\t 5 - Quit \n")

        return self.commands.check_command(commands)()

    """Play a tournament views"""

    def create_tournament_view(self):
        """This function display the view to enter all information to create
        a new tournament and return those information.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n "
            "\t You choose to create a new tournament. "
            "Please complete all information necessary  \n ")

        name = self.check_tournament.check_name()
        location = self.check_tournament.check_location()
        starting_date = self.check_tournament.check_starting_date()
        ending_date = self.check_tournament.check_ending_date(starting_date)
        number_of_players = self.check_tournament.check_number_of_players()
        number_of_rounds = self.check_tournament.check_number_of_rounds()
        type_of_game = self.check_tournament.check_type_of_game()

        return name, location, starting_date, ending_date, number_of_players, \
            number_of_rounds, type_of_game

    def register_tournament_view(self):
        """This function display a view to inform the user that the
        tournament has been saved. The user can choose to continue the
        tournament or to go back to the main menu.
        """

        self.commands.display_message(
            "\t This information has been saved. \n"
            "\t Do you want to continue the tournament ? \n"
            "\t\t 1 - Yes"
            "\t\t 2 - No")
        commands = {"1": "Continue", "2": "MainMenu"}
        validate = self.commands.check_command(commands)
        return validate

    def do_not_register_new_tournament_view(self):
        """This function display a view to invite the user to save the
        tournament in the database. If he refused then the tournament is not
        register and the user is redirected to the main menu.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n "
            "\t This information will not be register. \n"
            "\t What do you want to do next ?\n "
            "\t\t 1 - Correct tournament's information\n"
            "\t\t 2 - Go back to the main menu\n")

        commands = {"1": "StartAgain", "2": "MainMenu"}
        validate = self.commands.check_command(commands)
        return validate

    def enter_players_view(self):
        """This function display a view inviting the user to enter
        information about a player and return the data.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n "
            "\t Please enter information about the player\n ")

        first_name = self.check_player.check_first_name()
        last_name = self.check_player.check_last_name()
        birthday = self.check_player.check_birthday()
        gender = self.check_player.check_gender()
        rank = self.check_player.check_rank()
        return first_name, last_name, birthday, gender, rank

    def display_players_of_the_tournament_view(self, list_of_players):
        """This function display a view of all the players of the
        tournament. The user must choose if he wants to continue the
        tournament or to be redirect to the main menu.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n "
            "\t The players of this tournament are : \n ")

        for player in list_of_players:
            self.commands.display_message(
                f"First name: {player.first_name}, "
                f"Last name: {player.last_name}, "
                f"Birthday: {player.birthday}, "
                f"Gender: {player.gender}, "
                f"Rank: {player.rank}")

        self.commands.display_message(
            "What do you want to do ? \n\n"
            "\t\t 1 - Start the tournament  \n"
            "\t\t 2 - Register and go back to the main menu \n")

        commands = {"1": "start", "2": "quit"}
        validate = self.commands.check_command(commands)
        return validate

    def enter_information_about_the_round_view(self):
        """This function display a view in which the user is invited to
        enter the name of the round and return this data.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n\n \t "
            "Please enter the name of the round \n ")
        round_name = self.check_round.check_the_round_name()
        start = self.check_round.check_time_round()
        return round_name, start

    def display_matches_view(self, matches):
        """This function display a view of the matches of the round. The
        user is invited to continue to enter the score of each player.
        """

        self.commands.display_message(
            "Those are the matches of the round: \n ")

        for match in matches:
            self.commands.display_message(
                f" \t{match[0].first_name} {match[0].last_name} VS"
                f" \t{match[1].first_name} {match[1].last_name}\n")
        commands = {"1": "continue"}
        self.commands.display_message(
            " 1 - To enter the score of each player \n")
        validate = self.commands.check_command(commands)
        return validate

    def enter_score_of_round_view(self, player):
        """This function display a view of a player first name and last name
        and an input for the user to enter score. The score is returned.
        """

        self.commands.display_message(
            f"{player.first_name} {player.last_name}")
        score = self.check_round.check_score()
        return score

    def end_the_round_view(self, players_list, status):
        """This function display a view of the end of the round. Display all
        the players and their score for the round. The user is invited to
        continue or go back to the main menu.
        """
        self.commands.display_message(" You enter all score for this round : "
                                      "\n")

        for player in players_list:
            self.commands.display_message(
                f"\t{player.first_name} {player.last_name} get: "
                f"{player.score_of_round}")

        self.commands.display_message(f"\nThe round is {status}\n")

        self.commands.display_message(
            "What do you want to do next ? \n "
            "\t\t 1 - Continue the tournament  \n"
            "\t\t 2 - Register and go back to the main menu \n")

        commands = {"1": "continue", "2": "quit"}
        validate = self.commands.check_command(commands)
        return validate

    def end_of_tournament_view(self, tournament):
        """This function display a view of the end of the tournament. Display
        the players from the highest to the lowest.
        """

        self.commands.display_message(
            f"The tournament {tournament.name} is finished. The winner "
            f"of the tournament is {tournament.winner.first_name} "
            f"{tournament.winner.last_name} with a final score of "
            f"{tournament.winner.final_score[tournament.name]}. \n\nThe "
            f"ranking "
            f"is : \n ")

        x = 1
        for player in tournament.tournament_players:
            self.commands.display_message(
                f"{x} - {player.first_name} {player.last_name}"
                f"\t Final score : {player.final_score_of_tournament}")
            x += 1

        self.commands.display_message(
            f" \nThis is the end of the tournament {tournament.name}\n "
            f" 1 - To go back to the main menu \n")
        commands = {"1": "MainMenu"}
        validate = self.commands.check_command(commands)
        return validate

    """Resume a tournament views """

    def resume_tournament_view(self, tournaments):
        """This function display a view that invites the user to choose the
        tournament he wants to resume among a list of tournament with an
        'In progress' status and return the name of the chosen tournament.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t Which tournament do you want to resume ?"
            " \n\t You can choose in the list above :\n\n")

        x = 1
        for tournament in tournaments:
            self.commands.display_message(
                f"{x} - {tournament['name']} in {tournament['location']}, "
                f"start on : {tournament['beginning_date']} with status: "
                f" {tournament['status']}")
            x += 1

        self.commands.display_message("")
        name = self.check_tournament.check_name()
        return name

    def resume_tournament_name_and_location_view(self, tournaments):
        """This function display a view that invites the user to choose the
        tournament he wants to resume among a list of tournament with an
        'In progress' status with the same name and return the name and
        location of the chosen tournament.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t There is several tournaments with this name."
            " \n\t You can choose among this list :\n\n")

        x = 1
        for tournament in tournaments:
            self.commands.display_message(
                f"{x} - {tournament['name']} in {tournament['location']}, "
                f"start on : {tournament['beginning_date']} with status: "
                f" {tournament['status']}")
            x += 1
        print("")
        self.commands.display_message("Please enter the name, then the "
                                      "location")

        self.commands.display_message("")
        tournament_name = self.check_tournament.check_name()
        tournament_location = self.check_tournament.check_location()
        return tournament_name, tournament_location

    """Display tournament views"""

    def display_tournaments_view(self, commands):
        """This function display the view of a menu allowing the user to
        choose which tournament(s) he he wants to display and how.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t How do you want to display tournaments:\n "
            "\t\t 1 - Alphabetical ?\n"
            "\t\t 2 - Date ?\n"
            "\t If you want to see specifics about one tournament: \n"
            "\t\t 3 - All details \n"
            "\t\t 4 - The list of players \n"
            "\t\t 5 - Main menu \n")
        validate = self.commands.check_command(commands)
        return validate

    def display_tournament_alphabetical_view(self, list_t):
        """This function display the view of all tournaments ordered
        alphabetically.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t Tournaments displayed by alphabetical order: ")

        for tournament in list_t:
            self.commands.display_message(
                f"Name: {tournament['name']} takes place in: "
                f"{tournament['location']}, start on:  "
                f"from: {tournament['beginning_date']} to : "
                f"{tournament['ending_date']}, type of game: "
                f"{tournament['type_of_game']}, status: "
                f"{tournament['status']}. ")
        self.commands.display_message("")

    def display_tournament_date_view(self, list_t):
        """This function display the view of all tournaments ordered
        by date.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t Tournaments displayed by date of beginning: ")

        for tournament in list_t:
            self.commands.display_message(
                f"{tournament['beginning_date']} to "
                f"{tournament['ending_date']}, type of game: "
                f"Name: {tournament['name']} take place in: "
                f"{tournament['location']}, start on:  "
                f"{tournament['type_of_game']}, status: "
                f"{tournament['status']}. ")
        self.commands.display_message("")

    def search_a_tournament_by_name_view(self, list_t):
        """This function display the view allowing an user to search for a
        tournament by name and return the name of the tournament.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n ")
        for tournament in list_t:
            self.commands.display_message(
                f"Name: {tournament['name']} takes place in: "
                f"{tournament['location']}, start on:  "
                f"from: {tournament['beginning_date']} to : "
                f"{tournament['ending_date']}, type of game: "
                f"{tournament['type_of_game']}, status: "
                f"{tournament['status']}. \n\n")

        self.commands.display_message("\n\n You choose to search a specific "
                                      "tournament. Please enter the "
                                      "name of the tournament you're "
                                      "looking for: \n")
        name = self.check_tournament.check_name()
        return name

    def search_a_tournament_by_name_and_place_view(self, name, tournaments):
        """If the name is not sufficient to find the tournament, this function
        display a view that invite the user to search for a tournament by
        name and location and return the name and location of the tournament.
        """
        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "There is several tournament with this name. ")
        for tournament in tournaments:
            self.commands.display_message(
                f"{tournament['name']}, {tournament['location']}, "
                f"start on:  {tournament['beginning_date']} and end on: "
                f"{tournament['ending_date']}, type of game: "
                f"{tournament['type_of_game']}, status: "
                f"{tournament['status']} \n\n")
        self.commands.display_message(
            "Please enter the location of the one you want to see : \n\n")
        location = self.check_tournament.check_location()
        return name, location

    def display_detailed_tournament(self, tournament):
        """This function display a view of a specific tournament. The user
        can access to all data : generic information but also the list of
        players, the description of all matches of each round of the
        tournament. If it's not possible, the function return an error
        message.
        """

        try:
            self.commands.display_message(
                f"\t\t\t {tournament['name']}\n\n"
                f"- Location: {tournament['location']}, \n"
                f"- Date: {tournament['beginning_date']} - "
                f"{tournament['ending_date']}, \n"
                f"- Number of players: {tournament['number_of_players']},\n"
                f"- Number of rounds: {tournament['number_of_rounds']}, \n"
                f"- Type of game: {tournament['type_of_game']}, \n"
                f"- Status: {tournament['status']}. \n\n"
                f"The winner of this tournament was "
                f"{tournament['winner']['first_name']}"
                f"{tournament['winner']['last_name']} with a final score "
                f"of: "
                f"{tournament['winner']['final_score'][tournament['name']]}\n"
                f"\nThe players were : \n")
            x = 1
            for player in tournament['list_of_players']:
                self.commands.display_message(
                    f"{x} - {player['first_name']} {player['last_name']}")
                x += 1
            self.commands.display_message("\n\nDescription of the tournament")
            for round_name, list_of_match in \
                    tournament['list_of_round'].items():
                self.commands.display_message(f"\t{round_name}\n")
                for match in list_of_match:
                    self.commands.display_message(
                        f"{match[0][0]['first_name']} "
                        f"{match[0][0]['last_name']} {match[0][1]} versus "
                        f"{match[1][0]['first_name']} "
                        f"{match[1][0]['last_name']} {match[1][1]}\n")
        except KeyError:
            self.commands.display_message("It's not possible to display "
                                          "this tournament. Please excuse us "
                                          "for this inconvenience.")

    """ Display players views"""

    def display_players_main_view(self, commands):
        """This function display a view of the menu for the user to choose
        how he wants to display the players of the database.
        """

        self.commands.display_message(
            "CHESS TOURNAMENT \n\n "
            "\t How do you want to display players' list:\n "
            "\t\t 1 - Alphabetical order ?\n"
            "\t\t 2 - Ranking order ?\n"
            "\t\t 3 - Main menu \n")

        validate = self.commands.check_command(commands)
        return validate

    def display_players_alphabetical_views(self, list_of_players):
        """This function display a view of the list of players sorted
        alphabetically and then redirect him to the main menu.
        """

        x = 1
        for player in list_of_players:
            self.commands.display_message(
                f"{x} - {player['last_name']} {player['first_name']} "
                f"{player['birthday']} {player['gender']} "
                f"{player['rank']}")
            x += 1

    def display_players_by_rank_views(self, list_of_players):
        """This function display a view of the list of players sorted
            by rank and then redirect him to the main menu.
            """

        # display ranking sort list
        for player in list_of_players:
            self.commands.display_message(
                f"{player['rank']} - "
                f"{player['last_name']} {player['first_name']} "
                f"{player['birthday']} {player['gender']} ")
