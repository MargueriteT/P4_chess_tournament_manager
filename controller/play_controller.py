from models.database import Database
from models.tournament import Tournament, Round
from models.players import Player
from views.view import MainViews
from models.check_function import Commands


class PlayATournament:
    """This class describe the sequence of tournament from his creation to
    his end.
    """

    def __init__(self, main_menu):
        self.database = Database()
        self.main_view = MainViews()
        self.command = Commands()
        self.main_menu = main_menu

    def create_a_new_tournament(self):
        """This function instantiate a tournament from recovered data,
        register those main information and give the user the choice to
        pursue or go back to the main menu.
        """

        # recover tournament's information
        name, location, starting_date, ending_date, \
            number_of_players, number_of_rounds, type_of_game = \
            self.main_view.create_tournament_view()

        validate = self.command.valid_action()

        if validate == "yes":
            # If the user validate, then the tournament is instantiate and
            # register
            new_tournament = Tournament(name, location, starting_date,
                                        ending_date, number_of_players,
                                        number_of_rounds, type_of_game,
                                        status="In progress")

            self.database.update_tournament_in_database(new_tournament)
            validate = self.main_view.register_tournament_view()
            if validate == "Continue":
                self.add_players_to_the_tournament(new_tournament)
            else:
                return self.main_menu()
        else:
            # If user doesn't validate, then he can choose to go back to the
            # main menu or to enter new data
            validate = self.main_view.do_not_register_new_tournament_view()
            if validate == "StartAgain":
                self.create_a_new_tournament()
            elif validate == "MainMenu":
                return self.main_menu()

    def add_players_to_the_tournament(self, new_tournament):
        """ This function allows users to enter players of the tournament,
        add them to the players database and to the list of players of the
        tournament. Finally, the function register the tournament's data and
        offers the user to continue or to go back to the main menu.
        """

        for i in range(new_tournament.number_of_players):
            # recover player' information in view and return them
            first_name, last_name, birthday, gender, rank = \
                self.main_view.enter_players_view()
            self.command.display_message(
                f"{first_name} {last_name} {birthday} {gender} {rank}")

            validate = self.command.valid_action()

            while validate == "no":
                # the information is requested as long as the user doesn't
                # validate
                first_name, last_name, birthday, gender, rank = \
                    self.main_view.enter_players_view()
                validate = self.command.valid_action()

            # The validation allows to create an instance of Player
            player = Player(first_name, last_name, birthday, gender, rank,
                            final_score_of_tournament=0, score_of_round=0)
            # This instance is add to the players' list.
            new_tournament.add_players(player)
            # The player is added or updated in the database list of players
            self.database.register_player(player)

        # Update the tournament in the database
        self.database.update_tournament_in_database(new_tournament)

        # Display the list of players
        validate = self.main_view.display_players_of_the_tournament_view(
            new_tournament.tournament_players)

        if validate == "start":
            # Validation allows the user to start a round
            self.play_a_round(new_tournament)
        else:
            # Quit allows the user to go back to the main menu
            return self.main_menu()

    def play_a_round(self, new_tournament):
        """ This function allows the user to start a new round :
                - Choose the name of the round,
                - Sort the players,
                - Match the players and display all games,
                - Enter the score of each player for the round.
            At the end of the round, all information about the round are
            registered in the tournament round dictionary, the status of
            the round is changed to 'Finish' and the tournament is updated in
            the database.
            The user can choose to go back to the main menu or to continue
            the tournament.
        """
        while len(new_tournament.tournament_rounds_name) != \
                new_tournament.number_of_rounds:
            # The user is invited to enter the round' name.
            round_name, start = \
                self.main_view.enter_information_about_the_round_view()
            players = new_tournament.tournament_players

            # An instantiation of the class Round is created from data
            one_round = Round(round_name, players, start, end=None)

            # The name of the round is added to the round name's list of the
            # tournament
            new_tournament.tournament_rounds_name.append(one_round.round_name)

            # The player are sorted and matched for the round
            one_round.sort_players(new_tournament.tournament_rounds_name)
            one_round.matching_players(new_tournament.number_of_players,
                                       new_tournament.tournament_matches)

            # The list of matches is displayed
            self.main_view.display_matches_view(one_round.matches)

            # The score are update for all players as well as the list of match
            list_of_matches = one_round.matches[:]
            one_round.matches.clear()
            for match in list_of_matches:
                match_tuple = []
                for player in match:
                    score = self.main_view.enter_score_of_round_view(player)
                    player = one_round.enter_score_of_round(
                        player, score, new_tournament.name)
                    match_tuple.append(player)

                one_round.matches.append(match_tuple)

            # The list of rounds of the tournament is updated
            one_round.add_the_round_to_tournament(new_tournament)

            # The round end and the tournament is update in the database
            one_round.end_the_round()
            self.database.update_tournament_in_database(new_tournament)

            validate = self.main_view.end_the_round_view(
                new_tournament.tournament_players, one_round.status)

            if validate == "continue":
                # The user can continue the tournament (start a new round or
                # end the tournament if all rounds are played.
                pass
            else:
                # The user can go to the main menu
                return self.main_menu()
        self.end_the_tournament(new_tournament)

    def end_the_tournament(self, new_tournament):
        """ This function sorts the players, update the tournament in the
        database and the rank of the players of the tournament.
        """

        # The final score of each player is calculated
        ranking = new_tournament.score_of_the_tournament()

        # The players' database is updated with the new rank of the player
        for player in ranking:
            self.database.register_player(player)

        # The tournament status and the winner are updated
        new_tournament.update_status_and_winner()

        self.database.update_tournament_in_database(new_tournament)

        validate = self.main_view.end_of_tournament_view(new_tournament)
        if validate == "MainMenu":
            # If validation ok user goes back to the main menu
            return self.main_menu()
