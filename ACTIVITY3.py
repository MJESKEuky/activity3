#michael eskelson
#ISQA 3900
#ACTIVITY 3 PYTHON EXERCISE
def display_title():
    print("Grade Calculator Program")


def get_totalPoints():
    while True:
        try:
            total_points = float(input("Enter total points earned (0-1000): "))
            if 0 <= total_points <= 1000:
                return total_points
            else:
                print("Error: Total points must be between 0 and 1000. try again.")
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value.")


def get_letterGrade(average_earned):
    if average_earned >= 92:
        return 'A'
    elif average_earned >= 88:
        return 'B+'
    elif average_earned >= 82:
        return 'B'
    elif average_earned >= 78:
        return 'C+'
    elif average_earned >= 70:
        return 'C'
    elif average_earned >= 60:
        return 'D'
    else:
        return 'F'


def main():
    display_title()
    while True:
        total_points = get_totalPoints()
        average_earned = (total_points / 1000) * 100
        letter_grade = get_letterGrade(average_earned)
        print('Average score', average_earned,'%')
        print(f"Letter Grade: {letter_grade}")

        response = input("Do you want to continue? (yes/no): ")
        if response.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

