from tinydb import TinyDB, Query
from models.players import Player
from models.tournament import Tournament


class Database:
    """ This class create and organise all information to register into the
    database"""

    def __init__(self):
        """The init function create the database"""

        self.database = TinyDB('database.json')
        self.list_of_tournaments = self.database.table('list_of_tournaments')
        self.list_of_players = self.database.table('list_of_players')

    def clear_tournament_table(self):
        self.list_of_tournaments.truncate()

    def clear_player_table(self):
        self.list_of_players.truncate()

    """Functions to transform registered data into an INSTANCE"""
    @staticmethod
    def transform_a_registered_player_into_instance(player):
        """ This function transform a registered player to an instance of
        class Player.
        """
        object_player = Player(player['first_name'],
                               player['last_name'],
                               player['birthday'],
                               player['gender'],
                               player['rank'],
                               player['score_of_round'],
                               player['final_score_of_tournament'])
        object_player.scores = player["scores"]
        object_player.final_score = player['final_score']
        return object_player

    @staticmethod
    def transform_a_registered_tournament_into_instance(tournament_to_resume):
        """ This function set back tournament to resume' data to an instance
        of class Tournament that can be used to pursue tournament.
        """

        tournament = Tournament(tournament_to_resume['name'],
                                tournament_to_resume['location'],
                                tournament_to_resume['beginning_date'],
                                tournament_to_resume['ending_date'],
                                tournament_to_resume['number_of_players'],
                                tournament_to_resume['number_of_rounds'],
                                tournament_to_resume['type_of_game'],
                                tournament_to_resume['status'])
        if tournament_to_resume['winner'] is None:
            tournament.winner = None
        else:
            tournament.winner = \
                Database.transform_a_registered_player_into_instance(
                    tournament_to_resume['winner'])
        tournament.tournament_players = \
            Database().transform_a_registered_list_of_players_into_instances(
                tournament_to_resume)
        tournament.tournament_rounds_name = \
            tournament_to_resume["tournament_rounds_name"]
        tournament.tournament_rounds = {}

        # transform each paired round_name/list of matches for tournament
        # instance
        for round_name, matches in tournament_to_resume["list_of_round"].items(
        ):
            list_of_match = []
            for match in matches:
                object_match = []
                for player in match:
                    object_tuple = (
                        Database.transform_a_registered_player_into_instance(
                            player[0]), int(player[1]))
                    object_match.append(object_tuple)
                list_of_match.append(object_match)
            tournament.tournament_rounds[round_name] = list_of_match

        tournament.tournament_matches = list()
        for x in range(len(tournament_to_resume['matches'])):
            one_match = list()
            for player in tournament_to_resume['matches'][x]:
                p_obj = Database().transform_a_registered_player_into_instance(
                    player)
                one_match.append(p_obj)
            tournament.tournament_matches.append(one_match)

        return tournament

    @staticmethod
    def transform_a_registered_list_of_players_into_instances(
            tournament_to_resume):
        """This function transform a list of players' instance to data that
        can be saved in the database.
        """

        players_list = []
        for player in tournament_to_resume["list_of_players"]:
            object_player = Database.\
                transform_a_registered_player_into_instance(player)
            players_list.append(object_player)

        return players_list

    """Functions to transform an object into REGISTRABLE DATA"""

    @staticmethod
    def transform_player_object_to_json(player):
        if isinstance(player, Player):
            json_player = {'__class__': 'Player',
                           'first_name': player.first_name,
                           'last_name': player.last_name,
                           'birthday': str(player.birthday),
                           'gender': player.gender,
                           'rank': player.rank,
                           'score_of_round': player.score_of_round,
                           'scores': player.scores,
                           'final_score_of_tournament':
                               player.final_score_of_tournament,
                           'final_score': player.final_score}
            return json_player

    @staticmethod
    def transform_a_list_of_players_to_json(obj):
        """This function transform a list of players' instance to data that
        can be saved in the database.
        """

        players_list = []
        for player in obj.tournament_players:
            json_player = Database.transform_player_object_to_json(player)
            players_list.append(json_player)
        return players_list

    @staticmethod
    def transform_a_list_of_matches_to_json(obj):
        """This function transform a list of match to data that can be saved
        in the database.
        """
        all_matches = []
        for match in obj.tournament_matches:
            one_match_json = []
            for player in match:
                json_player = Database.transform_player_object_to_json(
                    player)
                one_match_json.append(json_player)

            all_matches.append(one_match_json)
        return all_matches

    @staticmethod
    def transform_a_dictionary_of_round_to_json(obj):
        """This function convert the data of the tournament round dictionary
        in data that can be saved in the database.
        """

        if obj.tournament_rounds:
            list_of_rounds_json = {}
            for key, values in obj.tournament_rounds.items():
                # for each key (= round name), value (= list of matches)
                matches = []
                for match in values:
                    # for each match in the list
                    one_match = []
                    for player_score in match:
                        # for each tuple (player, score)
                        player = Database.transform_player_object_to_json(
                            player_score[0])
                        score = player_score[1]
                        player_score_json = (player, score)
                        one_match.append(player_score_json)
                    matches.append(one_match)
                list_of_rounds_json[key] = matches
            return list_of_rounds_json
        else:
            return {}

    def register_player(self, player):
        """This function check the existence of the player in the database.
        It converts object's data to json data to add the player to the table
        list_of_players or update his data in the table.
        """
        if isinstance(player, Player):
            self.list_of_players.upsert(
                {'__class__': 'Player',
                 'first_name': player.first_name,
                 'last_name': player.last_name,
                 'birthday': str(player.birthday),
                 'gender': player.gender,
                 'rank': player.rank,
                 'score_of_round': player.score_of_round,
                 'final_score_of_tournament': player.final_score_of_tournament,
                 "scores": player.scores,
                 'final_score': player.final_score
                 },
                (Query().last_name == player.last_name)
                & (Query().first_name == player.first_name)
                & (Query().birthday == str(player.birthday)))

    def update_tournament_in_database(self, obj):
        """ The function add instance of Tournament to the database table
        list_of_tournaments and update the data in a format support by json
        file.
        """
        list_of_matches = []
        for match in obj.tournament_matches:
            m_json = []
            for player in match:
                p_json = self.transform_player_object_to_json(player)
                m_json.append(p_json)
            list_of_matches.append(m_json)

        self.list_of_tournaments.upsert(
            {"__class__": "Tournament",
             "name": obj.name,
             "location": obj.place,
             "beginning_date": str(obj.start),
             "ending_date": str(obj.end),
             "number_of_players": obj.number_of_players,
             "number_of_rounds": obj.number_of_rounds,
             "type_of_game": obj.type_of_game,
             "status": obj.status,
             "winner": self.transform_player_object_to_json(obj.winner),
             "tournament_rounds_name": obj.tournament_rounds_name,
             "list_of_players": self.transform_a_list_of_players_to_json(obj),
             "matches": list_of_matches,
             "list_of_round": self.transform_a_dictionary_of_round_to_json(
                 obj)},
            ((Query().name == obj.name)
             & (Query().location == obj.place)
             & (Query().beginning_date == str(
                        obj.start))
             & (Query().ending_date == str(
                        obj.end))))

    """Functions to search or select information on a tournament in the
    database
    """

    def search_tournament_in_database_with_name(self, name_input):
        """This function search if the tournament the user is looking for
        is in the database and return it.
        """

        tournament = self.list_of_tournaments.search(Query().name ==
                                                     str(name_input))
        if len(tournament) == 0:
            return tournament

        return tournament

    def search_tournament_name_and_location(self, name_input, location_input):
        """This function search if the tournament the user is looking for
        is in the database and return it.
        """

        tournament = self.list_of_tournaments.search(
            (Query().name == str(name_input)) & (Query().location ==
                                                 str(location_input)))
        if len(tournament) == 0:
            print("The tournament you're searching for doesn't exist. You "
                  "can try a new name or create a new tournament")

        return tournament

    def search_tournament_in_database_by_status(self):
        """This function search if the tournament the user is looking for
        is in the database and return it.
        """

        tournaments = self.list_of_tournaments.search(Query().status ==
                                                      'In progress')
        if len(tournaments) == 0:
            return 0
        return tournaments

    def display_tournaments_alphabetical_order(self):
        """This function return tournaments registered in the database
        by alphabetical order.
        """

        return sorted(self.list_of_tournaments, key=lambda t: t["name"])

    def display_tournaments_date_order(self):
        """This function return tournaments registered in the database
        from most recent to oldest.
        """

        return sorted(self.list_of_tournaments, key=lambda t: t[
            "beginning_date"], reverse=True)

    """Functions to search/select information on players in the database"""

    @staticmethod
    def sort_players_alphabetical_order(players_list):
        """This function display a list of players by alphabetical order"""

        return sorted(players_list, key=lambda t: (t[
                                                       "last_name"],
                                                   t["first_name"]))

    @staticmethod
    def sort_players_rank_order(players_list):
        """This function display a list of players from highest to lowest
        rank.
        """

        return sorted(players_list, key=lambda t: t["rank"],
                      reverse=True)
