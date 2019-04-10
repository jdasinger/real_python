input_file = open("poem.txt", "r")

output_file = open("poem_copy.txt", "w")

for line in input_file.readlines():
	output_file.write(line)

input_file.close()
output_file.close()

