#   a117_grades.py
#   This code is incomplete.
my_courses = ["English", "Math", "CS"]

check_grades = True
while (check_grades):
#first block
    print() # blank line
#third block
    for course in my_courses:
        print("Enter your points for " + course)
        a = int(input("Points -> "))

#fourth block
        if (a >= 90):
	        print("A")
        elif (a >= 80):
	        print("B")
        elif (a >= 70):
	        print("C")
        elif (a >= 60):
	        print("D")
        else:
	        print("F")        
#second block
    redo = input("Do you need to re-do these grades? (y/n)")
    if (redo == "y"):
	    check_grades = True
    else:
	    check_grades = False