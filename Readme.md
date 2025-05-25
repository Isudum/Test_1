# 📘 Course Record Management System

## 🧠 Objective
This Python project simulates a simple course management system using dictionaries and lists. It allows querying course data by instructor, computing average grades, and filtering courses based on grade thresholds.

## 📂 Project Files

| File Name        | Description |
|----|---|
| `course_info.py` | Contains core logic for course handling |
| `test_course_info.py` | PyTest unit tests for the functions |
| `README.md`      | Project overview and usage instructions |

## 🔧 Functions Implemented

- `get_course_by_instructor(instructor_name)`  
  Returns a list of courses taught by the specified instructor.

- `get_average_grade_of_all_courses()`  
  Computes and returns the average grade across all courses.

- `get_courses_above_grade(threshold)`  
  Returns a list of courses with average grade above a given value.

## 🧪 Test Structure
Unit tests are written using [PyTest](https://docs.pytest.org/).  
The test file `test_course_info.py` contains tests for all three functions.  
To run tests:

```bash
pytest test_course_info.py
```

Thank you
<img src="https://media.tenor.com/Rq4Oy8CarcgAAAAd/thank-you-thank-you-thanks.gif" width="200"/>[^1]

[^1]: [Credits to](https://vamosarema.com/ "vamosarema")


