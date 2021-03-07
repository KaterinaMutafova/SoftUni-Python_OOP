from encaps_ex3_team.player import Player


class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, value):
        self.__players = value

    def add_player(self, player: Player):
        filtered_player = [p for p in self.players if p == player]
        if not filtered_player:
            self.players.append(player)
            return f"Player {player.name} joined team {self.name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        filtered_players = [p for p in self.players if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} not found"
        filtered_player = filtered_players[0]
        self.__players.remove(filtered_player)
        return filtered_player

