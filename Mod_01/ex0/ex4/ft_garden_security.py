class Plant:
    def __init__ (self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f'Created: {self.name}: {self.height}cm, {self.age} days old')

if __name__ == '__main__':
    Rose = Plant('Rose', '25.0', '30')
    print('=== Garden Security System ===')
    Rose.show()

# System must protect and encapsulate sensitive data