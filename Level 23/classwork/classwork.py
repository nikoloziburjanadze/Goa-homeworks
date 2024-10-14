
#1

def simple_calculator(num1, num2, sign):
    
    if sign == "%" and num2 == 0:
        return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
    elif sign == "+":
        return num1 + num2
    elif sign == "%":
        return num1 / num1
    elif sign == "-":
        return num1- num2   
    elif sign == "x":
        return num1 * num2
   
print(simple_calculator(0.5, 7, "+"))

#2


#3
list1 = [34,56,78,50]
print(list1[3])


#4
list2 = [34,56,78,50,90]
print(list2[0]+list2[1]+list2[2]+list2[3]+list2[4])
print(list2[0]*list2[1]*list2[2]*list2[3]*list2[4])
