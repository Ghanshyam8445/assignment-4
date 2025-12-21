# Task 2: Write and Append Data to a File

# Take user input
data = input("Enter data to write to the file: ")

# Write data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
additional_data = input("Enter additional data to append: ")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")

# Read and display final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())