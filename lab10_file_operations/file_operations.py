"""
Mohammed Azhar
Oct 15, 2025
Lab 9, file operation test
"""


def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)


def read_file(filename):
    with open(filename, "r") as file:
        return file.read()


def append_file(filename, msg):
    with open(filename, "a") as file:
        file.write(msg)

    # function from lab 7


def email_read(filename, email):
    try:
        count_email = 0
        with open(filename, "r") as file1:
            filelines = file1.readlines()

            # Loop through each line in the file
            for eachline in filelines:
                print(eachline.strip())
                # Check if the email domain exists in the line (e.g. '@gmail', '@yahoo', etc.)
                if email in eachline:
                    count_email += 1
        # Return the final count
        return count_email

    except FileNotFoundError:
        # Exception if the file is not found
        print(f"Error: The file {filename} was not found.")
        return 0
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"An error occurred: {e}")
        return 0
