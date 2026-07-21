class Plant:
    def __init__ (self, name: str, height: int, age: int) -> None: # __init__ initializes & assigns values (non-manually)
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'{self.name}: {self.height}cm, {self.age} days old')


if __name__ == '__main__':
    Rose = Plant('Rose', 25, 30) #created obj, passing values to __init__
    Sunflower = Plant('Sunflower', 80, 45)
    Cactus = Plant('Cactus', 15, 120)
    print('=== Garden Plant Registry ===')
    Rose.show()
    Sunflower.show()
    Cactus.show()


# << OLD CODE >>

# def show(self):
#     print('=== Garden Plant Registry ===')
#     print(f'Rose: {self.height}, {self.age}')
#     print(f'Sunflower: {self.height}, {self.age}')
#     print(f'Cactus: {self.height}, {self.age}') # calls indiv self.info