# -*- coding: utf-8 -*-
"""lab1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1DINYncCI3KM9MngfCKmQf4EmKpoPNU0V
"""

import random
from google.colab import files

def read_student_ids(filename):
    """Reads student IDs from a file and returns them as a list."""
    try:
        with open(filename, 'r') as file:
            student_ids = [line.strip() for line in file.readlines() if line.strip()]
        if not student_ids:
            raise ValueError("The file is empty.")
        return student_ids
    except FileNotFoundError:
        print("Error: The file was not found.")
        return []
    except ValueError as e:
        print(f"Error: {e}")
        return []

def conduct_viva(student_list):
    """Randomly selects and prints students for viva until the list is exhausted."""
    viva_counter = 1
    remaining_students = student_list.copy()

    while remaining_students:
        selected_student = random.choice(remaining_students)
        print(f"Viva #{viva_counter}: {selected_student}")
        remaining_students.remove(selected_student)
        viva_counter += 1

    print("\nAll students have been selected. Resetting the list for next round.\n")
    return student_list  # Return the full list to reset the process

def main():
    # Prompt the user to upload a file in Colab
    print("Please upload the 'student_ids.txt' file.")
    uploaded = files.upload()  # This will open a file upload dialog in Colab

    filename = 'student_ids.txt'
    if filename in uploaded:
        student_list = read_student_ids(filename)

        if student_list:
            while True:
                student_list = conduct_viva(student_list)
                user_input = input("Do you want to repeat the process? (yes/no): ").strip().lower()
                if user_input != 'yes':
                    break
    else:
        print("Error: 'student_ids.txt' not uploaded.")

if __name__ == "__main__":
    main()