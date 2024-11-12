#1
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
##############################################
numbers.append(100)
numbers.insert(0, 5)
numbers.remove(30)
numbers.reverse()
index50 = numbers.index(50)
count20 = numbers.count(20)



#2
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
###########################################################
print(fruits)
print(fruits[0])
print(fruits[-1])
fruits.append("fig")
fruits.remove("banana")
fruits[1] = "blueberry"