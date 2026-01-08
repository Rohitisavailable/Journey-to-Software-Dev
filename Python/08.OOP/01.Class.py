"""
This module defines a simple Pokemon class for demonstration purposes.
It includes basic attributes and methods for a Pokemon character.
"""

class Pokemon:
    """
    A class representing a Pokemon with basic attributes and actions.
    
    Attributes:
        name (str): The name of the Pokemon.
        armor (int): The armor value of the Pokemon.
        hit_point (int): The hit points of the Pokemon.
    """
    
    def __init__(self, name: str, max_armor: int, max_hit: int):
        """
        Initialize a new Pokemon instance.
        
        Args:
            name (str): The name of the Pokemon.
            max_armor (int): The maximum armor value.
            max_hit (int): The maximum hit points.
        """
        self.name = name  # Set the Pokemon's name
        self.armor = max_armor  # Set the armor to the maximum value
        self.hit_point = max_hit  # Set the hit points to the maximum value
        #self. is used to refer to the instance itself
        self._is_charging = False

    def attack(self):
        #def attack(self):  # Define the attack method
        """
        Simulate the Pokemon performing an attack.
        
        Prints a message indicating the Pokemon is attacking.
        """
        print(f"{self.name} attack")  # Print an attack message with the Pokemon's name
    
    def _change_attack(self):
        print(f"{self.name} is charging")

    def defend(self):
        #def defend(self):  # Define the defend method
        """
        Simulate the Pokemon defending itself.
        
        Prints a message indicating the Pokemon is defending.
        """
        print(f"{self.name} defend itself")  # Print a defense message with the Pokemon's name




    def display_name(self):
        print(f"my name is {self.name} ")  # Print the Pokemon's name



    def get_name(self):
        print(f"Whats your name ?")
        input_name = input()
        print(f"Hello {input_name} ! nice to meet you")

    def sleep(self):
        print(f"ZZZzzzzZZZzz {self.name} is now going to sleepzzZzZzZzZ")






    # Create a Pokemon instance named Pikachu with armor 100 and hit points 1000
pikachu = Pokemon("pikachu", 100, 1000)
    #pikachu is an object of the Pokemon class, which has its own attributes and methods, which can be accessed using the dot notation.
    #For example, pikachu.name will return "pikachu", and pikachu.attack() will call the attack method.




pikachu.attack()  # Call the attack method
pikachu.defend()  # Call the defend method
pikachu.display_name()    # Call the display_name method
pikachu.get_name()  # Call the get_name method
pikachu.sleep() # Call the sleep method
pikachu._change_attack



snorlax = Pokemon("Snorlax", 150, 5000)

snorlax.attack()
snorlax.defend()
snorlax.display_name()
snorlax.get_name()
snorlax.sleep()


charmander = Pokemon("Charmander", 400, 50000)