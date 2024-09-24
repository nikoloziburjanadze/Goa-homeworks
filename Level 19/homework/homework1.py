def simple_calculator(num1, num2, sign):
    if sign == "%" and num2 == 0:
        return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
    elif sign == "%":
        return num1 / num1
    elif sign == "+":
        return num1 + num2
    elif sign == "x":
        return num1 * num2
    elif sign == "-":
        return num1- num2

print(simple_calculator(5, 7, "+"))





