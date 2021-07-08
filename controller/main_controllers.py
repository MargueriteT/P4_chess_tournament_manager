from controller.play_controller import PlayATournament
from controller.resume_controller import ResumeATournament
from controller.display_tournament_controller import DatabaseTournamentDisplay
from controller.display_player_controller import DatabasePlayerDisplay
from views.view import MainViews


class MainMenuController:
    """This class launched the main menu to start the app"""
    def __init__(self):
        self.main_view = MainViews()
        self.commands = {"1": NewTournamentController,
                         "2": ResumeATournamentController,
                         "3": DatabaseTournamentDisplayController,
                         "4": DatabasePlayerDisplayController,
                         "5": quit}
        self.main_menu = self.main_view.main_menu_views(self.commands)


class NewTournamentController:
    """This class initiate the creation of a tournament and then all the
    sequence of a tournament.
    """
    def __init__(self):
        self.main_menu = MainMenuController
        self.play = PlayATournament(self.main_menu)
        self.play.create_a_new_tournament()


class ResumeATournamentController:
    """This class initiate the sequence of a tournament from a tournament
    already created and saved in the database.
    """
    def __init__(self):
        self.main_menu = MainMenuController
        self.tournament = ResumeATournament(self.main_menu).tournaments_data()
        self.play = PlayATournament(self.main_menu)
        if len(self.tournament.tournament_players) == 0:
            self.play.add_players_to_the_tournament(self.tournament)
        elif len(self.tournament.tournament_rounds_name) != \
                self.tournament.number_of_rounds:
            self.play.play_a_round(self.tournament)
        else:
            self.play.end_the_tournament(self.tournament)


class DatabaseTournamentDisplayController:
    """This class initiate the access to the tournament database and display
    the information search by the user.
    """
    def __init__(self):
        self.main_menu = MainMenuController
        self.play = DatabaseTournamentDisplay(self.main_menu)
        self.play.display_menu_tournament_database_display()


class DatabasePlayerDisplayController:
    """This class initiate the access to the players database and display
    the information search by the user.
    """
    def __init__(self):
        self.main_menu = MainMenuController
        self.play = DatabasePlayerDisplay(self.main_menu)
        self.play.display_menu_player_database_display()
