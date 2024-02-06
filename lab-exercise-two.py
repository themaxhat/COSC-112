# Test Score Average Lab

def main():
    student_first, student_last = student_name()
    
    test_scores = []

    print('')

    for i in range(5):
        score = int(input(f'Enter Test Score {i+1}: '))
        test_scores += [score]

    print('\n' + f'The full name of the sutdent is:\t{student_first}\t{student_last}' + '\n')

    for i in range(5):
        score = test_scores[i]
        print(f'The score and letter grade entered for Test {i+1} is:\t{score}\t{determine_grade(score)}')

    average_score = calc_average(test_scores)
    print('\n' + f'The Test Score Average and Letter Grade is:\t{average_score}\t{determine_grade(average_score)}')


def student_name():
    f = input("Enter first name of student: ")
    l = input("Enter last name of student: ")

    return f, l

def calc_average(list):
    return float(sum(list))/len(list)
    
def determine_grade(g):
    if g >= 90:
        return 'A'
    elif g >= 80:
        return 'B'
    elif g >= 70:
        return 'C'
    elif g >= 60:
        return 'D'
    else:
        return 'F'
    
main()