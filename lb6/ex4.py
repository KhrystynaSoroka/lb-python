
users = ["Mark", "Tom", "Bob", "Alice", "Tom", "Bill", "Tom", "Alex", "Shaun", "Mark"]

count_tom = users.count("Tom")
count_mark = users.count("Mark")
count_alice = users.count("Alice")
count_john = users.count("John")

print(f"Tom зустрічається {count_tom} разів")
print(f"Mark зустрічається {count_mark} разів")
print(f"Alice зустрічається {count_alice} разів")
print(f"John зустрічається {count_john} разів")

users.pop(2)
while "Tom" in users:
    users.remove("Tom")

print("Список після вилучення елементів:", users)
