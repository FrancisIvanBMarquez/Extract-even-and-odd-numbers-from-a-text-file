# Extract-even-and-odd-numbers-from-a-text-file_Marquez Francis Ivan B._BSCpE 1-5

# Read numbers.txt
# Create files for even and odd numbers
with  open("numbers.txt", "r") as my_file1, open ("even_numbers.txt", "a") as my_file2, open ("odd_numbers.txt", "a") as my_file3:
    for line in my_file1:
        # if else for reading lines
        # if even
        if (int(line) % 2) == 0:
            my_file2.write(line)
        

# Append even numbers to even.txt
# if odd
# Append odd numbers to odd.txt