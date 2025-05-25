import numpy as np

courses = [
    {"name": "Mathematics", "instructor": "Dr. Tan", "students": 30, "average_grade": 85},
    {"name": "Physics", "instructor": "Dr. Lim", "students": 25, "average_grade": 78},
    {"name": "Programming", "instructor": "Ms. Lee", "students": 40, "average_grade": 90}
]

teachers = {
    "1": "Dr. Tan",
    "2": "Dr. Lim",
    "3": "Ms. Lee"
}

def get_course_by_instructor(name):
    result = []

    for item in courses:
        if item["instructor"] == name :
            result.append(item)

    return result


    
def get_average_grade_of_all_courses():
    
    total_grade = 0

    for item in courses: 
        total_grade += item["average_grade"]
        average = np.mean(total_grade)
        average = round(average, 2)

        return average


def get_courses_above_grade(threshold):
    result = []
    for item in courses:
        if item["average_grade"] > threshold:
            result.append(item)
    return result  # return should be outside the loop

def display_records(number):
    print(("Name" + "\t" +"Instructor" +"\t" +"students" +"\t" +"Average_Grade" ).expandtabs(15))
    for item in number:
        print((item["name"] + "\t" + item["instructor"] + "\t" + str(item["students"]) + "\t" + str(item["average_grade"])).expandtabs(15))
        
def reapeat_main():
    print("Welcome to the Course Management System")
    print("1. Get courses by instructor")
    print("1 for Dr. Lim, 2 for Dr. Tan, 3 for Ms. Lee")
    instructor_name = float(input("Please select instructor : "))
    teacher_choice = teachers.get(str(instructor_name), "Dr. Lim")
    display_records(get_course_by_instructor(teacher_choice))
    print("2. Average grade of all courses =", get_average_grade_of_all_courses() )
    print("3. Get courses above a certain grade")
    threshold = float(input("Please enter the grade threshold: "))
    Number = get_courses_above_grade(threshold)
    display_records(Number)


def main():
    while True:
        reapeat_main()
        choice = input("Do you want to continue? (yes/no): ")
        if choice != 'yes':
            print("Exiting the Course Management System. Goodbye!")
            quit()


if __name__ == "__main__":
    main()