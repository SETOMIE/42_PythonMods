class Plant:
    def __init__ (self, name: str, height: float, age: int) -> None: # __init__ initializes & assigns values (non-manually)
        self.name = name.capitalize()
        self.height = height
        self.age = age
    
    #INSTANCE METHOD
    def growth(self) -> float:
          while (self.height) < 30.6:
            self.height += 0.8

    def age(self) -> int:
        {self.age} = range(30, 38)

    def show(self):
        print('=== Garden Plant Growth ===')
        print(f'{self.name}: {self.height}cm, {self.day} days old')

if __name__ == '__main__':
    Rose = Plant('Rose', '25.0', '30')
    print('=== Day {self.day} ===')
    Rose.show()

        # OLD CODE

    # def grow(self) -> float:
        # while (self.height) < 30.6
        #     self.height += 0.8
    #         break
        
    # def age(self) -> int:
    #     while (self.day) < 37:
    #         self.day += 1
    #         break