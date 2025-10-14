"""
Mohammed Azhar
Lab, 7 accessing data in a file
Sep 29, 2025
"""

from lab7_function import *
testing()
print("\n ---- example 1: reading file -----")
read_data("phrase.txt")

print("\n ---- example #2: Reading specific portion of a file-----")
read_up("phrases.txt")

print("\n --- example 3: reading specific portion using readline----")
read_readline("phrases.txt")

print("\n-----example 4: reading specific portion using readlines----")
read_all("phrases.txt")

print("\n-----example 5: loop through each line ----")
read_each("phrases.txt")

print("\n---- example 6: creating a new file -----")
new_file("last_name.txt")

print("\n---- example 7: append data into an existing file -----")
new_file("last_name.txt")

print("\n ---- EXERCISE -----")
count_yahoo = email_read("user_email.txt", "@yahoo")
count_gmail = email_read("user_email.txt", "@gmail")
count_hotmail = email_read("user_email.txt", "@hotmail")
with open("reportemail.txt", "w") as report:
    # Write the Gmail count into the file
    report.write(f"gmail = {count_gmail}\n")
    
    # Write the Yahoo count into the file
    report.write(f"yahoo = {count_yahoo}\n")
    
    # Write the Hotmail count into the file
    report.write(f"hotmail = {count_hotmail}\n")

print("Report has been generated: 'reportemail.txt'.")