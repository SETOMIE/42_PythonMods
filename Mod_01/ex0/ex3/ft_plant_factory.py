class Plant:
    def __init__ (self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'Created: {self.name}: {self.height}cm, {self.age} days old')

if __name__ == '__main__':
    Rose = Plant('Rose', '25.0', '30')
    Oak = Plant('Oak', '200.0', '365')
    Cactus = Plant('Cactus', '5.0', '90')
    Sunflower = Plant('Sunflower', '80.0', '45')
    Fern = Plant('Fern', '15.0', '120')
    print('=== Plant Factory Output ===')
    Rose.show()
    Oak.show()
    Cactus.show()
    Sunflower.show()
    Fern.show()