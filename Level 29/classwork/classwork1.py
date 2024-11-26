#2
#i think its 0

def sum(x):
    res = 0
    for i in range(x):
        res+=i
        return res
print(sum(4))

#i was right

#3
#i think that this will output 12
def calc(x, y):
    return [x+y, x*y]

res = calc(3, 4)
print(res[1])

#i was right

 
#5
def text(text1):
    for i in range(len(text1)): 
        print(text1["I am Nick"])
 


#6

def get_grade(num1):
    if num1<0:
        return "negative"
    elif num1>0:
        return "positive"
    elif num1==0:
        return "zero"
    print (get_grade(1))

