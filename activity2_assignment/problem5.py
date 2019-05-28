def check_student_gpa(gpa_tuple):
    """
    return name and GPA of the top student

    parameter
    --------------
    gpa_tuple : string and integer tuple
        student name and GPA

    return
    --------------
    gpa_tuple[0], top_score : string and integer
        student name and GPA of the top student
    """
    top_score = 0
    for i in range(1, len(gpa_tuple)):
        if top_score < gpa_tuple[i]:
            top_score = gpa_tuple[i]
    return gpa_tuple[0], top_score


def main():
    """
    problem5
    call function
    """

    # testcase
     gpa_tuple = ("Ali", 67, 87, 90, 45, 39)
     print(check_student_gpa(gpa_tuple))

main()
