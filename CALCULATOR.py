print("CALCULATOR")
print("Valid operators include: *, /, +, -,!  and sqrt")
error = "invalid operator"
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
fact = 1
if operator == "*":
    print(num1 * num2)
elif operator == "!":
    for i in range(1, num1 + 1):
        fact = fact * i
    print(fact)
elif operator == "-":
    print(num1 - num2)
elif operator == "+":
    print(num1 + num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "sqrt":
    num = int(input("Enter a number for the square root:\n>>"))
    for i in range(2, num):
        cond = (num % i == 0)
        if cond:
            k = (i * i == num)
            if k:
                print("square root of", num, "==>", i)
                break
    else:
        kd = (num ** 0.5)
        print("square root of", num, "==>", kd)
else:
    print(error)
