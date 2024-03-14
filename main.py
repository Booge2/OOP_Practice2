class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real, self.imag * other.imag)

    def __truediv__(self, other):
        return ComplexNumber(self.real / other.real, self.imag / other.imag)

    def __floordiv__(self, other):
        return ComplexNumber(self.real // other.real, self.imag // other.imag)

    def __mod__(self, other):
        return ComplexNumber(self.real % other.real, self.imag % other.imag)

    def __gt__(self, other):
        return ComplexNumber(self.real > other.real, self.imag > other.imag)

    def __lt__(self, other):
        return ComplexNumber(self.real < other.real, self.imag < other.imag)

    def __eq__(self, other):
        return ComplexNumber(self.real == other.real, self.imag == other.imag)


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)

print(f"Num 1 + Num 2: {num1 + num2}")
print(f"Num 1 - Num 2: {num1 - num2}")
print(f"Num 1 * Num 2: {num1 * num2}")
print(f"Num 1 / Num 2: {num1 / num2}")
print(f"Num 1 // Num 2: {num1 // num2}")
print(f"Num 1 % Num 2: {num1 % num2}")

print(f"Перше число більше другого? {num1 > num2}")
print(f"Перше число менше другого? {num1 < num2}")
print(f"Числа рівні? {num1 == num2}")
