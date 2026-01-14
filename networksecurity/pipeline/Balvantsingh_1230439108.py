# Q1. Salary Increment Logic
salary = float(input("Enter salary: "))

if salary < 30000:
    salary += salary * 0.20
elif 30000 <= salary <= 60000:
    salary += salary * 0.10
else:
    salary = salary

print("New Salary:", salary)



# Q2. Multiple Conditions Check
num = int(input("Enter number: "))

if num % 3 == 0 and num % 4 == 0:
    print("Divisible by both 3 and 4")
elif num % 3 == 0 or num % 4 == 0:
    print("Divisible by only one of them")
else:
    print("Divisible by none")



# Q3. Bill Discount Calculator
bill = float(input("Enter bill amount: "))
payment = input("Payment mode: ")
premium = input("Premium member (yes/no): ")

if bill > 5000 and payment == "card":
    bill -= bill * 0.15
elif bill > 5000 or premium == "yes":
    bill -= bill * 0.10

print("Final Bill:", bill)



# Q4. Even–Odd and Range Check
num = int(input("Enter number: "))

if num % 2 == 0 and 50 <= num <= 100:
    print("Even and between 50–100")
elif num % 2 != 0 and num > 100:
    print("Odd and greater than 100")
else:
    print("Invalid Category")



# Q5. Assignment Operator Tracker
x = int(input("Enter x: "))

x += 10
x *= 2
x -= 5

print("Final Value:", x)



# Q6. Comparison Chain
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a < b < c:
    print("Increasing Order")
else:
    print("Not Increasing")



# Q7. Login Attempt Validator
username = input("Username: ")
password = input("Password: ")
attempts = int(input("Login attempts: "))

if username == "admin" and len(password) >= 6 and attempts < 3:
    print("Login Allowed")
else:
    print("Login Denied")



# Q8. Mathematical Expression Evaluation
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = (a + b) ** 2 > a**2 + b**2 + c
print(result)



# Q9. Divisibility Priority
num = int(input("Enter number: "))

if num % 2 == 0 and num % 5 == 0:
    print("Divisible by 2 and 5")
elif num % 2 == 0:
    print("Divisible by only 2")
elif num % 5 == 0:
    print("Divisible by only 5")
else:
    print("Not divisible by 2 or 5")



# Q10. Income Tax Slab
income = float(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.10
else:
    tax = income * 0.20

print("Tax:", tax)
print("Net Income:", income - tax)



# Q11. Student Grading System
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
    print("Excellent")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")


# Q12. Electricity Bill Calculation
units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
else:
    bill = 100 * 5 + 100 * 7 + (units - 200) * 10

print("Electricity Bill:", bill)



# Q13. ATM Withdrawal System
balance = float(input("Enter balance: "))
amount = int(input("Enter withdrawal amount: "))

if amount % 100 != 0:
    print("Amount must be multiple of 100")
elif amount > balance:
    print("Insufficient balance")
elif balance - amount < 500:
    print("Minimum balance of 500 required")
else:
    print("Withdrawal Successful")



# Q14. Day Type Checker (match-case)
day = int(input("Enter day number: "))

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")



# Q15. Menu-Driven Calculator
a = float(input("Enter a: "))
b = float(input("Enter b: "))
choice = int(input("1.Add 2.Sub 3.Mul 4.Div: "))

match choice:
    case 1:
        print(a + b)
    case 2:
        print(a - b)
    case 3:
        print(a * b)
    case 4:
        print(a / b)
    case _:
        print("Invalid choice")



# Q16. Insurance Eligibility
age = int(input("Age: "))
salary = int(input("Salary: "))
medical = input("Medical history (clear/not): ")

if age >= 25:
    if salary >= 40000:
        if medical == "clear":
            print("Eligible")
        else:
            print("Not Eligible")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")



# Q17. Traffic Signal Simulator
color = input("Enter signal color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Ready")
elif color == "green":
    print("Go")
else:
    print("Invalid")



# Q18. Triangle Type Checker
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Not a valid triangle")



# Q19. Exam Attempt Rules
result = input("Result (pass/fail): ")
attempts = int(input("Attempts: "))

if result == "fail" and attempts <= 3:
    print("Re-attempt allowed")
else:
    print("No more attempts")



# Q20. Password Strength Checker
password = input("Enter password: ")

has_digit = any(char.isdigit() for char in password)
has_upper = any(char.isupper() for char in password)

if len(password) >= 8 and has_digit and has_upper:
    print("Strong")
else:
    print("Weak")