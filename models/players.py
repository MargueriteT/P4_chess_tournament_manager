class Player:
    """Description of the class player"""

    def __init__(self, first_name, last_name, birthday, gender, rank,
                 score_of_round, final_score_of_tournament):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.rank = int(rank)
        self.scores = dict()
        self.score_of_round = score_of_round
        self.final_score_of_tournament = final_score_of_tournament
        self.final_score = dict()

    def __repr__(self):
        """This function display an instance of the class player with
        explicit data.
        """
        return "name :%r %r , rank: %r , score of tournament %r, " \
               "score_of_round %r" % (
                self.first_name, self.last_name, self.rank,
                self.scores, self.score_of_round)

    def update_ranking(self, new_ranking):
        self.rank = self.rank + int(new_ranking)
