
class MusJudger:

    @staticmethod
    def judge_winner(players):
        ''' Judge the winner of the game

        Args:
            players (list): The list of players who play the game

        Returns:
            (list): The player id of the winner or None
        '''

        for id, player in enumerate(players):
            if player.chickpeas >= 40:
                return id
            
        return None