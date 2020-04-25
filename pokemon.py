class PockMon:
    sound = ""
    def __init__(self,name=None,level=1):
        self._name = name
        self._level = level
    
        if len(self._name) == 0:
            raise ValueError("name cannot be empty")
            
        if self._level < 0:
            raise ValueError("level should be > 0")
            
    def __str__(self):
        return f"{self.name} - value {self.level}"

            
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @property
    def name(self):
        return self._name
        
    @property
    def level(self):
        return self._level
        

class running:
    by_run = ""
    @classmethod
    def run(cls):
        print(f"{cls.by_run} running...")
    

class swimming:
    by_swim = ""
    @classmethod
    def swim(cls):
        print(f"{cls.by_swim} swimming...")
        
        
class flying:
    by_fly = ""
    @classmethod
    def fly(cls):
        print(f"{cls.by_fly} flying...")


class Pikachu(PockMon,running):
    sound = "Pika Pika"
    by_run = "Pikachu"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        
    
class Squirtle(PockMon,running,swimming):
    sound = "Squirtle...Squirtle"
    by_run = "Squirtle"
    by_swim = "Squirtle"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        
        
class Pidgey(PockMon,flying):
    sound = "Pidgey...Pidgey"
    by_fly = "Pidgey"
    
    
    def attack(self):
        print(f"Air attack with {self.level*5} damage")
    
    
class Swanna(PockMon,flying,swimming):
    sound = "Swanna...Swanna"
    by_fly = "Swanna"
    by_swim = "Swanna"
    
    
    def attack(self):
        print(f"Water attack with {self.level*9} damage")
        print(f"Air attack with {self.level*5} damage")
   
    
class Zapdos(PockMon,flying):
    sound = "Zap...Zap"
    by_fly = "Zapdos"
    
    def attack(self):
        print(f"Electric attack with {self.level*10} damage")
        print(f"Air attack with {self.level*5} damage")
   


class Island:
    def __init__(self,name=None, max_no_of_pokemon=0, total_food_available_in_kgs=0):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0
        
    @property    
    def name(self):
        return self._name
        
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f"{self._name} - 0 pokemon - {self._total_food_available_in_kgs} food"

        
    def add_pokemon(self,num):
        if self._pokemon_left_to_catch + num >= self._max_no_of_pokemon:
            print("Island at its max pokemon capacity")
            
        else:
            self._pokemon_left_to_catch += num
    
    
    
    
