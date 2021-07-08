from models.database import Database
from views.view import MainViews
from models.check_function import Commands


class ResumeATournament:
    """ This class allows the user to choose which tournament he wants to
    resume and return the instance selected """

    def __init__(self, main_menu):
        self.database = Database()
        self.main_view = MainViews()
        self.command = Commands()
        self.main_menu = main_menu

        # Display all tournaments with 'In progress' status for the user to
        # selected the tournament he wants to resume
        tournaments = self.database.search_tournament_in_database_by_status()
        if tournaments == 0:
            # If no tournament in progress return to main menu
            self.command.display_message(
                "There is no tournaments in progress. Please start a new "
                "tournament.")
            self.main_menu()
        else:
            tournament_to_search = self.main_view.resume_tournament_view(
                tournaments)
            # Search it in the database
            tournament = self.database.search_tournament_in_database_with_name(
                tournament_to_search)

            # If tournaments in progress continue
            if len(tournament) > 1:
                # If several tournament with the same name, search with
                # location
                tournament_name, tournament_location =\
                    self.main_view.resume_tournament_name_and_location_view(
                        tournaments)
                tournament = self.database.\
                    search_tournament_name_and_location(
                        tournament_name, tournament_location)
            elif len(tournament) == 1:
                pass
            else:
                self.command.display_message("No tournament found")
                self.main_menu()

            # Instantiate tournament with the database data
            new_tournament = Database. \
                transform_a_registered_tournament_into_instance(
                    tournament[0])
            self.tournament = new_tournament

    def tournaments_data(self):
        """ Return the instance of tournament selected. """
        return self.tournament
