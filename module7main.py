# Dictionaries for course information
course_roomnumber = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411"
}

course_instructornames = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

course_meetingtimes = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

# Function to retrieve and display course information
def get_course_info(course_number):
    try:
        # Lookup values safely
        room_number = course_roomnumber.get(course_number)
        instructor_name = course_instructornames.get(course_number)
        meeting_time = course_meetingtimes.get(course_number)

        # If any of the details are missing, raise an error
        if not (room_number and instructor_name and meeting_time):
            raise KeyError("Course not found.")

        # Display the course details
        print(f"\nCourse: {course_number}")
        print(f"Room Number: {room_number}")
        print(f"Instructor: {instructor_name}")
        print(f"Meeting Time: {meeting_time}")

    # Exception handling for missing or invalid input
    except KeyError as e:
        print(f"Error: {e}")


def main():
    while True:
        # Prompt user input
        course_number = input("Enter a course number (e.g., CSC101) or 'exit' to quit: ").strip().upper()

        # Exit condition
        if course_number.lower() == "exit":
            print("Exiting program. Goodbye!")
            break

        # Validate input format (must be letters + numbers, e.g., CSC101)
        if not course_number[:3].isalpha() or not course_number[3:].isdigit():
            print("Invalid format. Course numbers must be like 'CSC101' or 'NET110'. Try again.")
            continue

        # Retrieve and display course info
        get_course_info(course_number)


# Run the program
if __name__ == "__main__":
    main()
