class Plant:
    def __init__ (self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        if self.age == 1:
            print(f'Created: {self.name}: {float(self.height)}cm,'
                  f' {self.age} day old')
        elif self.age > 1:
            print(f'Created: {self.name}: {float(self.height)}cm,'
                  f' {self.age} days old')
        else:
            print("Error, plant does not exist!")


if __name__ == '__main__':
    plants: list = [Plant('Rose', 25.0, 30),
                    Plant('Oak', 200.0, 365),
                    Plant('Cactus', 5.0, 90),
                    Plant('Sunflower', 80.0, 45),
                    Plant('Fern', 15.0, 120)]
    print('=== Plant Factory Output ===')
    count: int = 0
    for Plant in plants:
        Plant.show()


# def show(self) -> None:
#         print(f'Created: {self.name}: {self.height}cm, {self.age} days old')
