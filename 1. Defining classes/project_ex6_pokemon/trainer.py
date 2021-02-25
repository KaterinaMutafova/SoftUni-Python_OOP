from project.pokemon import Pokemon

class Trainer:
    def __init__(self, name: str, pokemon=[]):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemon:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str):
        filtered_pokemon = [p for p in self.pokemon if p.name == pokemon_name]
        if filtered_pokemon:
            self.pokemon.remove(filtered_pokemon[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = ""
        for pok in self.pokemon:
            result += f"- {pok.pokemon_details()}\n"
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n{result}"



pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())













