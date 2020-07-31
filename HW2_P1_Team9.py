
#Assign grades to classify
A_score = 90
B_score = 80
C_score = 70
D_score = 60


#Calculate the grade

def calculate_grade(score):
        if score >= A_score:
            print("Your grade is A")
        elif score >= B_score:
            print("Your grade is B")
        elif score >= C_score:
            print("Your grade is C")
        elif score >= D_score:
            print("Your grade is D")
        else:
            print("Your grade is F")
        return score   

#Validate the score input (main function) and print error message if input is invalid
def validate_input():
    try:
        score = int(input("Enter a score from 0 to 100: "))
    except:
        print("Enter numbers only")
    else:
        if 0 <= score <= 100:
            pass #ignore else statement if acceptable value
            print(calculate_grade(score))
        else:
            print("Enter a score between 0 and 100")
    
validate_input()
