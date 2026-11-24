#STUDENT GRADE MANAGEMENT SYSTEM

marks = []                                                        #empty list
while len(marks) < 5:                                             # for 5 marks
    m = int(input("Enter marks : "))                              # to take marks from user
    if m >= 0 and m <= 100:
        marks.append(m)                                           # to add into list
    else:                                                         # if mark is not betwn 0 and 100
        print("Invalid marks,enter valid mark,btwn 0 and 100")
        while m >= 0 and m <= 100:                                # till the user give mark btwn 0 and 100,ask for mark as input
            m = int(input("Enter marks: "))
            marks.append(m)
print("MARKS OF 5 SUBJECTS=",marks)


#CALCULATE AVARAGE
def calculate_average(marks):
    sum=0
    for i in range (len(marks)):
        sum=sum+marks[i]                # calculating sum of marks
        avarage=sum/len(marks)          # calculating avarage of marks
    return avarage
avarage=(calculate_average(marks))
print("AVARAGE MARK=",avarage)


# FINAL GRADE
def get_grade(avarage):
    if avarage >= 90:
        return "A"
    elif avarage >= 80 and avarage < 90:
        return"B"
    elif avarage >= 70 and avarage < 80:
        return"C"
    elif avarage >= 60 and avarage < 70:
        return"D"
    else:
        return"F"
grade=get_grade(avarage)
print("GRADE MARK=",grade)






