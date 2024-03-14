class Fraction:

  def __init__(self, numerator, denominator):

    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):

    return f"{self.numerator}/{self.denominator}"

  def __add__(self, other):

    new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __sub__(self, other):

    new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __mul__(self, other):

    new_numerator = self.numerator * other.numerator
    new_denominator = self.denominator * other.denominator
    return Fraction(new_numerator, new_denominator)

  def __truediv__(self, other):

    new_numerator = self.numerator * other.denominator
    new_denominator = self.denominator * other.numerator
    return Fraction(new_numerator, new_denominator)


fraction1 = Fraction(1, 2)
fraction2 = Fraction(3, 4)

print(f"Дріб 1: {fraction1}")
print(f"Дріб 2: {fraction2}")

sum_fraction = fraction1 + fraction2
difference_fraction = fraction1 - fraction2
product_fraction = fraction1 * fraction2
quotient_fraction = fraction1 / fraction2

print(f"Сума: {sum_fraction}")
print(f"Різниця: {difference_fraction}")
print(f"Добуток: {product_fraction}")
print(f"Частка: {quotient_fraction}")
# Завдання 2
class Stadium:

    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.capacity < other.capacity

    def __add__(self, other):
        return self.capacity + other.capacity


stadium1 = Stadium("Олімпійський", "1966-05-22", "Україна", "Київ", 70050)
stadium2 = Stadium("Сан-Сіро", "1926-09-19", "Італія", "Мілан", 75923)

print(f"Стадіон 1:\n{stadium1}")
print(f"Стадіон 2:\n{stadium2}")

print(f"Стадіони мають однакові назви? {stadium1 == stadium2}")
print(f"Місткість стадіону 1 менша, ніж стадіону 2? {stadium1 < stadium2}")
print(f"Сумарна місткість двох стадіонів: {stadium1 + stadium2}")
# Завдання 3
class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        return f"{self.brand} {self.model} ({self.year}) + {other.brand} {other.model} ({other.year})"

    def start_engine(self):
        print(f"Двигун автомобіля {self.brand} {self.model} {self.year} року випуску запущено!")


car1 = Car("Toyota", "Supra", 2002)
car2 = Car("Nissan", "Skyline", 2003)

print(f"Car 1: {car1}")
print(f"Car 2: {car2}")

print(f"Car 1 == Car 2? {car1 == car2}")
print(f"Car 1 < Car 2? {car1 < car2}")
print(f"Car 1 + Car 2: {car1 + car2}")

car1.start_engine()
# Завдання 4
class Book:

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.title < other.title

    def __add__(self, other):
        return f"{self.title} ({self.author}) + {other.title} ({other.author})"

    def __str__(self):
        return f"{self.title} {self.author} {self.genre}"


book1 = Book("Володар перснів", "Дж. Р. Р. Толкін", "Фентезі")
book2 = Book("Хроніки Нарнії", "К. С. Льюїс", "Фентезі")

print(f"Book 1: {book1}")
print(f"Book 2: {book2}")

print(f"Book 1 == Book 2? {book1 == book2}")
print(f"Book 1 < Book 2? {book1 < book2}")
print(f"Book 1 + Book 2: {book1 + book2}")
