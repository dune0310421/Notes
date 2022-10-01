f = open("score.txt", "r", encoding="UTF-8")


def avg():
    grade = 0
    credit = 0
    for s in f:
        t = s.split()
        # if '校公选课' in t:
        #     continue
        # if '体育课' in t:
        #     continue
        # if '2021-2022-1' not in t:
        #     continue
        print(t)
        credit += float(t[5])
        grade += float(t[4]) * float(t[5])

    print("avg", grade / credit)
    print("credit", credit)


def gpa():
    grade = 0
    credit = 0
    gpa = 0
    for s in f:
        t = s.split()
        # if '校公选课' in t:
        #     continue
        # if '体育课' in t:
        #     continue
        # if '2021-2022-1' not in t:
        #     continue
        print(t)
        credit += float(t[5])
        point = 0
        if float(t[4]) >= 90:
            point = 4.0
        elif float(t[4]) >= 85:
            point = 3.7
        elif float(t[4]) >= 82:
            point = 3.3
        elif float(t[4]) >= 78:
            point = 3.0
        elif float(t[4]) >= 75:
            point = 2.7
        elif float(t[4]) >= 72:
            point = 2.3
        elif float(t[4]) >= 68:
            point = 2.0
        elif float(t[4]) >= 64:
            point = 1.5
        elif float(t[4]) >= 60:
            point = 1.0
        grade += float(t[4]) * float(t[5])
        gpa += point * float(t[5])

    print("avg", grade / credit)
    print("gpa", gpa / credit)
    print("credit", credit)


gpa()
f.close()
