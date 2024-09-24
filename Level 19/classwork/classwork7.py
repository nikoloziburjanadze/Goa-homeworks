#7
def odd_or_even(number):
    if number % 2 == 0:
        return str(number) + " is even"
    else:
        return str(number) + " is odd"
    
print(odd_or_even(4))
