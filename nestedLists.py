class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
       # student=[name, score]
        student = Student(name, score)
        students.append(student)
    
    #sorted_students=sorted(students, key=lambda i: (i[1], i[0]))
    sorted_students=sorted(students, key=lambda s: (s.score, s.name))

    
    i=0
    while i<len(sorted_students):
        student=sorted_students[i]
        student_next=sorted_students[i+1]
        #if student[1]!=student_next[1]:
        if student.score != student_next.score:

            i=i+1
            break
        
        
        i+=1
    # i is the index of firt second worst scoring student
    print(sorted_students[i].name)
    i+=1
    while i<len(sorted_students):
        if sorted_students[i].score !=sorted_students[i-1].score:
           break

        print(sorted_students[i].name)

        i+=1