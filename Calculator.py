import math

class Calculator:
    def __init__(self):
        self.result = None  # Stores the result of operations
        self.history = []  # Keeps a history of calculations

    # Addition of numbers
    def add(self, *n):
        self.result = sum(n)
        self.history.append(f"Added: {n} = {self.result}")
        return self.result

    # Subtraction of numbers
    def subtract(self, *n):
        self.result = n[0] - sum(n[1:])
        self.history.append(f"Subtracted: {n} = {self.result}")
        return self.result

    # Multiplication of numbers
    def multiply(self, *n):
        self.result = 1
        for num in n:
            self.result *= num
        self.history.append(f"Multiplied: {n} = {self.result}")
        return self.result

    # Division of numbers
    def divide(self, *n):
        if 0 in n[1:]:
            raise ZeroDivisionError("Cannot divide by zero.")
        else:
            self.result = n[0]
            for num in n[1:]:
                self.result /= num
            self.history.append(f"Divided: {n} = {self.result}")
            return self.result
        
    # Power (Exponentiation) of numbers
    def power(self, *n):
        self.result = n[0]
        for num in n[1:]:
            self.result **= num
        self.history.append(f"Powered: {n} = {self.result}")
        return self.result
    
    # Square root of a number
    def sqrt(self, n):
        if n < 0:
            raise ValueError("Cannot take square root of a negative number.")
        else:
            self.result = n ** 0.5
            self.history.append(f"Square root: {n} = {self.result}")
            return self.result
        
    # Factorial of a number
    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot take factorial of a negative number.")
        elif n == 0 or n == 1:
            self.result = 1
        else:
            for i in range(1, n + 1):
                self.result *= i
        self.history.append(f"Factorial: {n} = {self.result}")
        return self.result
    
    # Fibonacci sequence for n-th number
    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Cannot compute Fibonacci of a negative number.")
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            a, b = 0, 1
            for _ in range(2, n + 1):
                a, b = b, a + b
            self.result = b
            self.history.append(f"Fibonacci: {n} = {self.result}")
            return self.result
        
    # Greatest Common Divisor (GCD)
    def gcd(self, a, b):
        self.result = math.gcd(a, b)
        self.history.append(f"GCD: {a}, {b} = {self.result}")
        return self.result
    
    # Least Common Multiple (LCM)
    def lcm(self, a, b):
        self.result = abs(a * b) // math.gcd(a, b)
        self.history.append(f"LCM: {a}, {b} = {self.result}")
        return self.result

    # Logarithm with base (default base is 10)
    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("Logarithm is not defined for non-positive numbers.")
        self.result = math.log(a, base)
        self.history.append(f"log_{base}({a}) = {self.result}")
        return self.result

    # Inverse of a number (1/n)
    def inverse(self, n):
        if n == 0:
            raise ZeroDivisionError("Cannot take inverse of zero.")
        self.result = f"{1} / {n}"
        self.history.append(f"Inverse: {n} = {self.result}")
        return self.result

    # Sine of an angle in degrees
    def sin(self, a):
        self.result = math.sin(math.radians(a))
        self.history.append(f"sin({a}°) = {self.result}")
        return self.result

    # Cosine of an angle in degrees
    def cos(self, a):
        self.result = math.cos(math.radians(a))
        self.history.append(f"cos({a}°) = {self.result}")
        return self.result

    # Tangent of an angle in degrees
    def tan(self, a):
        self.result = math.tan(math.radians(a))
        self.history.append(f"tan({a}°) = {self.result}")
        return self.result
    
    # Exponential function (e^a)
    def exp(self, a):
        self.result = math.exp(a)
        self.history.append(f"e^{a} = {self.result}")
        return self.result
    
    # Absolute value of a number
    def abs_value(self, a):
        self.result = abs(a)
        self.history.append(f"abs({a}) = {self.result}")
        return self.result
    
    # Ceiling of a number (rounds up)
    def ceil(self, a):
        self.result = math.ceil(a)
        self.history.append(f"ceil({a}) = {self.result}")
        return self.result

    # Floor of a number (rounds down)
    def floor(self, a):
        self.result = math.floor(a)
        self.history.append(f"floor({a}) = {self.result}")
        return self.result

    # Modf (fractional and integer parts)
    def modf(self, a):
        self.result = math.modf(a)
        self.history.append(f"modf({a}) = {self.result}")
        return self.result

    # Statistical functions

    # Mean (average) of a list of numbers
    def mean(self, numbers):
        if not numbers:
            raise ValueError("List is empty.")
        self.result = sum(numbers) / len(numbers)
        self.history.append(f"Mean of {numbers} = {self.result}")
        return self.result

    # Variance of a list of numbers
    def variance(self, numbers):
        if not numbers:
            raise ValueError("List is empty.")
        mean_value = self.mean(numbers)
        self.result = sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
        self.history.append(f"Variance of {numbers} = {self.result}")
        return self.result

    # Standard deviation of a list of numbers
    def standard_deviation(self, numbers):
        if not numbers:
            raise ValueError("List is empty.")
        variance_value = self.variance(numbers)
        self.result = math.sqrt(variance_value)
        self.history.append(f"Standard deviation of {numbers} = {self.result}")
        return self.result

    # Mathematical constants

    # Pi (π)
    def pi(self):
        self.result = math.pi
        self.history.append("Pi = " + str(self.result))
        return self.result

    # Euler's constant (e)
    def e(self):
        self.result = math.e
        self.history.append("e = " + str(self.result))
        return self.result

    # Phi (Golden ratio)
    def phi(self):
        self.result = (1 + math.sqrt(5)) / 2
        self.history.append("Phi (Golden ratio) = " + str(self.result))
        return self.result

    # Unit conversion functions

    # Celsius to Fahrenheit conversion
    def celsius_to_fahrenheit(self, celsius):
        self.result = (celsius * 9/5) + 32
        self.history.append(f"{celsius}°C = {self.result}°F")
        return self.result

    # Fahrenheit to Celsius conversion
    def fahrenheit_to_celsius(self, fahrenheit):
        self.result = (fahrenheit - 32) * 5/9
        self.history.append(f"{fahrenheit}°F = {self.result}°C")
        return self.result

    # Meters to Kilometers conversion
    def meters_to_kilometers(self, meters):
        self.result = meters / 1000
        self.history.append(f"{meters} meters = {self.result} kilometers")
        return self.result

    # Kilometers to Meters conversion
    def kilometers_to_meters(self, kilometers):
        self.result = kilometers * 1000
        self.history.append(f"{kilometers} kilometers = {self.result} meters")
        return self.result

    # Kilograms to Grams conversion
    def kilograms_to_grams(self, kilograms):
        self.result = kilograms * 1000
        self.history.append(f"{kilograms} kilograms = {self.result} grams")
        return self.result

    # Grams to Kilograms conversion
    def grams_to_kilograms(self, grams):
        self.result = grams / 1000
        self.history.append(f"{grams} grams = {self.result} kilograms")
        return self.result

    # Pounds to Kilograms conversion
    def pounds_to_kg(self, pounds):
        self.result = pounds * 0.453592
        self.history.append(f"{pounds} pounds = {self.result} kg")
        return self.result

    # Kilograms to Pounds conversion
    def kg_to_pounds(self, kg):
        self.result = kg / 0.453592
        self.history.append(f"{kg} kg = {self.result} pounds")
        return self.result

    # Inches to Centimeters conversion
    def inches_to_cm(self, inches):
        self.result = inches * 2.54
        self.history.append(f"{inches} inches = {self.result} cm")
        return self.result

    # Centimeters to Inches conversion
    def cm_to_inches(self, cm):
        self.result = cm / 2.54
        self.history.append(f"{cm} cm = {self.result} inches")
        return self.result

    # Display the result of the last operation
    def display_result(self):
        return self.result

    # Display the operation history
    def display_history(self):
        return self.history

    def main():
        # Create an instance of the Calculator
        calc = Calculator()

        print("Welcome to the Calculator!")
        print("You can perform the following operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Factorial")
        print("8. Fibonacci")
        print("9. GCD")
        print("10. LCM")
        print("11. Logarithm")
        print("12. Inverse")
        print("13. Sin")
        print("14. Cos")
        print("15. Tan")
        print("16. e^x")
        print("17. Absolute Value")
        print("18. Ceil")
        print("19. Floor")
        print("20. Modf")
        print("21. Mean")
        print("22. Variance")
        print("23. Standard Deviation")
        print("24. Pi (π)")
        print("25. Euler's Number (e)")
        print("26. Golden Ratio (Phi)")
        print("27. Convert Celsius to Fahrenheit")
        print("28. Convert Fahrenheit to Celsius")
        print("29. Convert Meters to Kilometers")
        print("30. Convert Kilometers to Meters")
        print("31. Convert Kilograms to Grams")
        print("32. Convert Grams to Kilograms")
        print("33. Convert Pounds to Kilograms")
        print("34. Convert Kilograms to Pounds")

        while True:
            # Get user choice for operation
            operation = input("\nEnter the number of the operation you want to perform (or type 'exit' to quit): ")

            if operation.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            
            if operation == '1':  # Addition
                nums = input("Enter numbers separated by spaces: ").split()
                nums = [float(num) for num in nums]
                print("Result: ", calc.add(*nums))

            elif operation == '2':  # Subtraction
                nums = input("Enter numbers separated by spaces: ").split()
                nums = [float(num) for num in nums]
                print("Result: ", calc.subtract(*nums))

            elif operation == '3':  # Multiplication
                nums = input("Enter numbers separated by spaces: ").split()
                nums = [float(num) for num in nums]
                print("Result: ", calc.multiply(*nums))

            elif operation == '4':  # Division
                nums = input("Enter numbers separated by spaces: ").split()
                nums = [float(num) for num in nums]
                print("Result: ", calc.divide(*nums))

            elif operation == '5':  # Power
                nums = input("Enter numbers separated by spaces: ").split()
                nums = [float(num) for num in nums]
                print("Result: ", calc.power(*nums))

            elif operation == '6':  # Square Root
                num = float(input("Enter a number: "))
                print("Result: ", calc.sqrt(num))

            elif operation == '7':  # Factorial
                num = int(input("Enter a number: "))
                print("Result: ", calc.factorial(num))

            elif operation == '8':  # Fibonacci
                num = int(input("Enter a number: "))
                print("Result: ", calc.fibonacci(num))

            elif operation == '9':  # GCD
                a, b = map(int, input("Enter two numbers separated by a space: ").split())
                print("Result: ", calc.gcd(a, b))

            elif operation == '10':  # LCM
                a, b = map(int, input("Enter two numbers separated by a space: ").split())
                print("Result: ", calc.lcm(a, b))

            elif operation == '11':  # Logarithm
                a = float(input("Enter a number: "))
                base = float(input("Enter the base (default is 10): ") or 10)
                print("Result: ", calc.log(a, base))

            elif operation == '12':  # Inverse
                num = float(input("Enter a number: "))
                print("Result: ", calc.inverse(num))

            elif operation == '13':  # Sin
                angle = float(input("Enter an angle in degrees: "))
                print("Result: ", calc.sin(angle))

            elif operation == '14':  # Cos
                angle = float(input("Enter an angle in degrees: "))
                print("Result: ", calc.cos(angle))

            elif operation == '15':  # Tan
                angle = float(input("Enter an angle in degrees: "))
                print("Result: ", calc.tan(angle))

            elif operation == '16':  # e^x
                num = float(input("Enter a number: "))
                print("Result: ", calc.exp(num))

            elif operation == '17':  # Absolute Value
                num = float(input("Enter a number: "))
                print("Result: ", calc.abs_value(num))

            elif operation == '18':  # Ceil
                num = float(input("Enter a number: "))
                print("Result: ", calc.ceil(num))

            elif operation == '19':  # Floor
                num = float(input("Enter a number: "))
                print("Result: ", calc.floor(num))

            elif operation == '20':  # Modf
                num = float(input("Enter a number: "))
                print("Result: ", calc.modf(num))

            elif operation == '21':  # Mean
                numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Result: ", calc.mean(numbers))

            elif operation == '22':  # Variance
                numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Result: ", calc.variance(numbers))

            elif operation == '23':  # Standard Deviation
                numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
                print("Result: ", calc.standard_deviation(numbers))

            elif operation == '24':  # Pi
                print("Result: ", calc.pi())

            elif operation == '25':  # Euler's Number
                print("Result: ", calc.e())

            elif operation == '26':  # Golden Ratio
                print("Result: ", calc.phi())

            elif operation == '27':  # Celsius to Fahrenheit
                celsius = float(input("Enter temperature in Celsius: "))
                print("Result: ", calc.celsius_to_fahrenheit(celsius))

            elif operation == '28':  # Fahrenheit to Celsius
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                print("Result: ", calc.fahrenheit_to_celsius(fahrenheit))

            elif operation == '29':  # Meters to Kilometers
                meters = float(input("Enter distance in meters: "))
                print("Result: ", calc.meters_to_kilometers(meters))

            elif operation == '30':  # Kilometers to Meters
                kilometers = float(input("Enter distance in kilometers: "))
                print("Result: ", calc.kilometers_to_meters(kilometers))

            elif operation == '31':  # Kilograms to Grams
                kilograms = float(input("Enter weight in kilograms: "))
                print("Result: ", calc.kilograms_to_grams(kilograms))

            elif operation == '32':  # Grams to Kilograms
                grams = float(input("Enter weight in grams: "))
                print("Result: ", calc.grams_to_kilograms(grams))

            elif operation == '33':  # Pounds to Kilograms
                pounds = float(input("Enter weight in pounds: "))
                print("Result: ", calc.pounds_to_kg(pounds))

            elif operation == '34':  # Kilograms to Pounds
                kg = float(input("Enter weight in kilograms: "))
                print("Result: ", calc.kg_to_pounds(kg))

            else:
                print("Invalid operation, please try again.")

print(Calculator.main())
