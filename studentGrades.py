import psycopg2

# Establish connection to PostgreSQL database
conn = psycopg2.connect(
    dbname="rhysPy",
    user="rhysThompson",
    password="Thegecko@1995!",
    host="localhost",  # or your host IP if different
    port="5432"  # default PostgreSQL port
)


def create_students_table(conn):
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
	    First_name VARCHAR(20) NOT NULL,
	    Last_name VARCHAR(20) NOT NULL,
	    grade INTEGER NOT NULL
    )
''')

    # Commit the table creation
    conn.commit()
    cursor.close()


# Function to insert student data into the database
def insert_student_data(conn, First_name, Last_name, grade):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO student (First_name, Last_name, grade)
        VALUES (%s, %s, %s)
    ''', (First_name, Last_name, grade))
    conn.commit()
    cursor.close()


# An array to define grade categories alphabetically
grade_alphabetic = ['F', 'D', 'C', 'B', 'A', 'A+']

while True:
    # Prompt for first name input and validate
    while True:
        student_first_name = input("Enter Your First Name: ")

        if len(student_first_name) > 20:
            print("Error! Your first name must be 20 characters or fewer.")
        elif len(student_first_name) < 2:
            print("Error! Your first name must be between 2 and 20 characters long.")
        elif not student_first_name.isalpha():
            print("Error! Do not enter special characters or numbers.")
        else:
            break  # Exit the loop if the input is valid

    # Prompt for last name input and validate
    while True:
        student_last_name = input("Enter Your Last Name: ")

        if len(student_last_name) > 20:
            print("Error! Your last name must be 20 characters or fewer.")
        elif len(student_last_name) < 2:
            print("Error! Your last name must be between 2 and 20 characters long.")
        elif not student_last_name.isalpha():
            print("Error! Do not enter special characters or numbers.")
        else:
            break  # Exit the loop if the input is valid

    # Prompt for grade input and validate
    while True:
        student_grade_input = input("Please enter a student grade between 0 - 100: ")

        try:
            student_grade_input = int(student_grade_input)  # Convert user input to an integer

            if student_grade_input < 0 or student_grade_input > 100:
                print("Error! Grade must be between 0 and 100.")
            else:
                # Determine grade category based on numeric input
                if student_grade_input < 50:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[0]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[0])
                elif student_grade_input < 60:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[1]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[1])
                elif student_grade_input < 70:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[2]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[2])
                elif student_grade_input < 80:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[3]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[3])
                elif student_grade_input < 90:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[4]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[4])
                else:
                    print(f"Hello {student_first_name} {student_last_name}, your grade is {grade_alphabetic[5]}.")
                    insert_student_data(conn, student_first_name, student_last_name, grade_alphabetic[5])
                break  # Exit the loop after successful input

        except ValueError:
            print("Error! Please enter numeric data only.")

    another_student = input("Do you want to add another student? Press y to continue or n to close program: ").lower()
    if another_student != "yes":
        break

    # Reset variables for next student entry
    student_first_name = ''
    student_last_name = ''
    student_grade_input = ''

conn.close()
