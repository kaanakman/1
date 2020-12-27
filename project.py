import random as rnd
import sys as sys

s_name = "KAAN"
s_surname = "AKMAN"

   
courses = ["Course Names", "1-Course A", "2-Course B", "3-Course C", "4-Course D", "5-Course E"]

def student_login():
    
    login_attempt_count= 3
    
    while login_attempt_count > 0:
        user_name = input("Please enter your name: ").upper()
        user_surname = input ("Please enter your surname: ").upper()
    
        if user_name != s_name or user_surname != s_surname:        
            login_attempt_count -= 1
            print("You have entered a wrong name/surname. Please try again.")
        else:
            
            print("\nWELCOME", user_name)
            
            break
             
    
    else:
        print("Please try again later...")
        sys.exit()

student_login()
  

print("\nAt least three of courses belowing should be taken:\n")
for list in courses:
    print(list)    

  

def course_selection():    
    selection = input('Please, select at least three courses you want to take by entering its number with using "," between them: ').split(",")
    if len(selection) >= 3:
        

        selection_indices = [int(item) for item in selection]


        selected_courses = []
        for index in selection_indices:
            selected_courses.append(courses[index])
        for x in range(len(selected_courses)): 
      
            print(selected_courses[x])
        print("You have completed your selection successfully.")
    else:
         return print("\nYou failed in class. You have to take at least 3 courses"), course_selection()         

    
    while True:
        
        print("\n Select a course for your exams")
       
        exam_selection = int((input("Enter the course number for exam which is written at the beginning of your courses: ")))
        if 0 < exam_selection <= len(selected_courses):
            print("\n",selected_courses[(exam_selection-1)])
            midterm_p = rnd.randint(0,100)
            final_p = rnd.randint(0,100)
            project_p = rnd.randint(0,100)
            exams = {"midterm": midterm_p, "final": final_p, "project": project_p }
            for i,j in exams.items():
                print("\n {}: {}".format(i,j))
            grade = midterm_p * 0.3 + final_p * 0.5 + project_p * 0.2
            if grade > 90:
                 print("\nAA - PASSED")
            elif 70 <= grade < 90:
                 print("\nBB - PASSED")
            elif 50 <= grade < 70:
                 print("\nCC - PASSED")
            elif 30 <= grade < 50:
                 print("\nDD - PASSED")
            elif grade < 30:
                 print("\nFF - Failed")
                 
            sys.exit()       
        
        else:    
            
            print("You have entered a wrong number")   
            
  
course_selection()

