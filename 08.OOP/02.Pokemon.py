class Pokemon:
    def __init__(self, name: str, max_armor: int, max_attack: int):
        self.name = name
        self.max_armor = max_armor
        self.max_attack = max_attack

    def attack(self):
        print(f"{self.name} is now attacking")
    
    def defend(self):
        print(f"{self.name} is now defending")

    def rest(self):
        print(f"{self.name} is now taking rest")

class ElectricPokemon(Pokemon):   
    def wild_charge(self):
        print("Static is now attacking")
        
class FlyingPokemon(Pokemon):
    def dragon_ascent(self):
        print("Dragon is now attacking")

class WaterPokemon(Pokemon): 
    def __init__(self, name: str, max_armor: int, max_attack: int, speed: int):
        Pokemon.__init__(self, name, max_armor, max_attack)
        self.speed = speed
    def aqua_tail(self):
        print("Aqua is now attacking")


pikachu = Pokemon("Pikachu", 100, 1000)
raichu = ElectricPokemon("Raichu", 500, 1000)
vaporeon = WaterPokemon("Vaporeon", 99, 1000, 500)
togekiss = FlyingPokemon("Togekiss", 100, 500,)


Pokemons = (pikachu, vaporeon, togekiss, raichu)

for pokemon in Pokemons:
    pokemon.attack()


