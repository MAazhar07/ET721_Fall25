"""
Mohammed Azhar
Lab, 7 accessing data in a file (functions)
Sep 29, 2025
"""
def testing():
    print("Mohammed Azhar")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line in a file with a Phython code
    with open(filename, "r") as file1:
        filecontent = file1.read()
        print(filecontent)
    # check if the file is closed. If it is closed, it should return True
    print(f"Is the file closed? {file1.closed}")

# EXAMPLE 1: reading specific portion of a file
def read_up(filename):
    with open (filename,"r")as file1:
            #read the first 30 characters
            print(file1.read(30))
            #read the next 5 characters
            print(file1.read(5))
# EXAMPLE 2: Reading specific portion of a file
def read_up (filename):
     with open(filename,"r") as file1:
          #read the first 30 characters
          print(file1.read(30))
          #read the next 5 characters
          print(file1.read(5))

     print(file1.read(5))
# EXAMPLE 3: readline 
def read_readline(filename):
     with open(filename, "r") as file1:
          # read up to 30 characters of the first line
          print(file1.readline(30))
          #continues reading next line up to 5 characters
          print(file1.readlines()) 

# EXAMPLE 4: readline
def read_all(filename):
     with open (filename, "r")as file1:
          print(file1.readlines())

#EXAMPLE 5: loop through a readlines file
def read_all(filename):
     with open (filename, "r")as file1:
          filelines = file1.readlines()

          #loop through each item in 'filelines'
          for eachline in filelines:
            print(eachline.strip())
          #strip()removes the newline character \n

#EXAMPLE 6: create a new file
def new_file(filename):
     with open (filename, "w")as file:
          file.write("Python Basics for data analysis\n")
          file.write("student's full name")

#EXAMPLE 7: append data into an existing file
def stamp_date(filename):
     with open(filename, "a") as file:
          file.write(f"\n\n{datetime.now()}")


# EXERCISE
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