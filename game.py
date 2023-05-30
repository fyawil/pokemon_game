import requests
import random

class FriendlyPokemon:
    def __init__(self, name):
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
        self.name = name
        self.health = data["base_experience"]
        self.height = data["height"]
        self.weight = data["weight"]
        self.moves_json = data["moves"]

    def __str__(self):
        return f"""{self.name.capitalize()}:
Health: {self.health}
Height: {self.height}
Weight: {self.weight}
Moves: 
{self.get_moves_list()}
"""

    def get_moves_list(self):
        moves_list = []
        for i, move_dict in enumerate(self.moves_json):
            moves_list.append(self.moves_json[i]["move"]["name"])
        return moves_list
    
    def attack(self, enemy_pokemon):
        while True:
            attacking_move = input(f"""
ENTER AN ATTACKING MOVE NOW:
{self.get_moves_list()}
: """)
            if attacking_move not in self.get_moves_list():
                print(f"{self.name} CANNOT ATTACK LIKE THAT...")
                continue
            attacking_move_power = requests.get(f"https://pokeapi.co/api/v2/move/{attacking_move}").json()["power"]
            if attacking_move_power == None:
                attacking_move_power = 0
            enemy_pokemon.health -= attacking_move_power

            print(f"{self.name} {attacking_move}'d {enemy_pokemon.name}. It's health is now {enemy_pokemon.health}")
            break


class EnemyPokemon:
    def __init__(self):
        data_for_name = requests.get(
            f"https://pokeapi.co/api/v2/pokemon").json()["results"][random.randint(0, 19)]
        self.name = data_for_name["name"]
        data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{self.name}").json()
        self.health = data["base_experience"]
        self.moves_json = data["moves"]

    def get_moves_list(self):
        moves_list = []
        for i, move_dict in enumerate(self.moves_json):
            moves_list.append(self.moves_json[i]["move"]["name"])
        return moves_list

    def attack(self, friendly_pokemon):
        while True:
            attacking_move = self.get_moves_list()[random.randint(0, len(self.get_moves_list()) - 1)]
            attacking_move_power = requests.get(f"https://pokeapi.co/api/v2/move/{attacking_move}").json()["power"]
            if attacking_move_power == None:
                attacking_move_power = 0

            friendly_pokemon.health -= attacking_move_power

            print(f"{self.name} {attacking_move}'d {friendly_pokemon.name}. It's health is now {friendly_pokemon.health}")
            break


def choose_pokemon():
    while True:

        friendly_pokemon_name = input(
            "Please enter the name of your chosen Pokemon: ")

        try:
            friendly_pokemon = FriendlyPokemon(friendly_pokemon_name)
        except:
            print("Pokemon not found...")
            continue
        break

    print(f"""
YOU CHOSE {friendly_pokemon}""")
    return friendly_pokemon

def start_game():

    friendly_pokemon = choose_pokemon()

    for i in range(1, 11):

        print(f"ROUND {i}...")
        print("WHO IS THAT POKEMON?")
        enemy_pokemon = EnemyPokemon()
        print(f"IT'S {enemy_pokemon.name.upper()} it's health is {enemy_pokemon.health}")
        while friendly_pokemon.health > 0 and enemy_pokemon.health > 0:
            friendly_pokemon.attack(enemy_pokemon)
            enemy_pokemon.attack(friendly_pokemon)
        
        if friendly_pokemon.health < 0:
            print("GAME OVER!!!!!!!!!!!!!!")
            break
        friendly_pokemon.health *= 2

    if friendly_pokemon.health > 0:
        print("YOU WON!!!!!!")


if __name__ == "__main__":
    start_game()

# https://pokeapi.co/api/v2/pokemon/pokemon_name/ where the pokemon
# https://pokeapi.co/api/v2/move/14/ move is the move derived from the pokemon
