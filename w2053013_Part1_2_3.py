     # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
     # Any code taken from other sources is referenced within my code soluon.
     # Student ID: w2053013
     # Date: 12/13/2023

    # Import everything from the graphics module
from graphics import *

    # Initialize the variables to get different outputs
progress_value = 0
Trailer_value = 0
Retriever_value = 0
Exclude_value = 0
Outcome = ""
data_list = []   # Create (data_list) variable for store student output

    # Start infinite loop for enter students data
while True:
    try:
           #  Get and check the credits for error handling
        PASS_credits = int(input("Please Enter Your Credits At Pass - "))
        if PASS_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Number is out of range")
            continue   # If there is not any error skip and continue loop
           #  Get and check the credits for error handling
        DEFER_credits = int(input("Please Enter Your Credits At Defer - "))
        if DEFER_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Number is out of range")
            continue   # If there is not any error skip and continue loop
           #  Get and check the credits for error handling
        FAIL_credits = int(input("Please Enter Your Credits At Fail - "))
        if FAIL_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Number is out of range")
            continue   # If there is not any error skip and continue loop

    except ValueError:
        print("Please enter integer number only")   # Ask the user to enter Integer only
        continue

          # Determine the outputs of student progression based on credits values
    if PASS_credits == 120:
        Outcome = "Progress"
        progress_value += 1
    elif PASS_credits >= 100:
        Outcome = "Progress (module trailer)"
        Trailer_value += 1
    elif 60 <= PASS_credits <= 80:
        Outcome = "Do not Progress - module retriever"
        Retriever_value += 1
    elif  PASS_credits + DEFER_credits <= 40:
        Outcome = "Exclude"
        Exclude_value += 1

    if (PASS_credits + DEFER_credits + FAIL_credits) > 120:
        print("Total incorrect")
        continue
    total = (progress_value + Trailer_value + Retriever_value + Exclude_value)
    data_list.append(((PASS_credits, DEFER_credits, FAIL_credits), Outcome))
    print(Outcome)

    print("\nWould you like to enter another set of data?")   # Ask from user wants to continue or quit
    user_input = input("Enter 'Y' for continue and 'Q' for quit: ")
    user_input = user_input.upper()

    if user_input not in ['Y', 'Q']:
        print("Please type 'Y' or 'Q'")
        user_input = input("Would you like to enter another set of data?\
        Enter 'Y' for yes or 'Q' for quit and show your results :")

    if user_input == 'Y':
        continue
    elif user_input == 'Q':
        break

win = GraphWin("Histogram", 800, 600)   # Create the graphics window
win.setBackground("white")

      # Display heading of the Histogram window
histogram_heading = Text(Point(200, 30), "Histogram results")
histogram_heading.setTextColor = ("black")
histogram_heading.setSize(21)
histogram_heading.setStyle("bold")
histogram_heading.draw(win)

   # Condition for the outcomes representation in the histogram.)
if total <= 1:
    bottom_caption = Text(Point(230, 510), str(total) + " outcomes in total.")
else:
    bottom_caption = Text(Point(230, 510), str(total) + " outcomes in total.")
bottom_caption.setTextColor = ("purple")
bottom_caption.setSize(18)
bottom_caption.setStyle("bold")
bottom_caption.draw(win)

   # Histogram column representation
Histogram_column_1 = progress_value * 20
Histogram_column_2 = Trailer_value * 20
Histogram_column_3 = Retriever_value * 20
Histogram_column_4 = Exclude_value * 20

column_1 = Rectangle(Point(75, 450), Point(185, (450 - (progress_value) * 20)))
column_1.setFill("slategray")
column_1.draw(win)

column_2 = Rectangle(Point(205, 450), Point(315, (450 - (Trailer_value) * 20)))
column_2.setFill('thistle')
column_2.draw(win)

column_3 = Rectangle(Point(335, 450), Point(445, (450 - (Retriever_value) * 20)))
column_3.setFill('wheat')
column_3.draw(win)

column_4 = Rectangle(Point(465, 450), Point(575, (450 - (Exclude_value) * 20)))
column_4.setFill('red')
column_4.draw(win)

   # Name of each column and bottom line
column_1_name = Text(Point(130, 470), 'Progress')
column_1_name.setSize(16)
column_1_name.setFill('dark blue')
column_1_name.setStyle('bold')
column_1_name.draw(win)

column_2_name = Text(Point(260, 470), 'Trailer')
column_2_name.setSize(16)
column_2_name.setFill('dark blue')
column_2_name.setStyle('bold')
column_2_name.draw(win)

column_3_name = Text(Point(390, 470), 'Retriever')
column_3_name.setSize(16)
column_3_name.setStyle('bold')
column_3_name.setFill('dark blue')
column_3_name.draw(win)

column_4_name = Text(Point(520, 470), 'Excluded')
column_4_name.setSize(16)
column_4_name.setStyle('bold')
column_4_name.setFill('dark blue')
column_4_name.draw(win)

# Displaying lines in histogram chart
a_row = Line(Point(45, 450), Point(605, 450))
a_row.draw(win)

   # Save data to a text file
with open("credit_outcome.txt", "w") as file:
    file.write("Part 3:\n")
    for i in data_list:
        file.write(f"{i[1]} - {i[0][0]}, {i[0][1]}, {i[0][2]}\n")

win.getMouse()   # Add mouse click to close the window
win.close()   # Close the graphics window

print("\nPart 2:")
for i in data_list:
    print(f"{i[0]} - {i[1]}")

print("Successfully created file")

input("Press Enter to exit")
