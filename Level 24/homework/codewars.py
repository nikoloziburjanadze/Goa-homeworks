#1
def count_by(x, n):
    return [x * i for i in range(1, n + 1)]

#2
def find_average(nums):
    return sum(nums) / len(nums)

#3
def get_grade(s1, s2, s3):
    if s1<=90 and s2 <=90 and s3 <=90:
        return "A"
    elif s1<=80 and s2 <=80 and s3 <=80:
        return "B"
    elif s1<=70 and s2 <=70 and s3 <=70:
        return "C"
    elif s1<=60 and s2 <=60 and s3 <=60:
        return "D"
    elif s1<=0 and s2 <=0 and s3 <=0:
        return "F"

#4
def paperwork(n, m):
    if n>0 and m>0:
        return n*m 
    elif n==0 or m==0:
        return 0
    elif n<0:
        return 0
    elif m<0:
        return 0