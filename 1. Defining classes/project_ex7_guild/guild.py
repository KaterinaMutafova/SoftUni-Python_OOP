from project_ex7_guild.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.list_players = []

    def assign_player(self, player: Player):
        if not player.guild == self.name and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        filtered_players = [p for p in self.list_players if p == player]
        if filtered_players:
            return f"Player {player.name} is already in the guild."
        self.list_players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        filtered_names = [pl.name for pl in self.list_players if pl.name == player_name]
        if filtered_names:
            self.list_players.remove(filtered_names[0])
            self.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        res = f"Guild: {self.name}\n"
        for p in self.list_players:
            res += p.player_info()
        return res


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())












