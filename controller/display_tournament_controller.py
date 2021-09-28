from models.database import Database
from views.view import MainViews
from models.check_function import Commands


class DatabaseTournamentDisplay:
    def __init__(self, main_menu):
        self.database = Database()
        self.main_view = MainViews()
        self.command = Commands()
        self.main_menu = main_menu

    def display_menu_tournament_database_display(self):
        """This method display a menu for the user to choose if he wants
        to display all the tournament (date or alphabetical order) or to see
        one tournament in details and return the corresponding link.
        """

        commands = {"1": self.display_all_tournaments_alphabetical,
                    "2": self.display_all_tournaments_date,
                    "3": self.display_detailed_tournament,
                    "4": self.display_all_players_of_a_tournament,
                    "5": self.main_menu}
        self.main_view.display_tournaments_view(commands)()

    def display_all_tournaments_alphabetical(self):
        """This function recover the list of tournaments ordered
        alphabetically and display it for the user. Then, the user can go
        back to main menu.
        """

        # Recover alphabetical list
        alphabetical_ordered = \
            self.database.display_tournaments_alphabetical_order()
        # Display the list
        self.main_view.display_tournament_alphabetical_view(
            alphabetical_ordered)
        # Link to the main menu
        self.command.display_message("\n\n1 - Go back to the main menu  ")
        commands = {"1": self.main_menu}
        self.command.check_command(commands)()

    def display_all_tournaments_date(self):
        """This function recover the list of tournaments ordered by beginning
        date and display it for the user. Then, the user can go
        back to main menu.
        """

        # Recover date list
        date_ordered = \
            self.database.display_tournaments_date_order()
        #  Display the list
        self.main_view.display_tournament_date_view(
            date_ordered)
        # Link to the main menu
        self.command.display_message("\n\n1 - Go back to the main menu  ")
        commands = {"1": self.main_menu}
        self.command.check_command(commands)()

    def display_all_players_of_a_tournament(self):
        """This method return a menu for the user to choose how he wants the
        tournament's players to be sorted and then display the list of
        players as chosen by the user.
        """
        # Recover alphabetical list
        alphabetical_ordered = \
            self.database.display_tournaments_alphabetical_order()
        # View to search the tournament
        tournament = self.search_a_tournament(alphabetical_ordered)
        self.command.display_message(
            f"How do you want to display the list of players of the "
            f"tournament {tournament['name']} ?\n"
            f"\t 1 - Alphabetical"
            f"\t 2 - Ranking")
        commands = {"1": "alphabetical",
                    "2": "ranking"}
        choice = self.command.check_command(commands)

        if choice == "alphabetical":
            alpha = self.database.sort_players_alphabetical_order(
                tournament['list_of_players'])
            self.main_view.display_players_alphabetical_views(alpha)
            self.command.display_message("\n\n1 - Go back to the main menu  ")
            commands = {"1": self.main_menu}
            self.command.check_command(commands)()

        elif choice == "ranking":
            ranking = self.database.sort_players_rank_order(tournament[
                                                      'list_of_players'])
            self.main_view.display_players_by_rank_views(ranking)
            # Commands to go back to main menu
            self.command.display_message("\n\n1 - Go back to the main menu  ")
            commands = {"1": self.main_menu}
            self.command.check_command(commands)()
        else:
            self.command.display_message("\n\n1 - Go back to the main menu  ")
            commands = {"1": self.main_menu}
            self.command.check_command(commands)()

    def display_detailed_tournament(self):
        """This function invites an user to choose the tournament he wants
        details on and then display it.
        """
        # Recover alphabetical list
        alphabetical_ordered = \
            self.database.display_tournaments_alphabetical_order()

        # View to search a tournament
        tournament = self.search_a_tournament(alphabetical_ordered)
        # View to display details
        self.main_view.display_detailed_tournament(tournament)
        # Commands to go back to main menu
        self.command.display_message("\n\n1 - Go back to the main menu  ")
        commands = {"1": self.main_menu}
        self.command.check_command(commands)()

    def search_a_tournament(self, list):
        """This function allows the search of a tournament by name and if
        necessary by name and location and then return the tournament's
        data. If the tournament doesn't exist in the database then the user
        is informed and redirected to the main menu.
        """

        # View with input and return the user input
        name = self.main_view.search_a_tournament_by_name_view(list)
        # Search with the name in the database
        tournament = self.database.search_tournament_in_database_with_name(
            name)

        if not tournament:
            # No tournaments with the name : redirection main menu
            commands = {"1": self.main_menu}
            self.command.check_command(commands)()
        elif len(tournament) != 1:
            # Several tournament with the same name, user must precised
            # location
            name_2, location_2 = \
                self.main_view.search_a_tournament_by_name_and_place_view(
                    name, tournament)
            tournament = self.database.search_tournament_name_and_location(
                name_2, location_2)
            return tournament[0]
        else:
            # tournament found
            return tournament[0]
