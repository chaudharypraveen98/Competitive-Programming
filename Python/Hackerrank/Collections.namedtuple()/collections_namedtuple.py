from collections import namedtuple
n, Student = int(input()), namedtuple('Student', input())
# unpacking *input().split()
marks = [int(Student(*input().split()).MARKS) for _ in range(n)]
print("%.2f" % (sum(marks)/len(marks)))
