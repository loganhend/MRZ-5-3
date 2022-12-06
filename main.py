from nn import *

if __name__ == '__main__':
    p, e, a, N, col = 0, 0, 0, 0, 0

    print("1) Educate NN\n2) Predict\n")
    choice1 = input("Enter number: ")

    if choice1 == '1':
        print("1) Enter settings\n2) Default settings\n")
        settings_choice = input("Choose option: ")

        if settings_choice == '1':
            p = input("Enter screen size (p): ")
            e = input("Enter max error (e): ")
            a = input("Enter alpha (a): ")
            N = input("Enter number of iterations (N): ")
            col = input("Enter number of columns (col): ")
        elif settings_choice == '2':
            p = 8
            e = 0.00001
            a = 0.00001
            N = 1000000
            col = 4

        training_sequence = input("Enter training sequence num: ")

        study(N, col, int(training_sequence)-1, p, e, a)

    elif choice1 == '2':

        print('Enter a list of elements of sequence to continue')
        print('After entering the last element press "enter" instead of extra-number')
        element = float(input('> '))
        user_sequence = []
        while True:
            try:
                user_sequence.append([element])
                element = float(input('> '))
            except:
                break

        continue_num = input("Enter the number of numbers to predict: ")
        predict_nums(user_sequence, int(continue_num))