from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from data_structures.abstract_list import List

# class MyList(abstract_list.List):
#     def __init__(self):
#         super().__init__()
#         self._data = []  # Initialize a list to store data
    
#     def __getitem__(self, index):
#         return self._data[index]  # Implement __getitem__ method
    
#     def __setitem__(self, index, value):
#         self._data[index] = value  # Implement __setitem__ method
    
#     def delete_at_index(self, index):
#         del self._data[index]  # Implement delete_at_index method
    
#     def index(self, item):
#         return self._data.index(item)  # Implement index method
    
#     def insert(self, index, item):
#         self._data.insert(index, item)  # Implement insert method


class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self):
        self.team = List()
        self.team_count = 0

    def choose_manually(self):
        while len(self.team) < self.TEAM_LIMIT:
            print("Choose a Pokemon type (or press Enter to finish):")
            print("Available Pokemon types:", self.POKE_LIST)
            pokemon_type = input("Enter Pokemon type: ")
            if not pokemon_type:
                break
            if pokemon_type in self.POKE_LIST:
                self.team.append(pokemon_type)
                self.team_count += 1
            else:
                print("Invalid Pokemon type. Please choose from the available types.")

    def choose_randomly(self) -> None:
        all_pokemon = get_all_pokemon_types()
        self.team_count = 0
        for _ in range(self.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team.append(all_pokemon[rand_int])
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None:
        for pokemon_type in self.team:
            # Code to regenerate Pokemon team based on battle mode and criterion
            pass

    def assign_team(self, criterion: str = None) -> None:
        pass

    def assemble_team(self, battle_mode: BattleMode) -> None:
        pass

    def special(self, battle_mode: BattleMode) -> None:
        pass

    def __getitem__(self, index: int):
        return self.team[index]

    def __len__(self):
        return len(self.team)

    def __str__(self):
        return '\n'.join(str(pokemon) for pokemon in self.team)

class Trainer:

    def __init__(self, name) -> None:
        self.name = name
        self.poke_team = PokeTeam()
        self.pokedex = List()

    def pick_team(self, method: str) -> None:
        if method == 'Random':
            self.poke_team.choose_randomly()
        elif method == 'Manual':
            self.poke_team.choose_manually()
        else:
            raise ValueError("Invalid team selection method! Please choose 'Random' or 'Manual'.")

    def get_team(self) -> PokeTeam:
        return self.poke_team

    def get_name(self) -> str:
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None:
        pokemon_type = Pokemon.get_poketype(pokemon)
        self.pokedex.append(pokemon_type)
    
    def get_pokedex_completion(self) -> float:
        total_types = len(PokeType)
        seen_types = 0
        for p_type in self.pokedex:
            if p_type != PokeType.FIRE:
                seen_types += 1
        if PokeType.FIRE in self.pokedex:
            seen_types += 1  # Increment if FIRE type is seen
        return round(seen_types / total_types, 2)  # Calculate completion percentage

    def __str__(self) -> str:
        completion = int((self.get_pokedex_completion()) * 100)
        return f"Trainer {self.name} Pokedex Completion: {completion}%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
