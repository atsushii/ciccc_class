def check_student_avarage(student_dict):
    """
    return hight avarage student

    parameter
    --------------
    student_dict : dictionary
        there are student information in dictionary

    return
    -------------
    highest_avarage_student : dictionary
        student who has highest avarage
    """

    high_avarage = 0
    highest_avarage_student = {}
    for student in student_dict:
        if student['Avarage'] > high_avarage:
            high_avarage = student['Avarage']
            highest_avarage_student = student

    return highest_avarage_student

def main():
    """
    problem4
    create student info
    """

    student_dict = [
        {
            'firstName' : 'Jan',
            'lastName' : 'Min',
            'address' : 'Tokyo',
            'year of birth' : 1993,
            'Avarage' : 122
        },
        {
            'firstName' : 'Atsushi',
            'lastName' : 'Miyamoto',
            'address' : 'Vancuver',
            'year of birth' : 1994,
            'Avarage' : 1000
        },
        {
            'firstName' : 'Leo',
            'lastName' : 'doksdo',
            'address' : 'Malta',
            'year of birth' : 2000,
            'Avarage' : 30
        },

    ]

    print(check_student_avarage(student_dict))

main()
