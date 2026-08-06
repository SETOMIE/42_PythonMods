class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.age = age

    def growth(self, cm: float) -> None:
        self.height += cm

    def age_by(self, days: int) -> None:
        self.age += days

    def show(self) -> None:
        print(f'{self.name}: {round(self.height, 1)}cm, {self.age} days old')


if __name__ == '__main__':
    plant1 = Plant("Rose", 25, 29)
    print("=== Garden Plant Growth ===")
    start_height: float = plant1.height
    plant1.show()
    for day in range(1, 8):
        print(f"=== Day {day} ====")
        plant1.growth(0.8)
        plant1.age_by(1)
        plant1.show()
    total_growth: float = round(plant1.height - start_height, 2)
    print(f"Growth this week: {total_growth}cm")
