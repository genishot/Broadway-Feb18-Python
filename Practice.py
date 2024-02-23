a = int(input("First Number "))
b = int(input("Second Number "))
x = f'The sum of {a} and {b} is {a+b}'
print(x)

e = int(input("Enter your birthdate "))
f = 2024
y = f'You are {f-e} years old'
print(y)

#Stock Market Doubles Every Years
Investment = int(input("How much are you planning to invest "))
Year = int(input("Which years investment results would you like to see "))
Timeline = Year-2024
Compound = Power(Investment,Timeline)
print(Compound)