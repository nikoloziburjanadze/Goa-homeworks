def get_grade(s1, s2, s3):
    if s1<=90 and s2 <=90 and s3 <=90:
        return "A"
    elif s1<=80 and s2 <=80 and s3 <=80:
        return "B"
    elif s1<=70 and s2 <=70 and s3 <=70:
        return "C"
    elif s1<=60 and s2 <=60 and s3 <=60:
        return "D"
    elif s1>=0 and s2 >=0 and s3 >=0:
        return "F"