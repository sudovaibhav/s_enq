def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    if avg >= 90: return 'S'
    elif avg >= 80: return 'A'
    elif avg >= 65: return 'B'
    elif avg >= 50: return 'C'
    elif avg >= 40: return 'D'
    else: return 'F'

def main():
    print("--- Student Grading System ---")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sem = input("Enter Semester: ")
    
    try:
        m1 = float(input("Enter Marks for Subject 1: "))
        m2 = float(input("Enter Marks for Subject 2: "))
        m3 = float(input("Enter Marks for Subject 3: "))
        
        grade = calculate_grade([m1, m2, m3])
        
        print(f"\n--- Result ---")
        print(f"Student: {name}\nDepartment: {dept}\nSemester: {sem}")
        print(f"Grade: {grade}")
    except ValueError:
        print("Error: Please enter numeric values for marks.")

if __name__ == "__main__":
    main()