# This function prompts the user for course and section number


def getCourseSec():
    print('Please provide valid course and section numbers.')
    while True:
        # Prompt for course number
        course_number = input("Enter a 4-digit course number: ")
        
        # Validate course number
        if not course_number.isdigit() or len(course_number) != 4:
            print("Invalid input. Please enter a 4-digit course number.")
            continue
        
        # Prompt for section number
        section_number = input("Enter a 3-digit section number: ")
        
        # Validate section number
        if not section_number.isdigit() or len(section_number) != 3:
            print("Invalid input. Please enter a 3-digit section number.")
            continue
        
        # If both course and section numbers are valid, break out of the loop
        break
    
    return course_number, section_number