from operator import attrgetter
from models.check_function import RoundInputChecker


class Tournament:
    """Description of the tournament class"""

    def __init__(self, name, place, start, end, number_of_players,
                 number_of_rounds, type_of_game, status):
        self.name = name
        self.place = place
        self.start = start
        self.end = end
        self.number_of_players = number_of_players
        self.number_of_rounds = number_of_rounds
        self.type_of_game = type_of_game
        self.status = status
        self.winner = None
        self.tournament_rounds_name = []
        self.tournament_players = []
        self.tournament_matches = []
        self.tournament_rounds = {}

    def add_players(self, i):
        """ This function add players to the list of players of the
        tournament and register each of them in the database list of
        players.
        """

        # add a dictionary to register the scores of the tournament
        i.scores = {self.name: {}}
        # add the player to the list of players of the new tournament
        self.tournament_players.append(i)

    def score_of_the_tournament(self):
        """ This function calculate the final score of each player, update
        the rank of the player.
        """

        for player in self.tournament_players:
            # Creation of the key to associate to the final score
            player.final_score[self.name] = 0
            for key in player.scores[self.name]:
                # add score of each round to the final score
                player.final_score[self.name] += player.scores[self.name][key]
            # the final score is temporary stock in
            # player.final_score_of_tournament to allow final classification

            player.final_score_of_tournament = player.final_score[self.name]
            player.update_ranking(player.final_score_of_tournament)
        self.tournament_players.sort(
            key=attrgetter("final_score_of_tournament"),
            reverse=True)
        # The list of player is displayed according to the final score (from
        # the best to the worst)
        return self.tournament_players

    def update_status_and_winner(self):
        """This function update the status and the winner at the end of the
        tournament.
        """

        self.status = "Finished"
        self.winner = self.tournament_players[0]
        return self.status, self.winner


class Round:
    """Description of the round class """

    def __init__(self, round_name, players, start, end):
        self.round_name = round_name
        self.players = players
        self.status = "Started"
        self.start = start
        self.end = end
        self.matches = []

    def sort_players(self, tournament_round_name):
        """ This function sort players by rank for first round and then by
        score of the last round
        """

        if len(tournament_round_name) == 1:
            # sort object player by attribute rank for first round
            self.players.sort(key=attrgetter("rank"), reverse=True)
            return self.players
        else:
            # sort object player by attribute score of the previous round,
            # and rank in case of equality
            self.players.sort(key=attrgetter("score_of_round", "rank"),
                              reverse=True)
            return self.players

    def matching_players(self, tournament_number_of_players,
                         tournament_matches):
        """This function match two players together until every one is
        paired for the round. The player are match by rank or by score
        according the round.
        """

        # Creation of two list from the sorted_list
        players_1 = self.players[0: int(tournament_number_of_players / 2)]
        players_2 = self.players[int(tournament_number_of_players / 2):]

        half_players = int(tournament_number_of_players / 2)
        # Creation of a list_of_matches for the round
        while len(self.matches) < half_players:
            # matching two players as long as long as there are players
            match = [players_1[len(self.matches)],
                     players_2[len(self.matches)]]
            check = RoundInputChecker()
            match_exist = check.check_match(match, tournament_matches)
            if match_exist == "match_exist":
                # function check_match check if the match already happened
                # in the previous round, if yes, change in the order of the
                # list
                change = players_2.pop(0)
                players_2.append(change)

                match = [players_1[len(self.matches)],
                         players_2[len(self.matches)]]

                self.matches.append(match)
                tournament_matches.append(match)

            elif match_exist == "not":
                # if not, add directly the match to the list
                self.matches.append(match)
                tournament_matches.append(match)

        return tournament_matches

    def enter_score_of_round(self, player, score, tournament_name):
        """This function display the name of each player of the list to enter
        the score he had at the round.
        """

        player.score_of_round = score
        player.scores[tournament_name][self.round_name] = score
        p = (player, score)
        return p

    def add_the_round_to_tournament(self, tournament):
        """This function update the tournament_rounds dictionary as:
        key = round name
        value = a list constituted of all the matches
        Each match is a list constituted of two tuples.
        Each tuple is constituted of an instance of player and his score for
        the match.
        """
        tournament.tournament_rounds[self.round_name] = self.matches

    def end_the_round(self):
        """This function checks the end time of the round and change
        the status to Finished.
        """
        check = RoundInputChecker()
        self.status = "Finished"
        self.end = check.check_time_round()
