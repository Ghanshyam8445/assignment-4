**for task 1(1.py)**
The try Block
This section contains the code that might fail.
with open('sample.txt', 'r') as file:: It attempts to open a file named sample.txt in "read" mode ('r'). Using the with statement is a best practice because it automatically closes the file once the task is done, even if an error occurs.
**The Loop:** If the file opens successfully, it iterates through every line and prints it. The .strip() method is used to remove extra whitespace or the "newline" character at the end of each line so the output looks clean.
**The except Blocks (Error Handling)**
These act as a safety net if something goes wrong in the try block:
**FileNotFoundError:** If the file sample.txt isn't in the folder, the program won't crash. Instead, it catches this specific error and prints a friendly message: "Error: The file sample.txt does not exist.
**"Exception as e:** This is a "catch-all" for any other problems (like the file being corrupted or a lack of system permissions). it captures the error message and prints it so you know exactly what went wrong.
**for task 2(2.py)**
