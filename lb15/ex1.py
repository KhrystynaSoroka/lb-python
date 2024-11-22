class Progression:
    def __init__(self, n):
        self.n = n
    def sum(self):
        pass
class ArithmeticProgression(Progression):
    def __init__(self, n, a1, d):
        super().__init__(n)
        self.a1 = a1
        self.d = d
    def sum(self):
        an = self.a1 + (self.n - 1) * self.d
        return self.n * (self.a1 + an) / 2
class GeometricProgression(Progression):
    def __init__(self, n, b1, r):
        super().__init__(n)
        self.b1 = b1
        self.r = r
    def sum(self):
        if self.r == 1:
            return self.b1 * self.n  
        return self.b1 * (self.r**self.n - 1) / (self.r - 1)

arithmetic = ArithmeticProgression(5, 2, 3)
print(f"Сума арифметичної прогресії: {arithmetic.sum()}")
geometric = GeometricProgression(4, 2, 3)
print(f"Сума геометричної прогресії: {geometric.sum()}")
