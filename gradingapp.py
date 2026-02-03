def letter_grade(percentage):
    if percentage >= 97:
        return 'A+'
    elif percentage >= 93:
        return 'A'
    elif percentage >= 90:
        return 'A-'
    elif percentage >= 87:
        return 'B+'
    elif percentage >= 83:
        return 'B'
    elif percentage >= 80:
        return 'B-'
    elif percentage >= 77:
        return 'C+'
    elif percentage >= 73:
        return 'C'
    elif percentage >= 70:
        return 'C-'
    elif percentage >= 67:
        return 'D+'
    elif percentage >= 63:
        return 'D'
    elif percentage >= 60:
        return 'D-'
    else:
        return 'F'
    
def average_grade(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def main():
    grades = []
    while True:
        try:
            entry = (input("Enter a grade percentage (or 'q' or 'done' to exit)"))
            if entry.lower() in ('q','done'):
                break
            grade = float(entry)
            grades.append(grade)
            print(f"Letter Grade: {letter_grade(grade)}")
            
        except ValueError:
            print("Invalid input. Please enter a numeric grade percentage or 'q' to quit.")
            
    if grades:
        print(f"Average Grade: {average_grade(grades)}")
    else:
        print("No grades were entered.")

if __name__ == "__main__":
        main()