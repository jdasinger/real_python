with open("poem.txt", "r") as input_file, open("poem_copy.txt", "w") as output_file:

for line in input_file.readlines():
	output_file.write(line)


