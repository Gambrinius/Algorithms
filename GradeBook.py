# -*- coding: utf-8 -*-

__author__ = "Ilya Konon"
__email__ = "ilya.konon.95@gmail.com"

"""
Create Class Gradebook, keeps a list of students, with names and surnames.
Each student has information on subjects that he passed.
This information is two estimates: a ranking of the semester examination.

Gradebook class must contain at least the following methods:
1) get_best_exam_student - receives subject parameter, returns the student with the highest test scores obtained by the subject subject.
2) get_passed_exams - returns all the items on which students take exams.
3) print_result_grades - outputs to the console all the students names with the names of objects, which they passed.
Opposite each item to display an overall assessment on the subject for this student, that rating * = 0.3 + 0.7 * examination,
rounded to the nearest integer. As a result, the output should be as follows:

Student1
  subject1 - result_grade_for_subj1
  subject2 - result_grade_for_subj2
Student2
  subject1 - result_grade_for_subj1
  subject10 - result_grade_for_subj10
etc.
"""


class Student:
    """
    Class describes Student objects
    """
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Subject:
    """
    Class describes Subject objects
    """
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.subject_students = {}

    def get_students(self):
        """
        return sorted students list have passed through the subject
        :return:
        """
        return sorted(self.subject_students)

    def add_student(self, student_object, rating_mark, exam_mark):
        try:
            if isinstance(student_object, Student) and isinstance(rating_mark, int) and isinstance(exam_mark, int):
                self.subject_students[str(student_object)] = {
                    "rating_mark": rating_mark,
                    "exam_mark": exam_mark
                }
            else:
                raise TypeError
        except TypeError:
            print("TypeError: student_object - must be 'Student' object, "
                  "rating_mark - must be integer, exam_mark - must be integer.")

    def remove_student(self, student_object):
        try:
            if isinstance(student_object, Student):
                self.subject_students.pop(str(student_object))
            else:
                raise TypeError
        except KeyError as e:
            print("KeyError: No such student %s." % e)
        except TypeError:
            print("TypeError: argument student_object - must be 'Student' object.")

    def __str__(self):
        return "%s" % self.subject_name


class GradeBook:
    """
    Class describes GradeBook object
    """

    def __init__(self):
        self.students_dict = {}
        self.subjects_dict = {}

    def get_students(self):
        """
        return sorted list of students in the GradeBook
        :return: students_list
        """
        return sorted(self.students_dict)

    def add_student(self, student_object):
        """
        add new student to students dictionary.
        :param student_object:
        :return:
        """
        try:
            if isinstance(student_object, Student):
                self.students_dict[str(student_object)] = student_object
            else:
                raise TypeError
        except TypeError:
            print("TypeError: student_object - must be 'Student' object.")

    def remove_student(self, student_object):
        """
        remove current student from students dictionary.
        :param student_object:
        :return:
        """
        try:
            if isinstance(student_object, Student):
                del self.students_dict[str(student_object)]
            else:
                raise TypeError
        except KeyError as e:
            print("KeyError: No such student %s." % e)
        except TypeError:
            print("TypeError: argument student_object - must be 'Student' object.")

    def add_subject(self, subject_object):
        """
        add new subject to subjects dictionary.
        :param subject_object:
        :return:
        """
        try:
            if isinstance(subject_object, Subject):
                self.subjects_dict[subject_object.subject_name] = subject_object
            else:
                raise TypeError
        except TypeError:
            print("TypeError: subject_object - must be 'Subject' object.")

    def remove_subject(self, subject_object):
        """
        remove current subject from subjects dictionary.
        :param subject_object:
        :return:
        """
        try:
            if isinstance(subject_object, Subject):
                del self.subjects_dict[subject_object.subject_name]
            else:
                raise TypeError
        except KeyError as e:
            print("KeyError: No such subject %s." % e)
        except TypeError:
            print("TypeError: argument subject_object - must be 'Subject' object.")

    def get_best_exam_student(self, subject_object):
        """
        returns the student/students with the highest examination scores obtained by the subject subject.
        :param subject_object:
        :return: list
        """
        top_students = []
        top_mark = 0
        if subject_object.subject_name in self.subjects_dict.keys():
            for student, marks in subject_object.subject_students.items():
                if not top_students:    # initialization
                    top_students.append(student)
                    top_mark = marks["exam_mark"]
                elif top_mark < marks["exam_mark"]:
                    # top_students.clear()
                    top_students = list()
                    top_students.append(student)
                    top_mark = marks["exam_mark"]
                elif top_mark == marks["exam_mark"]:    # if same top marks have 2 or more students
                    top_students.append(student)
            top_students.append(top_mark)   # add to end of list top mark among students
        return top_students

    def get_passed_exams(self):
        """
        returns all the subjects for which students take exams.
        :return: subjects_list
        """
        return sorted(self.subjects_dict)

    def print_result_grades(self):
        """
        outputs all the students names with the names of objects, which they passed.
        rating subject for this student = 0.3 * rating mark + 0.7 * examination mark,
        rounded to the nearest integer.
        :return: result strings
        """
        count = 1
        for student in sorted(self.students_dict.keys()):
            print("Student%i %s" % (count, student))
            for key in self.subjects_dict.keys():
                current_subject = self.subjects_dict[key]
                if student in current_subject.get_students():
                    result_mark = round(current_subject.subject_students[str(student)]["rating_mark"] * 0.3
                                        + current_subject.subject_students[str(student)]["exam_mark"] * 0.7)
                    print("\t%s - %i" % (key, result_mark))
            count += 1

    def __str__(self):
        return "GradeBook Object \n\r Students list -%s \n\r Subjects list - %s" \
               % (sorted(self.students_dict.keys()), sorted(self.subjects_dict.keys()))
