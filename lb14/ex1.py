class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def pod(self):
        if self.salary <= 1100:
            return 0
        elif 1100 < self.salary <= 4000:
            return self.salary * 0.1
        else:
            return self.salary * 0.2
worker1 = Worker("Жабченко", 15000)
print(f"Податок для {worker1.name}: {worker1.pod()} грн.")