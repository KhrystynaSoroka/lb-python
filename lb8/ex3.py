flights = []
n = int(input("Введіть кількість авіарейсів для додавання: "))

for i in range(n):
    print(f"\nВведіть інформацію про рейс {i + 1}:")
    flight = {}
    flight['flight_number'] = int(input("  Введіть номер рейсу (додатне ціле число): "))
    flight['plane_name'] = input("  Введіть назву літака: ")
    flight['destination'] = input("  Введіть місце призначення: ")
    flight['total_seats'] = int(input("  Введіть кількість місць для пасажирів (шт., додатне ціле число): "))
    flight['tickets_sold'] = int(input("  Введіть кількість проданих квитків (шт., додатне ціле число): "))
    baggage = {}
    baggage['type'] = input("  Введіть тип багажу: ")
    baggage['total_weight'] = float(input("  Введіть загальну вагу багажу (в кг., додатне дійсне число): "))
    baggage['estimated_value'] = int(input("  Введіть оціночну вартість багажу (в грн., додатне ціле число): "))
    flight['baggage'] = baggage
    flights.append(flight)

print("\nІнформація про всі авіарейси:")
for i, flight in enumerate(flights, start=1):
    print(f"\nРейс {i}:")
    print(f"  Номер рейсу: {flight['flight_number']}")
    print(f"  Назва літака: {flight['plane_name']}")
    print(f"  Місце призначення: {flight['destination']}")
    print(f"  Кількість місць для пасажирів: {flight['total_seats']}")
    print(f"  Кількість проданих квитків: {flight['tickets_sold']}")
    print("  Інформація про багаж:")
    print(f"    Тип багажу: {flight['baggage']['type']}")
    print(f"    Загальна вага багажу: {flight['baggage']['total_weight']} кг")
    print(f"    Оціночна вартість багажу: {flight['baggage']['estimated_value']} грн")
