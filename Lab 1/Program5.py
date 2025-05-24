""" 
Write a program that asks any number students to enter their final grade and 
enables you to store these grades into a grades.txt plain text file. Then it 
reads the grades from the grades.txt file, and displays the individual grades 
and their count and average.
"""

def write_grades_to_file(filename):
    """Write student grades to a file."""
    with open(filename, 'w') as file:
        while True:
            # ask any number of students to enter their final grade
            grade = input("Enter a student's final grade (or 'done' to finish): ")
            if grade.lower() == 'done':
                break
            if grade.isdigit():
                file.write(grade + '\n') # enables storage into a grades.txt file
            else:
                print("Invalid input. Please enter a numeric grade or 'done'.")

def read_grades_from_file(filename):
    """Read grades from a file and calculate count and average."""
    try: # exception handling syntax
        with open(filename, 'r') as file:
            grades = [int(line.strip()) for line in file.readlines()]
            if grades:
                print("\nGrades from file:")
                for grade in grades:
                    print(grade)
                print(f"\nCount of grades: {len(grades)}")
                # display the individual grades and count their average
                print(f"Average grade: {sum(grades) / len(grades):.2f}")
            else:
                print("The file is empty. No grades to display.")
    except FileNotFoundError: # catches a built-in exception
        print(f"Error: The file '{filename}' does not exist.")

def main():
    """Main function to handle program execution."""
    filename = "grades.txt"
    print("Welcome to the Grades Program!")
    write_grades_to_file(filename)
    read_grades_from_file(filename)

if __name__ == "__main__":
    main()
