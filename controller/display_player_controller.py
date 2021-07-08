from models.database import Database
from views.view import MainViews
from models.check_function import Commands


class DatabasePlayerDisplay:
    def __init__(self, main_menu):
        self.database = Database()
        self.main_view = MainViews()
        self.command = Commands()
        self.main_menu = main_menu

    def display_menu_player_database_display(self):
        """This method display a menu for the user to choose if he wants
        to display all players by rank or alphabetical order) and return the
        corresponding link.
        """
        commands = {"1": self.display_all_players_alphabetical,
                    "2": self.display_all_players_by_ranking,
                    "3": self.main_menu}
        self.main_view.display_players_main_view(commands)()

    def display_all_players_alphabetical(self):
        """This method recover the list of players ordered alphabetically
        and display it. Then, the user can go back to main menu.
        """
        alphabetical_list = self.database.sort_players_alphabetical_order(
                self.database.list_of_players)
        self.main_view.display_players_alphabetical_views(alphabetical_list)
        self.command.display_message("\n\n1 - Go back to the main menu")
        commands = {"1": self.main_menu}
        self.command.check_command(commands)()

    def display_all_players_by_ranking(self):
        """This method recover the list of tournaments ordered by rank and
        display it. Then, the user can go back to main menu.
        """
        ranking_list = self.database.sort_players_rank_order(
                self.database.list_of_players)
        self.main_view.display_players_by_rank_views(ranking_list)
        self.command.display_message("\n\n1 - Go back to the main menu")
        commands = {"1": self.main_menu}
        self.command.check_command(commands)()
