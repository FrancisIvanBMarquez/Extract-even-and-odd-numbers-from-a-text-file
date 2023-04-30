# Extract-even-and-odd-numbers-from-a-text-file_Marquez Francis Ivan B._BSCpE 1-5

# Read numbers.txt
with  open("numbers.txt", "r") as my_file:
    for line in my_file:
        print (line.strip())



# Create even.txt and odd.txt
# Append even numbers to even.txt
# Append odd numbers to odd.txt