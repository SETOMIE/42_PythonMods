class Plant:
    def __init__ (self, name: str, height: float, age: int) -> None: # __init__ initializes & assigns values (non-manually)
        self.name = name.capitalize()
        self.height = height
        self.age = age
    
    def growth(self, cm: float) -> None:
        self.height += cm
            #   while (self.height) < 30.6:
            #     self.height += 0.8

    def age_by(self, days: int) -> None:
        self.age += days
            # {self.age} = range(30, 38) << OLD >>

    def show(self) -> str:
        print(f'{self.name}: {round(self.height, 1)}cm, {self.age} days old')


if __name__ == '__main__':
    plant1 = Plant("Rose", 24.2, 29)
    start_height: float = plant1.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 8):
        print(f"=== Day {day} ====")
        plant1.growth(0.8)
        plant1.age_by(1)
        print(plant1.show())
    total_growth: int = round(plant1.height - start_height)
    print(f"Growth this week: {total_growth}cm")

    # Plant1 = Plant('Rose', '25.0', '30') -1 and 0.8 from each because of rounding off and addition


# << OLD CODE >>

    # def grow(self) -> float:
        # while (self.height) < 30.6
        #     self.height += 0.8
    #         break
        
    # def age(self) -> int:
    #     while (self.day) < 37:
    #         self.day += 1
    #         break
    