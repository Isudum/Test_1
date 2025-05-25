import Sample1 as sample


def test_get_course_by_instructor():
    result = sample.get_course_by_instructor("Dr. Lim")
    expected = [{"name": "Physics", "instructor": "Dr. Lim", "students": 25, "average_grade": 78}]
    assert (result == expected)

def test_get_average_grade_of_all_courses():
    result = sample.get_average_grade_of_all_courses()
    expected = 85.0
    assert (result == expected)

def test_get_courses_above_grade():
    result = sample.get_courses_above_grade(80)
    expected = [
        {"name": "Mathematics", "instructor": "Dr. Tan", "students": 30, "average_grade": 85},
        {"name": "Programming", "instructor": "Ms. Lee", "students": 40, "average_grade": 90}
    ]
    assert (result == expected)