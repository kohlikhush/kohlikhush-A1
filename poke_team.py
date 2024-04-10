from pokemon import *
import random
from typing import List
from battle_mode import BattleMode
from data_structures.referential_array import ArrayR
from data_structures.abstract_list import List

class MyList(List):
    def __init__(self): #  Best case: O(1), Worst case: O(1)
        super().__init__()
        self._data = []  # Initialize a list to store data
    
    def __getitem__(self, index): #  Best case: O(1), Worst case: O(1)
        return self._data[index]  # Implement __getitem__ method
    
    def __setitem__(self, index, value): #  Best case: O(1), Worst case: O(1)
        self._data[index] = value  # Implement __setitem__ method
    
    def delete_at_index(self, index): # Best case: O(1) (when the item to delete is at the end of the list), Worst case: O(n) (when the item to delete is at the beginning or middle of the list, requiring elements to be shifted)
        del self._data[index]  # Implement delete_at_index method
    
    def index(self, item): # Best case: O(1), Worst case: O(n)
        return self._data.index(item)  # Implement index method
    
    def insert(self, index, item): # Best case: O(1) (when inserting at the end of the list), Worst case: O(n) (when inserting at the beginning or middle of the list, requiring elements to be shifted)
        self._data.insert(index, item)  # Implement insert method


class PokeTeam:
    TEAM_LIMIT = 6
    POKE_LIST = get_all_pokemon_types()
    CRITERION_LIST = ["health", "defence", "battle_power", "speed", "level"]

    def __init__(self): # Best case: O(1), Worst case: O(1)
        self.team = ArrayR(6)
        self.team_count = 0

    def choose_manually(self): # Best case: O(1) (when team is already filled), Worst case: O(TEAM_LIMIT) (when manually selecting Pokémon for the team)
        while len(self.team) < self.TEAM_LIMIT:
            print("Choose a Pokemon type (or press Enter to finish):")
            print("Available Pokemon types:", self.POKE_LIST)
            pokemon_type = input("Enter Pokemon type: ")
            if not pokemon_type:
                break
            if pokemon_type in self.POKE_LIST:
                self.team.__setitem__(self.team_count, pokemon_type)
                self.team_count += 1
            else:
                print("Invalid Pokemon type. Please choose from the available types.")

    def choose_randomly(self) -> None: # Best case: O(TEAM_LIMIT), Worst case: O(TEAM_LIMIT) (when randomly selecting Pokémon for the team)
        all_pokemon = get_all_pokemon_types()
        for i in range(PokeTeam.TEAM_LIMIT):
            rand_int = random.randint(0, len(all_pokemon)-1)
            self.team.append(all_pokemon[rand_int])
            self.team_count += 1

    def regenerate_team(self, battle_mode: BattleMode, criterion: str = None) -> None: #  Best case: O(1) (when the team is empty), Worst case: O(TEAM_LIMIT) (when regenerating health for each Pokémon in the team)
        for pokemon in self.team:
            parent_class = pokemon.__class__()
            max_hp = parent_class.health
            pokemon.health = max_hp        

    def assign_team(self, criterion: str = None) -> None:
        pass

    def assemble_team(self, battle_mode: BattleMode) -> None:
        pass

    def special(self, battle_mode: BattleMode) -> None:
        pass

    def __getitem__(self, index: int): # Best case: O(1), Worst case: O(1)
        return self.team[index]

    def __len__(self): # Best case: O(1), Worst case: O(1)
        return self.team_count

    def __str__(self): # Best case: O(n), Worst case: O(n) (where n is the size of the team)
        return '\n'.join(str(pokemon) for pokemon in self.team if pokemon is not None)
        
        
            

class Trainer:

    def __init__(self, name) -> None: # Best case: O(1), Worst case: O(1)
        self.name = name
        self.poke_team = PokeTeam()
        self.pokedex = MyList()

    def pick_team(self, method: str) -> None:  # Best case: O(1) (when selecting randomly), Worst case: O(TEAM_LIMIT) (when manually selecting Pokémon for the team)
        if method == 'Random':
            self.poke_team.choose_randomly()
        elif method == 'Manual':
            self.poke_team.choose_manually()
        else:
            raise ValueError("Invalid team selection method! Please choose 'Random' or 'Manual'.")

    def get_team(self) -> PokeTeam: # Best case: O(1), Worst case: O(1)
        return self.poke_team

    def get_name(self) -> str: # Best case: O(1), Worst case: O(1)
        return self.name

    def register_pokemon(self, pokemon: Pokemon) -> None: # Best case: O(1), Worst case: O(1)
        pokemon_type = Pokemon.get_poketype(pokemon)
        self.pokedex.append(pokemon_type)  
    
    def get_pokedex_completion(self) -> float: # Best case: O(n), Worst case: O(n) (where n is the number of unique Pokémon types in the Pokedex)
        total_types = len(PokeType)
        seen_types = len(set(self.pokedex))
        return round(seen_types / total_types, 2)  # Calculate completion percentage

    def __str__(self) -> str: # Best case: O(1), Worst case: O(1).
        completion = int((self.get_pokedex_completion()) * 100)
        return f"Trainer {self.name} Pokedex Completion: {completion}%"

if __name__ == '__main__':
    t = Trainer('Ash')
    print(t)
    t.pick_team("Random")
    print(t)
    print(t.get_team())
    
